import pywhatkit

try:
    # Meminta input nama lagu
    lagu = input("Masukkan Nama Lagu Yang Diputar: ")

    # Memutar lagu di YouTube
    pywhatkit.playonyt(lagu)

    # Menyimpan riwayat ke file
    with open("riwayat_lagu.txt", "a") as file:
        file.write(lagu + "\n")

    print("Lagu:", lagu)
    print("Berhasil Diputar")
    print("Riwayat lagu telah disimpan.")
except Exception as e:
    print("Terjadi kesalahan:", str(e))
