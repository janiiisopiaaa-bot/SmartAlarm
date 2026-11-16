import winsound
waktualarm = "Belum diatur"
statusalarm = "Mati"

print("===== SMART ALARM =====")
print("1. Atur alarm\n2. Aktifkan alarm\n3. Nonaktifkan alarm\n4. Cek status alarm\n5. Tes Bunyi\n6. Exit")

pilihan = input("pilih menu(1-5) : ")

if pilihan == "1":
    waktualarm = input("Mau jam berapa? ")
    print("Alarm berhasil diatur ke jam " + waktualarm)

elif pilihan == "2":
    statusalarm = "Aktif"
    print("Alarm sudah DIAKTIFKAN!")

elif pilihan == "3":
    statusalarm = "Mati"
    print("Alarm sudah DIMATIKAN!")

elif pilihan == "4":
    print("Jam Alarm : " + waktualarm)
    print("Status saat in : " +statusalarm)

elif pilihan == "5":
    print("\a BIIIIP... BIIIIP... Alarm Berbunyi!")
    # windsound.Beep(frekuensi, durasi_milidetik)
    # Frekuensi 2000 (nyaring), durasi 10000 milidetik (10 detik)
    winsound.Beep(2000, 10000)

elif pilihan == "6":
    print("Program  selesai, terima kasih!")