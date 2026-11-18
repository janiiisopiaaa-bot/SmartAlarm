from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/visualisasi")
def visualisasi():
    return render_template("visualisasi.html")


# Hanya untuk dijalankan di komputer sendiri (python app.py).
# Di Vercel, variabel `app` di atas yang dipakai otomatis.
if __name__ == "__main__":
    app.run(debug=True)
