# ====================================
# APLIKASI MANAJEMEN NILAI MAHASISWA
# ====================================

data_mahasiswa = [
    ["padel", 95],
    ["amee", 100],
    ["yogi gondrong", 80]
]

while True:
    print("\n====================================")
    print(" APLIKASI MANAJEMEN NILAI MAHASISWA")
    print("====================================")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("6. Urutkan Data Berdasarkan Nilai")
    print("7. Hitung Rata-rata Nilai")
    print("8. Keluar")

    pilihan = input("\nPilih menu 1-8: ")

    # 1. Tampilkan Data
    if pilihan == "1":
        print("\nDAFTAR MAHASISWA")
        print("-" * 30)

        if len(data_mahasiswa) == 0:
            print("Data masih kosong!")
        else:
            for i in range(len(data_mahasiswa)):
                print(
                    f"{i+1}. Nama : {data_mahasiswa[i][0]} | Nilai : {data_mahasiswa[i][1]}"
                )

    # 2. Tambah Data
    elif pilihan == "2":
        nama = input("Masukkan nama mahasiswa : ")
        nilai = int(input("Masukkan nilai : "))

        data_mahasiswa.append([nama, nilai])
        print("Data berhasil ditambahkan!")

    # 3. Ubah Data
    elif pilihan == "3":
        nama_cari = input("Masukkan nama yang ingin diubah : ")

        ditemukan = False

        for data in data_mahasiswa:
            if data[0].lower() == nama_cari.lower():
                nama_baru = input("Nama baru : ")
                nilai_baru = int(input("Nilai baru : "))

                data[0] = nama_baru
                data[1] = nilai_baru

                print("Data berhasil diubah!")
                ditemukan = True
                break

        if not ditemukan:
            print("Data tidak ditemukan!")

    # 4. Hapus Data
    elif pilihan == "4":
        nama_hapus = input("Masukkan nama yang ingin dihapus : ")

        ditemukan = False

        for data in data_mahasiswa:
            if data[0].lower() == nama_hapus.lower():
                data_mahasiswa.remove(data)
                print("Data berhasil dihapus!")
                ditemukan = True
                break

        if not ditemukan:
            print("Data tidak ditemukan!")

    # 5. Cari Data
    elif pilihan == "5":
        nama_cari = input("Masukkan nama mahasiswa : ")

        ditemukan = False

        for data in data_mahasiswa:
            if data[0].lower() == nama_cari.lower():
                print("\nDATA DITEMUKAN")
                print(f"Nama  : {data[0]}")
                print(f"Nilai : {data[1]}")
                ditemukan = True
                break

        if not ditemukan:
            print("Data tidak ditemukan!")

    # 6. Urutkan Data
    elif pilihan == "6":
        data_mahasiswa.sort(key=lambda x: x[1], reverse=True)

        print("\nDATA SETELAH DIURUTKAN (NILAI TERTINGGI)")
        print("-" * 40)

        for i, data in enumerate(data_mahasiswa, start=1):
            print(f"{i}. {data[0]} - {data[1]}")

    # 7. Hitung Rata-rata
    elif pilihan == "7":
        if len(data_mahasiswa) == 0:
            print("Data masih kosong!")
        else:
            total = 0

            for data in data_mahasiswa:
                total += data[1]

            rata_rata = total / len(data_mahasiswa)

            print(f"Rata-rata nilai mahasiswa = {rata_rata:.2f}")

    # 8. Keluar
    elif pilihan == "8":
        print("Terima kasih, program selesai.")
        break

    else:
        print("Pilihan tidak valid! Silakan pilih 1-8.")
