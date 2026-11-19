import os
from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Flask, render_template, session, redirect, url_for, request, jsonify

app = Flask(__name__)
# Kunci untuk mengamankan cookie. Di Vercel, isi lewat Environment Variable SECRET_KEY.
app.secret_key = os.environ.get("SECRET_KEY", "ganti-kunci-ini")

ZONA = ZoneInfo("Asia/Jakarta")


def sekarang():
    return datetime.now(ZONA)


def ambil():
    """Ambil data alarm dari cookie (pengganti variabel waktualarm & statusalarm)."""
    return session.get("waktualarm", "Belum diatur"), session.get("statusalarm", "Mati")


@app.route("/")
def home():
    waktualarm, statusalarm = ambil()
    return render_template(
        "index.html",
        waktualarm=waktualarm,
        statusalarm=statusalarm,
        jam=sekarang().strftime("%H:%M:%S"),
        pesan=request.args.get("pesan", ""),
        tes=request.args.get("tes") == "1",
    )


# Menu 1: Atur alarm
@app.route("/atur", methods=["POST"])
def atur():
    waktu = request.form.get("waktu", "")
    if waktu:
        session["waktualarm"] = waktu
        pesan = "Alarm berhasil diatur ke jam " + waktu
    else:
        pesan = "Pilih jam dulu"
    return redirect(url_for("home", pesan=pesan))


# Menu 2: Aktifkan alarm
@app.route("/aktif", methods=["POST"])
def aktif():
    if "waktualarm" not in session:
        return redirect(url_for("home", pesan="Atur jam alarm dulu"))
    session["statusalarm"] = "Aktif"
    return redirect(url_for("home", pesan="Alarm sudah DIAKTIFKAN!"))


# Menu 3: Nonaktifkan alarm
@app.route("/nonaktif", methods=["POST"])
def nonaktif():
    session["statusalarm"] = "Mati"
    return redirect(url_for("home", pesan="Alarm sudah DIMATIKAN!"))


# Menu 5: Tes bunyi (bunyinya diputar browser, Python hanya memberi perintah)
@app.route("/tes", methods=["POST"])
def tes():
    return redirect(url_for("home", pesan="BIIIIP... Tes bunyi", tes=1))


# Dipanggil browser tiap detik: Python yang memutuskan apakah alarm harus bunyi
@app.route("/cek")
def cek():
    waktualarm, statusalarm = ambil()
    now = sekarang()
    bunyi = statusalarm == "Aktif" and waktualarm == now.strftime("%H:%M")
    return jsonify(jam=now.strftime("%H:%M:%S"), bunyi=bunyi)


# Halaman visualisasi: semua dihitung di Python
@app.route("/visualisasi")
def visualisasi():
    waktualarm, statusalarm = ambil()
    now = sekarang()
    menit_now = now.hour * 60 + now.minute

    persen_alarm = None
    sisa = ""
    if waktualarm != "Belum diatur":
        h, m = map(int, waktualarm.split(":"))
        menit_alarm = h * 60 + m
        persen_alarm = menit_alarm / 1440 * 100
        selisih = (menit_alarm - menit_now) % 1440
        sisa = f"{selisih // 60} jam {selisih % 60} menit lagi"

    return render_template(
        "visualisasi.html",
        waktualarm=waktualarm,
        statusalarm=statusalarm,
        persen_now=menit_now / 1440 * 100,
        persen_alarm=persen_alarm,
        sisa=sisa,
    )


if __name__ == "__main__":
    app.run(debug=True)
