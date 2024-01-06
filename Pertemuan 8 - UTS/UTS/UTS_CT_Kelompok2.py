import math


# -----FUNGSI RUMUS MATEMATIKA-----
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


# Fungsi menghitung volume limas segi lima
def volume_limas_segi_lima(sisi, tinggi):
    luas_alas = luas_alas_prisma_segi_lima(sisi)
    return round(luas_alas * tinggi / 3, 1)
# Fungsi menghitung luas permukaan limas segi lima
def luas_permukaan_limas_segi_lima(sisi, tinggi):
    luas_alas = luas_alas_prisma_segi_lima(sisi)
    return round(luas_alas + (5 * sisi * tinggi) / 2, 1)


# Fungsi untuk menghitung volume, luas permukaan, dan keliling prisma segitiga
def prisma_segitiga(keliling_alas, tinggi):
    # Keliling alas
    K = keliling_alas
    # Volume
    V = (1/2) * K * tinggi
    # Luas permukaan
    L = K * tinggi + 2 * keliling_alas
    return K, V, L


# Fungsi menghitung volume prisma segi empat
def volume_prisma_segi_empat(panjang, lebar, tinggi):
    return panjang * lebar * tinggi
# Fungsi menghitung luas permukaan prisma segi empat
def luas_permukaan_prisma_segi_empat(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
# Fungsi menghitung keliling prisma segi empat
def keliling_prisma_segi_empat(panjang, lebar, tinggi):
    return 2 * (panjang + lebar) + 4 * tinggi


# Fungsi menghitung luas alas prisma segi lima
def luas_alas_prisma_segi_lima(sisi):
    return 5 * sisi ** 2 / (4 * math.tan(math.pi / 5))
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


# Fungsi untuk menghitung volume kerucut
def volume_kerucut(jari_jari, tinggi):
    volume = (1/3) * math.pi * (jari_jari ** 2) * tinggi
    return volume
# Fungsi untuk menghitung luas permukaan kerucut
def luas_permukaan_kerucut(jari_jari, sisi_miring):
    return math.pi * jari_jari * (jari_jari + sisi_miring)


# Fungsi untuk menghitung keliling, volume, dan luas permukaan balok
def balok(panjang, lebar, tinggi):
    # Keliling alas
    K = 2 * (panjang + lebar)
    # Volume
    V = panjang * lebar * tinggi
    # Luas permukaan
    L = 2 * (panjang*lebar + panjang*tinggi + lebar*tinggi)
    return K, V, L


# Fungsi untuk menghitung keliling, volume, dan luas permukaan bola
def bola(jari_jari):
    # Keliling
    C = 2 * math.pi * jari_jari
    # Volume
    V = (4/3) * math.pi * jari_jari**3
    # Luas permukaan
    A = 4 * math.pi * jari_jari**2
    return C, V, A



# -----FUNGSI RUMUS FISIKA-----
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


# Fungsi untuk menghitung percepatan
def hitung_percepatan(kecepatan_awal, kecepatan_akhir, waktu):
    percepatan = (kecepatan_akhir - kecepatan_awal) / waktu
    return percepatan



# Fungsi untuk menampilkan menu matematika
def menu_mtk():
    print("\n==========MENU MATEMATIKA==========")
    print("1. Rumus Limas Segitiga")
    print("2. Rumus Limas Segi Empat")
    print("3. Rumus Limas Segi Lima")
    print("4. Rumus Prisma Segitiga")
    print("5. Rumus Prisma Segi Empat")
    print("6. Rumus Prisma Segi Lima")
    print("7. Rumus Balok")
    print("8. Rumus Bola")
    print("9. Rumus Kerucut")
    print("10. Menu utama")

# Fungsi untuk menampilkan menu fisika
def menu_fisika():
    print("\n============MENU FISIKA============")
    print("1. Rumus Frekuensi")
    print("2. Rumus Impuls")
    print("3. Rumus Massa Jenis")
    print("4. Rumus Gaya")
    print("5. Rumus Panjang Gelombang")
    print("6. Rumus Intensitas Cahaya")
    print("7. Rumus Percepatan")
    print("8. Menu utama")

# Fungsi untuk menampilkan menu utama
def menu_utama():
    while True:
        print("\n============MENU UTAMA============")
        print("1. Tampilkan Rumus Matematika")
        print("2. Tampilkan Rumus Fisika")
        print("3. Keluar")

        pilihan_menu = int(input("Pilih untuk memilih menu (1/2/3): "))

        if pilihan_menu == 1:
            while True:
                menu_mtk()
                pilihan_matematika = int(input("\nPilih perintah operasi matematika (1-9): "))

                # Pilihan rumus matematika
                match pilihan_matematika:
                    case 1:
                        # Input variabel limas segitiga
                        print("\n=== INPUT PENGHITUNGAN LIMAS SEGITIGA ===")
                        alas_limas_segitiga = float(input("Masukkan panjang sisi alas limas segitiga: "))
                        tinggi_limas_segitiga = float(input("Masukkan tinggi limas segitiga: "))
                        sisi_miring_limas_segitiga = float(input("Masukkan panjang sisi miring limas segitiga: "))

                        # Menghitung volume, luas permukaan, dan keliling limas segitiga
                        hasil_volume = volume_limas_segitiga(alas_limas_segitiga, tinggi_limas_segitiga)
                        hasil_luas_permukaan = luas_permukaan_limas_segitiga(alas_limas_segitiga, tinggi_limas_segitiga, sisi_miring_limas_segitiga)
                        hasil_keliling = keliling_limas_segitiga(alas_limas_segitiga, sisi_miring_limas_segitiga)

                        # Menampilkan hasil
                        print("\n=== HASIL PERHITUNGAN RUMUS LIMAS SEGITIGA ===")
                        print(f"Volume: {hasil_volume:.1f}")
                        print(f"Luas Permukaan: {hasil_luas_permukaan:.1f}")
                        print(f"Keliling: {hasil_keliling:.1f}")
                    case 2:
                        # Input variabel limas segi empat
                        print("\n=== INPUT PENGHITUNGAN LIMAS SEGI EMPAT ===")
                        alas_limas_segi_empat = float(input("Masukkan panjang sisi alas limas segi empat: "))
                        tinggi_limas_segi_empat = float(input("Masukkan tinggi limas segi empat: "))
                        sisi_miring_limas_segi_empat = float(input("Masukkan panjang sisi miring limas segi empat: "))

                        # Menghitung volume, luas permukaan, dan keliling limas segi empat
                        hasil_volume = volume_limas_segi_empat(alas_limas_segi_empat, tinggi_limas_segi_empat)
                        hasil_luas_permukaan = luas_permukaan_limas_segi_empat(alas_limas_segi_empat, tinggi_limas_segi_empat, sisi_miring_limas_segi_empat)
                        hasil_keliling = keliling_limas_segi_empat(alas_limas_segi_empat)

                        # Menampilkan hasil
                        print("\n=== HASIL PERHITUNGAN RUMUS LIMAS SEGI EMPAT ===")
                        print(f"Volume: {hasil_volume:.1f}")
                        print(f"Luas Permukaan: {hasil_luas_permukaan:.1f}")
                        print(f"Keliling: {hasil_keliling:.1f}")
                    case 3:
                        # Input variabel limas segi lima
                        print("\n=== INPUT PENGHITUNGAN LIMAS SEGI LIMA ===")
                        sisi_limas_lima = float(input("Masukkan panjang sisi limas segi lima: "))
                        tinggi_limas_lima = float(input("Masukkan tinggi limas segi lima: "))

                        # Menghitung volume, luas permukaan, dan keliling limas segi lima
                        volume_lsl = volume_limas_segi_lima(sisi_limas_lima, tinggi_limas_lima)
                        luas_permukaan_lsl = luas_permukaan_limas_segi_lima(sisi_limas_lima, tinggi_limas_lima)

                        # Menampilkan hasil
                        print("\n==== HASIL PERHITUNGAN RUMUS LIMAS SEGI LIMA ===")
                        print(f"Volume: {volume_lsl}")
                        print(f"Luas Permukaan: {luas_permukaan_lsl}")
                    case 4:
                        # Input variabel prisma segitiga
                        print("\n=== INPUT PENGHITUNGAN PRISMA SEGITIGA ===")
                        keliling_alas_prisma = float(input("Masukkan keliling alas segitiga: "))
                        tinggi_prisma = float(input("Masukkan tinggi prisma: "))

                        # Menghitung volume, luas permukaan, dan keliling prisma segitiga
                        hasil_keliling, hasil_volume, hasil_luas = prisma_segitiga(keliling_alas_prisma, tinggi_prisma)

                        # Menampilkan hasil
                        print("\n=== HASIL PERHITUNGAN RUMUS PRISMA SEGITIGA ===")
                        print(f"Volume: {hasil_volume}")
                        print(f"Luas Permukaan: {hasil_luas}")
                        print(f"Keliling: {hasil_keliling}")
                    case 5:
                        # Input variabel prisma segi empat
                        print("=== INPUT PENGHITUNGAN PRISMA SEGI EMPAT ===")
                        panjang = float(input("Masukkan panjang prisma segi empat: "))
                        lebar = float(input("Masukkan lebar prisma segi empat: "))
                        tinggi_prisma_empat = float(input("Masukkan tinggi prisma segi empat: "))

                        # Menghitung volume, luas permukaan, dan keliling prisma segi empat
                        volume_pse = volume_prisma_segi_empat(panjang, lebar, tinggi_prisma_empat)
                        luas_permukaan_pse = luas_permukaan_prisma_segi_empat(panjang, lebar, tinggi_prisma_empat)
                        keliling_pse = keliling_prisma_segi_empat(panjang, lebar, tinggi_prisma_empat)

                        # Menampilkan hasil
                        print("\n==== HASIL PERHITUNGAN RUMUS PRISMA SEGI EMPAT ===")
                        print(f"Volume: {volume_pse}")
                        print(f"Luas Permukaan: {luas_permukaan_pse}")
                        print(f"Keliling: {keliling_pse}")
                    case 6:
                        # Input variabel prisma segi lima
                        print("\n=== INPUT PENGHITUNGAN PRISMA SEGI LIMA ===")
                        sisi_prisma_lima = float(input("Masukkan panjang sisi prisma segi lima: "))
                        tinggi_prisma_lima = float(input("Masukkan tinggi prisma segi lima: "))

                        # Menghitung volume, luas permukaan, dan keliling prisma segi lima
                        volume_psl = volume_prisma_segi_lima(sisi_prisma_lima, tinggi_prisma_lima)
                        luas_permukaan_psl = luas_permukaan_prisma_segi_lima(sisi_prisma_lima, tinggi_prisma_lima)
                        keliling_psl = keliling_prisma_segi_lima(sisi_prisma_lima)

                        # Menampilkan hasil
                        print("\n==== HASIL PERHITUNGAN RUMUS PRISMA SEGI LIMA ===")
                        print(f"Volume: {volume_psl}")
                        print(f"Luas Permukaan: {luas_permukaan_psl}")
                        print(f"Keliling: {keliling_psl}")
                    case 7:
                        # Input variabel Balok
                        print("\n=== INPUT PENGHITUNGAN BALOK ===")
                        panjang_balok = float(input("Masukkan panjang balok: "))
                        lebar_balok = float(input("Masukkan lebar balok: "))
                        tinggi_balok = float(input("Masukkan tinggi balok: "))

                        # Menghitung volume, luas permukaan, dan keliling balok
                        hasil_keliling, hasil_volume, hasil_luas = balok(panjang_balok, lebar_balok, tinggi_balok)

                        # Menampilkan hasil
                        print("\n=== HASIL PERHITUNGAN RUMUS BALOK ===")
                        print(f"Volume: {hasil_volume}")
                        print(f"Luas Permukaan: {hasil_luas}")
                        print(f"Keliling: {hasil_keliling}")
                    case 8:
                        # Input variabel Bola
                        print("\n=== INPUT PENGHITUNGAN BOLA ===")
                        jari_jari_bola = float(input("Masukkan jari-jari bola: "))

                        # Menghitung keliling, volume, dan luas permukaan bola
                        hasil_keliling, hasil_volume, hasil_luas = bola(jari_jari_bola)

                        # Menampilkan hasil
                        print("\n=== HASIL PERHITUNGAN RUMUS BOLA ===")
                        print(f"Volume Bola: {hasil_volume:.1f}")
                        print(f"Luas Permukaan Bola: {hasil_luas:.1f}")
                        print(f"Keliling Bola: {hasil_keliling:.1f}")
                    case 9:
                        # Input variabel kerucut
                        print("\n=== INPUT PENGHITUNGAN KERUCUT ===")
                        jari_jari_kerucut = float(input("Masukkan jari-jari kerucut: "))
                        tinggi_kerucut = float(input("Masukkan tinggi kerucut: "))

                        # Menghitung volume dan luas permukaan kerucut
                        volume = volume_kerucut(jari_jari_kerucut, tinggi_kerucut)
                        sisi_miring_kerucut = math.sqrt(jari_jari_kerucut ** 2 + tinggi_kerucut ** 2)
                        luas_permukaan = luas_permukaan_kerucut(jari_jari_kerucut, sisi_miring_kerucut)

                        # Menampilkan hasil untuk kerucut
                        print("\n=== HASIL PERHITUNGAN RUMUS KERUCUT ===")
                        print(f"Volume Kerucut: {volume:.1f}")
                        print(f"Luas Permukaan Kerucut: {luas_permukaan:.1f}")
                    case 10:
                        break
                    case _:
                        print("\nMenu yang kamu pilih tidak valid, pilih angka 1-10.")

        elif pilihan_menu == 2:
            while True:
                menu_fisika()
                pilihan_fisika = int(input("\nPilih perintah operasi fisika (1-7): "))

                # Pilihan rumus fisika
                match pilihan_fisika:
                    case 1:
                        # Input variabel frekuensi
                        print("\n=== INPUT PENGHITUNGAN FREKUENSI ===")
                        kecepatan = float(input("Masukkan kecepatan gelombang (m/s): "))
                        panjang_gelombang = float(input("Masukkan panjang gelombang (meter): "))

                        # Menghitung frekuensi
                        frekuensi = hitung_frekuensi(kecepatan, panjang_gelombang)

                        # Menampilkan hasil untuk frekuensi
                        print("\n=== HASIL PERHITUNGAN RUMUS FREKUENSI ===")
                        print("Frekuensi gelombang: ", frekuensi, "Hertz (Hz)")
                    case 2:
                        # Input variabel impuls
                        print("\n=== INPUT PENGHITUNGAN IMPULS ===")
                        massa = float(input("Masukkan massa benda (kilogram): "))
                        delta_kecepatan = float(input("Masukkan perubahan kecepatan (meter per detik): "))

                        # Menghitung impuls
                        impuls = hitung_impuls(massa, delta_kecepatan)

                        # Menampilkan hasil untuk impuls
                        print("\n=== HASIL PERHITUNGAN RUMUS IMPULS ===")
                        print("Impuls: ", impuls, "kilogram meter per detik (kg·m/s)")
                    case 3:
                        # Input variabel massa jenis
                        print("\n=== INPUT PENGHITUNGAN MASSA JENIS ===")
                        massa = float(input("Masukkan massa (kg): "))
                        volume = float(input("Masukkan volume (m^3): "))

                        # Menghitung massa jenis
                        hasil_massa_jenis = hitung_massa_jenis(massa, volume)

                        # Menampilkan hasil untuk massa jenis
                        print("\n=== HASIL PERHITUNGAN RUMUS MASSA JENIS ===")
                        print(f"Massa Jenis (kg/m^3): {hasil_massa_jenis:.2f}")
                    case 4:
                        # Input variabel gaya
                        print("\n=== INPUT PENGHITUNGAN GAYA ===")
                        massa = float(input("Masukkan massa (kg): "))
                        percepatan = float(input("Masukkan percepatan (m/s^2): "))

                        # Menghitung gaya
                        hasil_gaya = hitung_gaya(massa, percepatan)

                        # Menampilkan hasil untuk gaya
                        print("\n=== HASIL PERHITUNGAN RUMUS GAYA ===")
                        print(f"Gaya (N): {hasil_gaya:.2f}")
                    case 5:
                        # Input perhitungan panjang gelombang
                        print("\n=== INPUT PENGHITUNGAN PANJANG GELOMBANG ===")
                        kecepatan = float(input("Masukkan kecepatan gelombang (m/s): "))
                        frekuensi = float(input("Masukkan frekuensi gelombang (Hz): "))

                        # Menghitung panjang gelombang
                        panjang_gelombang = hitung_panjang_gelombang(kecepatan, frekuensi)

                        # Menampilkan hasil untuk panjang gelombang
                        print("\n=== HASIL PERHITUNGAN RUMUS PANJANG GELOMBANG ===")
                        print("Panjang Gelombang: ", panjang_gelombang, "meter (m)")
                    case 6:
                        # Input perhitungan intensitas cahaya
                        print("\n=== INPUT PENGHITUNGAN INTENSITAS CAHAYA ===")
                        daya = float(input("Masukkan daya sumber cahaya (Watt): "))
                        luas_permukaan = float(input("Masukkan luas permukaan yang menerima cahaya (m^2): "))

                        # Menghitung intensitas cahaya
                        intensitas_cahaya = hitung_intensitas_cahaya(daya, luas_permukaan)

                        # Menampilkan hasil untuk intensitas cahaya
                        print("\n=== HASIL PERHITUNGAN RUMUS INTENSITAS CAHAYA ===")
                        print("Intensitas Cahaya: ", intensitas_cahaya, "Watt/m^2")
                    case 7:
                        # Input perhitungan percepatan
                        print("\n=== INPUT PENGHITUNGAN PERCEPATAN ===")
                        kecepatan_awal = float(input("Masukkan kecepatan awal (meter per detik): "))
                        kecepatan_akhir = float(input("Masukkan kecepatan akhir (meter per detik): "))
                        waktu = float(input("Masukkan waktu (detik): "))

                        # Menghitung percepatan
                        hasil_percepatan = hitung_percepatan(kecepatan_awal, kecepatan_akhir, waktu)

                        # Menampilkan hasil untuk percepatan
                        print("\n=== HASIL PERHITUNGAN RUMUS PERCEPATAN ===")
                        print("Percepatan: ", hasil_percepatan, "meter per detik kuadrat (m/s^2)")
                    case 8:
                        break
                    case _:
                        print("\nMenu yang kamu pilih tidak valid, pilih angka 1-8.")
        
        elif pilihan_menu == 3:
            print("\nTerima kasih sudah menggunakan program ini :)\n")
            break

        else:
            print("\nPilihan menu tidak valid, pilih 1/2/3.")
menu_utama()