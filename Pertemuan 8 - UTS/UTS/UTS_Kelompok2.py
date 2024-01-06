import math


# Fungsi untuk menghitung volume limas segitiga
def volume_limas_segitiga(alas, tinggi):
    return (1/3) * (1/2 * alas ** 2) * tinggi

# Fungsi untuk menghitung luas permukaan limas segitiga
def luas_permukaan_limas_segitiga(alas, tinggi, sisi_miring):
    return (1/2 * alas * sisi_miring) + (alas * tinggi)

# Fungsi untuk menghitung keliling limas segitiga
def keliling_limas_segitiga(alas, sisi_miring):
    return alas + 3 * sisi_miring

# Fungsi untuk menghitung volume limas segi empat
def volume_limas_segi_empat(alas, tinggi):
    return (1/3) * (alas ** 2) * tinggi

# Fungsi untuk menghitung luas permukaan limas segi empat
def luas_permukaan_limas_segi_empat(alas, tinggi, sisi_miring):
    return (alas ** 2) + 4 * (1/2 * alas * sisi_miring)

# Fungsi untuk menghitung keliling limas segi empat
def keliling_limas_segi_empat(alas):
    return 4 * alas

# Fungsi untuk menghitung volume kerucut
def volume_kerucut(jari_jari, tinggi):
    volume = (1/3) * math.pi * (jari_jari ** 2) * tinggi
    return volume

# Fungsi untuk menghitung luas permukaan kerucut
def luas_permukaan_kerucut(jari_jari, sisi_miring):
    return math.pi * jari_jari * (jari_jari + sisi_miring)

# Fungsi untuk menghitung keliling, volume, dan luas permukaan Prisma Segitiga
def prisma_segitiga(keliling_alas, tinggi):
    # Keliling alas
    K = keliling_alas
    # Volume
    V = (1/2) * K * tinggi
    # Luas permukaan
    L = K * tinggi + 2 * keliling_alas
    return K, V, L

# Fungsi untuk menghitung keliling, volume, dan luas permukaan Balok
def balok(panjang, lebar, tinggi):
    # Keliling alas
    K = 2 * (panjang + lebar)
    # Volume
    V = panjang * lebar * tinggi
    # Luas permukaan
    L = 2 * (panjang*lebar + panjang*tinggi + lebar*tinggi)
    return K, V, L

# Fungsi untuk menghitung keliling, volume, dan luas permukaan Bola
def bola(jari_jari):
    # Keliling
    C = 2 * math.pi * jari_jari
    # Volume
    V = (4/3) * math.pi * jari_jari**3
    # Luas permukaan
    A = 4 * math.pi * jari_jari**2
    return C, V, A

# Fungsi menghitung luas alas prisma segi lima
def luas_alas_prisma_segi_lima(sisi):
    return 5 * sisi ** 2 / (4 * math.tan(math.pi / 5))


# Fungsi menghitung volume prisma segi empat
def volume_prisma_segi_empat(panjang, lebar, tinggi):
    return panjang * lebar * tinggi


# Fungsi menghitung luas permukaan prisma segi empat
def luas_permukaan_prisma_segi_empat(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)


# Fungsi menghitung keliling prisma segi empat
def keliling_prisma_segi_empat(panjang, lebar, tinggi):
    return 2 * (panjang + lebar) + 4 * tinggi


# Fungsi menghitung volume prisma segi lima
def volume_prisma_segi_lima(sisi, tinggi):
    luas_alas = luas_alas_prisma_segi_lima(sisi)
    return round(luas_alas * tinggi, 1)


# Fungsi menghitung luas permukaan prisma segi lima
def luas_permukaan_prisma_segi_lima(sisi, tinggi):
    luas_alas = luas_alas_prisma_segi_lima(sisi)
    return round(5 * luas_alas + 5 * sisi * tinggi, 1)


# Fungsi menghitung keliling prisma segi lima
def keliling_prisma_segi_lima(sisi):
    return round(5 * sisi, 1)


# Fungsi menghitung volume limas segi lima
def volume_limas_segi_lima(sisi, tinggi):
    luas_alas = luas_alas_prisma_segi_lima(sisi)
    return round(luas_alas * tinggi / 3, 1)


# Fungsi menghitung luas permukaan limas segi lima
def luas_permukaan_limas_segi_lima(sisi, tinggi):
    luas_alas = luas_alas_prisma_segi_lima(sisi)
    return round(luas_alas + (5 * sisi * tinggi) / 2, 1)


# FUNGSI RUMUS FISIKA
# Fungsi untuk menghitung frekuensi
def hitung_frekuensi(kecepatan, panjang_gelombang):
    frekuensi = kecepatan / panjang_gelombang
    return frekuensi

# Fungsi untuk menghitung impuls
def hitung_impuls(massa, delta_kecepatan):
    impuls = massa * delta_kecepatan
    return impuls

# Fungsi untuk menghitung massa jenis
def hitung_massa_jenis(massa, volume):
    massa_jenis = massa / volume
    return massa_jenis

# Fungsi untuk menghitung gaya
def hitung_gaya(massa, percepatan):
    gaya = massa * percepatan
    return gaya

# Fungsi untuk menghitung panjang gelombang
def hitung_panjang_gelombang(kecepatan, frekuensi):
    panjang_gelombang = kecepatan / frekuensi
    return panjang_gelombang

# Fungsi untuk menghitung intensitas cahaya
def hitung_intensitas_cahaya(daya, luas_permukaan):
    intensitas_cahaya = daya / luas_permukaan
    return intensitas_cahaya


# Fungsi untuk menampilkan menu matematika
def menu_mtk():
    print("\n==========MENU MATEMATIKA==========")
    print("1. Rumus limas segitiga")
    print("2. Rumus limas segi empat")
    print("3. Rumus kerucut")
    print("4. Rumus prisma segitiga")
    print("5. Rumus balok")
    print("6. Rumus bola")
    print("7. Rumus prisma segi empat")
    print("8. Rumus prisma segi lima")
    print("9. Rumus limas segi lima")
    print("10. Menu utama")

# Fungsi untuk menampilkan menu fisika
def menu_fisika():
    print("\n============MENU FISIKA============")
    print("1. Rumus frekuensi")
    print("2. Rumus impuls")
    print("3. Rumus massa jenis")
    print("4. Rumus gaya")
    print("5. Rumus panjang gelombang")
    print("6. Rumus intensitas cahaya")
    print("7. Menu utama")

# Fungsi untuk menampilkan menu utama
def menu_utama():
    while True:
        print("\n============MENU UTAMA============")
        print("1. Rumus Matematika")
        print("2. Rumus Fisika")
        print("3. Keluar")

        pilihan_menu = int(input("Pilih untuk memilih menu (1/2/3): "))

        if pilihan_menu == 1:
            while True: 
                menu_mtk()
                pilihan_matematika = int(input("Pilih perintah operasi matematika (1-9): "))

                # Pilihan rumus matematika
                if pilihan_matematika == 1:
                    # Input variabel limas segitiga
                    alas_limas_segitiga = float(input("Masukkan panjang sisi alas limas segitiga: "))
                    tinggi_limas_segitiga = float(input("Masukkan tinggi limas segitiga: "))
                    sisi_miring_limas_segitiga = float(input("Masukkan panjang sisi miring limas segitiga: "))

                    # Menampikan hasil
                    print("\nVolume Limas Segitiga :", volume_limas_segitiga(alas_limas_segitiga, tinggi_limas_segitiga))
                    print("Luas Permukaan Limas Segitiga :", luas_permukaan_limas_segitiga(alas_limas_segitiga, tinggi_limas_segitiga, sisi_miring_limas_segitiga))
                    print("Keliling Limas Segitiga :", keliling_limas_segitiga(alas_limas_segitiga, sisi_miring_limas_segitiga))
                elif pilihan_matematika == 2:
                    # Input variabel limas segi empat
                    alas_limas_segi_empat = float(input("Masukkan panjang sisi alas limas segi empat: "))
                    tinggi_limas_segi_empat = float(input("Masukkan tinggi limas segi empat: "))
                    sisi_miring_limas_segi_empat = float(input("Masukkan panjang sisi miring limas segi empat: "))

                    # Menampilkan hasil
                    print("\nVolume Limas Segi Empat :", volume_limas_segi_empat(alas_limas_segi_empat, tinggi_limas_segi_empat))
                    print("Luas Permukaan Limas Segi Empat :", luas_permukaan_limas_segi_empat(alas_limas_segi_empat, tinggi_limas_segi_empat, sisi_miring_limas_segi_empat))
                    print("Keliling Limas Segi Empat :", keliling_limas_segi_empat(alas_limas_segi_empat))
                elif pilihan_matematika == 3:
                    # Input variabel kerucut
                    jari_jari_kerucut = float(input("Masukkan jari-jari kerucut: "))
                    tinggi_kerucut = float(input("Masukkan tinggi kerucut: "))

                    # Menghitung volume kerucut
                    volume = volume_kerucut(jari_jari_kerucut, tinggi_kerucut)

                    # Menghitung luas permukaan kerucut
                    sisi_miring_kerucut = math.sqrt(jari_jari_kerucut ** 2 + tinggi_kerucut ** 2)
                    luas_permukaan = luas_permukaan_kerucut(jari_jari_kerucut, sisi_miring_kerucut)

                    # Menampilkan hasil
                    print("\nVolume Kerucut : ", volume)
                    print("Luas Permukaan Kerucut : ", luas_permukaan)
                elif pilihan_matematika == 4:
                    # Input dari pengguna untuk Prisma Segitiga
                    keliling_alas_prisma = float(input("Masukkan keliling alas segitiga : "))
                    tinggi_prisma = float(input("Masukkan tinggi prisma : "))
                    hasil_keliling, hasil_volume, hasil_luas = prisma_segitiga(keliling_alas_prisma, tinggi_prisma)

                    # Menampilkan hasil
                    print("\nPrisma Segitiga:")
                    print("Prisma segitiga adalah bangun ruang tiga dimensi yang memiliki segitiga sebagai alasnya")
                    print("Prisma Segitiga dengan keliling alas", {keliling_alas_prisma}, "dan tinggi" ,{tinggi_prisma}, ", Dapat kita hitung ")
                    print(f"\nKeliling Prisma Segitiga : {hasil_keliling}")
                    print(f"Volume Prisma Segitiga : {hasil_volume}")
                    print(f"Luas Permukaan Prisma Segitiga : {hasil_luas}")
                elif pilihan_matematika == 5:
                    # Input dari pengguna untuk Balok
                    panjang_balok = float(input("Masukkan panjang balok : "))
                    lebar_balok = float(input("Masukkan lebar balok : "))
                    tinggi_balok = float(input("Masukkan tinggi balok : "))
                    hasil_keliling, hasil_volume, hasil_luas = balok(panjang_balok, lebar_balok, tinggi_balok)

                    # Menampilkan hasil
                    print("\nBalok:")
                    print("Balok adalah bangun ruang tiga dimensi yang memiliki dua sisi yang berbentuk persegi atau persegi panjang sebagai alas dan tutupnya")
                    print("Balok dengan panjang", {panjang_balok} , "lebar", {lebar_balok}, "dan tinggi", {tinggi_balok}, ", Dapat kita hitung.")
                    print(f"\nKeliling Balok : {hasil_keliling}")
                    print(f"Volume Balok : {hasil_volume}")
                    print(f"Luas Permukaan Balok : {hasil_luas}")
                elif pilihan_matematika == 6:
                    # Input dari pengguna untuk Bola
                    jari_jari_bola = float(input("Masukkan jari-jari bola : "))
                    hasil_keliling, hasil_volume, hasil_luas = bola(jari_jari_bola)

                    # Menampilkan Hasil
                    print("\nBola:")
                    print("Bola adalah bangun ruang tiga dimensi yang memiliki bentuk bulat sempurna")
                    print("Bola dengan Jari-jari", {jari_jari_bola}, ", Dapat kita hitung ")
                    print(f"\nKeliling Bola : {hasil_keliling}")
                    print(f"Volume Bola : {hasil_volume}")
                    print(f"Luas Permukaan Bola : {hasil_luas}")
                elif pilihan_matematika == 7:
                    # Input dan penghitungan prisma segi empat
                    print("=== INPUT PENGHITUNGAN PRISMA SEGI EMPAT ===")
                    panjang = float(input("Masukkan panjang prisma segi empat: "))
                    lebar = float(input("Masukkan lebar prisma segi empat: "))
                    tinggi_prisma_empat = float(input("Masukkan tinggi prisma segi empat: "))

                    # Menghitung volume, luas permukaan, dan keliling prisma segi empat
                    volume_pse = volume_prisma_segi_empat(panjang, lebar, tinggi_prisma_empat)
                    luas_permukaan_pse = luas_permukaan_prisma_segi_empat(panjang, lebar, tinggi_prisma_empat)
                    keliling_pse = keliling_prisma_segi_empat(panjang, lebar, tinggi_prisma_empat)

                    # Menampilkan hasil
                    print("\n==== HASIL PERHITUNGAN RUMUS ===")
                    print("Prisma Segi Empat")
                    print(f"Volume: {volume_pse}")
                    print(f"Luas Permukaan: {luas_permukaan_pse}")
                    print(f"Keliling: {keliling_pse}")
                elif pilihan_matematika == 8:
                    # Input dan penghitungan prisma segi lima
                    print("\n=== INPUT PENGHITUNGAN PRISMA SEGI LIMA ===")
                    sisi_prisma_lima = float(input("Masukkan panjang sisi prisma segi lima: "))
                    tinggi_prisma_lima = float(input("Masukkan tinggi prisma segi lima: "))

                    # Menghitung volume, luas permukaan, dan keliling prisma segi lima
                    volume_psl = volume_prisma_segi_lima(sisi_prisma_lima, tinggi_prisma_lima)
                    luas_permukaan_psl = luas_permukaan_prisma_segi_lima(sisi_prisma_lima, tinggi_prisma_lima)
                    keliling_psl = keliling_prisma_segi_lima(sisi_prisma_lima)

                    # Menampilkan hasil
                    print("\n==== HASIL PERHITUNGAN RUMUS ===")
                    print("Prisma Segi Lima")
                    print(f"Volume: {volume_psl}")
                    print(f"Luas Permukaan: {luas_permukaan_psl}")
                    print(f"Keliling: {keliling_psl}")
                elif pilihan_matematika == 9:
                    # Input dan penghitungan limas segi lima
                    print("\n=== INPUT PENGHITUNGAN LIMAS SEGI LIMA ===")
                    sisi_limas_lima = float(input("Masukkan panjang sisi limas segi lima: "))
                    tinggi_limas_lima = float(input("Masukkan tinggi limas segi lima: "))

                    # Menghitung volume, luas permukaan, dan keliling limas segi lima
                    volume_lsl = volume_limas_segi_lima(sisi_limas_lima, tinggi_limas_lima)
                    luas_permukaan_lsl = luas_permukaan_limas_segi_lima(sisi_limas_lima, tinggi_limas_lima)

                    # Menampilkan hasil
                    print("\n==== HASIL PERHITUNGAN RUMUS ===")
                    print("\nLimas Segi Lima")
                    print(f"Volume: {volume_lsl}")
                    print(f"Luas Permukaan: {luas_permukaan_lsl}")
                elif pilihan_matematika == 10:
                    break
                else:
                    print("Menu yang kamu pilih tidak valid, pilih angka 1-10")

        elif pilihan_menu == 2:
            while True:
                menu_fisika()
                pilihan_fisika = int(input("Pilih perintah operasi fisika (1-7): "))

                # Pilihan rumus fisika
                if pilihan_fisika == 1:
                    kecepatan = float(input("Masukkan kecepatan gelombang (m/s): "))
                    panjang_gelombang = float(input("Masukkan panjang gelombang (meter): "))

                    # Menghitung frekuensi
                    frekuensi = hitung_frekuensi(kecepatan, panjang_gelombang)

                    # Menampilkan hasil
                    print("Frekuensi gelombang adalah:", frekuensi, "Hertz (Hz)")

                elif pilihan_fisika == 2: 
                    massa = float(input("Masukkan massa benda (kilogram): "))
                    delta_kecepatan = float(input("Masukkan perubahan kecepatan (meter per detik): "))

                    # Menghitung impuls
                    impuls = hitung_impuls(massa, delta_kecepatan)

                    # Menampilkan hasil
                    print("Impuls : ", impuls, "kilogram meter per detik (kg·m/s)")
                elif pilihan_fisika == 3: 
                    massa = float(input("Masukkan massa (kg): "))
                    volume = float(input("Masukkan volume (m^3): "))

                    # Menghitung massa jenis
                    hasil_massa_jenis = hitung_massa_jenis(massa, volume)

                    # Menampilkan hasil
                    print(f"Massa Jenis (kg/m^3) : {hasil_massa_jenis:.2f}")
                elif pilihan_fisika == 4:
                    massa = float(input("Masukkan massa (kg): "))
                    percepatan = float(input("Masukkan percepatan (m/s^2): "))

                    # Menghitung gaya
                    hasil_gaya = hitung_gaya(massa, percepatan)

                    # Menampilkan hasil
                    print(f"Gaya (N): {hasil_gaya:.2f}")
                elif pilihan_fisika == 5:
                    kecepatan = float(input("Masukkan kecepatan gelombang (m/s): "))
                    frekuensi = float(input("Masukkan frekuensi gelombang (Hz): "))

                    # Menghitung panjang gelombang
                    panjang_gelombang = hitung_panjang_gelombang(kecepatan, frekuensi)

                    # Menampilkan hasil
                    print("Panjang Gelombang : ", panjang_gelombang, "meter (m)")
                elif pilihan_fisika == 6:
                    daya = float(input("Masukkan daya sumber cahaya (Watt): "))
                    luas_permukaan = float(input("Masukkan luas permukaan yang menerima cahaya (m^2): "))

                    # Menghitung intensitas cahaya
                    intensitas_cahaya = hitung_intensitas_cahaya(daya, luas_permukaan)

                    # Menampilkan hasil
                    print("Intensitas Cahaya : ", intensitas_cahaya, "Watt/m^2")
                elif pilihan_fisika == 7:
                    break
                else:
                    print("Menu yang kamu pilih tidak valid, pilih angka 1-7")

        elif pilihan_menu == 3:
            print("Terima kasih sudah menggunakan program ini :)\n")
            break
        else:
            print("Pilihan menu tidak valid, pilih 1/2/3")

menu_utama()