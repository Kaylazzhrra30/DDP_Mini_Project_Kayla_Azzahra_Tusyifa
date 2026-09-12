data_tiket = []

daftar_film = [
    ("F01", "Hope", 50000),
    ("F02", "Insidious Out of the further", 45000),
    ("F03", "Operasi Pesta Copet", 40000),
    ("F04", "Runner", 45000)
]

while True:

    print("\n PEMBELIAN TIKET BIOSKOP")
    print("1. Tambah Tiket")
    print("2. Lihat Data Pembelian")
    print("3. Ubah Data Tiket")
    print("4. Hapus Data Tiket")
    print("5. Lihat Daftar Film")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ").strip()

    if pilihan == "1":

        print("\nPEMBELIAN TIKET")

        while True:
            nama = input("Masukkan nama pembeli: ").strip()

            if nama == "":
                print("Nama tidak boleh kosong!")
            else:
                break

        print("\nDAFTAR FILM")

        for film in daftar_film:
            print(f"ID     : {film[0]}")
            print(f"Film   : {film[1]}")
            print(f"Harga  : Rp{film[2]:,.0f}")
            print("------------------------")

        while True:
            id_film = input("Masukkan ID film: ").upper().strip()

            film = None

            for data in daftar_film:
                if data[0] == id_film:
                    film = data
                    break

            if film is None:
                print("ID film tidak ditemukan!")
            else:
                break

        while True:
            kategori = input(
                "Kategori tiket (REGULER/VIP): "
            ).upper().strip()

            if kategori == "REGULER":
                harga_tiket = film[2]
                break

            elif kategori == "VIP":
                harga_tiket = film[2] + 20000
                break

            else:
                print("Kategori hanya REGULER atau VIP!")

        while True:
            try:
                jumlah = int(input("Jumlah tiket: "))

                if jumlah <= 0:
                    print("Jumlah tiket harus lebih dari 0!")
                else:
                    break

            except ValueError:
                print("Input harus berupa angka!")

        total_harga = harga_tiket * jumlah

        id_transaksi = len(data_tiket) + 1

        tiket = (
            id_transaksi,
            nama,
            film[1],
            kategori,
            jumlah,
            total_harga
        )

        data_tiket.append(tiket)

        print("\nTiket berhasil ditambahkan!")
        print(f"ID Transaksi : {id_transaksi}")
        print(f"Nama         : {nama}")
        print(f"Film         : {film[1]}")
        print(f"Kategori     : {kategori}")
        print(f"Jumlah       : {jumlah}")
        print(f"Total Harga  : Rp{total_harga:,.0f}")

    elif pilihan == "2":

        print("\nDATA PEMBELIAN")

        if len(data_tiket) == 0:
            print("Belum ada data pembelian tiket.")

        else:
            for tiket in data_tiket:
                print(f"ID Transaksi : {tiket[0]}")
                print(f"Nama         : {tiket[1]}")
                print(f"Film         : {tiket[2]}")
                print(f"Kategori     : {tiket[3]}")
                print(f"Jumlah       : {tiket[4]}")
                print(f"Total Harga  : Rp{tiket[5]:,.0f}")

    elif pilihan == "3":

        print("\nUBAH DATA TIKET")

        if len(data_tiket) == 0:
            print("Belum ada data pembelian.")

        else:

            for tiket in data_tiket:
                print(f"ID Transaksi : {tiket[0]}")
                print(f"Nama         : {tiket[1]}")
                print(f"Film         : {tiket[2]}")
                print(f"Kategori     : {tiket[3]}")
                print(f"Jumlah       : {tiket[4]}")

            while True:
                try:
                    id_transaksi = int(
                        input("Masukkan ID transaksi yang ingin diubah: ")
                    )

                    if id_transaksi <= 0:
                        print("ID harus lebih dari 0!")
                    else:
                        break

                except ValueError:
                    print("ID harus berupa angka!")

            index = -1

            for i in range(len(data_tiket)):
                if data_tiket[i][0] == id_transaksi:
                    index = i
                    break

            if index == -1:
                print("Data transaksi tidak ditemukan!")

            else:

                tiket_lama = data_tiket[index]

                print("\nData yang akan diubah:")
                print(f"Nama     : {tiket_lama[1]}")
                print(f"Film     : {tiket_lama[2]}")
                print(f"Kategori : {tiket_lama[3]}")
                print(f"Jumlah   : {tiket_lama[4]}")

                while True:
                    nama = input("Nama pembeli baru: ").strip()

                    if nama == "":
                        print("Nama tidak boleh kosong!")
                    else:
                        break

                print("\nDAFTAR FILM")

                for film in daftar_film:
                    print(f"ID     : {film[0]}")
                    print(f"Film   : {film[1]}")
                    print(f"Harga  : Rp{film[2]:,.0f}")
                    print("------------------------")

                while True:
                    id_film = input(
                        "Masukkan ID film baru: "
                    ).upper().strip()

                    film = None

                    for data in daftar_film:
                        if data[0] == id_film:
                            film = data
                            break

                    if film is None:
                        print("ID film tidak ditemukan!")
                    else:
                        break

                while True:
                    kategori = input(
                        "Kategori baru (REGULER/VIP): "
                    ).upper().strip()

                    if kategori == "REGULER":
                        harga_tiket = film[2]
                        break

                    elif kategori == "VIP":
                        harga_tiket = film[2] + 20000
                        break

                    else:
                        print("Kategori hanya REGULER atau VIP!")

                while True:
                    try:
                        jumlah = int(input("Jumlah tiket baru: "))

                        if jumlah <= 0:
                            print("Jumlah tiket harus lebih dari 0!")
                        else:
                            break

                    except ValueError:
                        print("Input harus berupa angka!")

                total_harga = harga_tiket * jumlah

                tiket_baru = (
                    id_transaksi,
                    nama,
                    film[1],
                    kategori,
                    jumlah,
                    total_harga
                )

                data_tiket[index] = tiket_baru

                print("\nData tiket berhasil diubah!")
                print(f"Total harga baru: Rp{total_harga:,.0f}")

    elif pilihan == "4":

        print("\nHAPUS DATA TIKET")

        if len(data_tiket) == 0:
            print("Belum ada data pembelian.")

        else:

            for tiket in data_tiket:
                print(f"ID Transaksi : {tiket[0]}")
                print(f"Nama         : {tiket[1]}")
                print(f"Film         : {tiket[2]}")
                print(f"Kategori     : {tiket[3]}")
                print(f"Jumlah       : {tiket[4]}")

            while True:
                try:
                    id_transaksi = int(
                        input("Masukkan ID transaksi yang ingin dihapus: ")
                    )

                    if id_transaksi <= 0:
                        print("ID harus lebih dari 0!")
                    else:
                        break

                except ValueError:
                    print("ID harus berupa angka!")

            index = -1

            for i in range(len(data_tiket)):
                if data_tiket[i][0] == id_transaksi:
                    index = i
                    break

            if index == -1:
                print("Data transaksi tidak ditemukan!")

            else:

                tiket = data_tiket[index]

                print("\nData yang akan dihapus:")
                print(f"Nama : {tiket[1]}")
                print(f"Film : {tiket[2]}")

                while True:
                    konfirmasi = input(
                        "Yakin ingin menghapus? (Y/T): "
                    ).upper().strip()

                    if konfirmasi == "Y":
                        data_tiket.pop(index)
                        print("Data tiket berhasil dihapus!")
                        break

                    elif konfirmasi == "T":
                        print("Penghapusan dibatalkan.")
                        break

                    else:
                        print("Masukkan hanya Y atau T!")


    elif pilihan == "5":

        print("\nDAFTAR FILM")

        for film in daftar_film:
            print(f"ID     : {film[0]}")
            print(f"Film   : {film[1]}")
            print(f"Harga  : Rp{film[2]:,.0f}")
            print("------------------------")

    elif pilihan == "6":

        print("\nTerima kasih, selamat menonton!.")
        break

    else:

        print("Pilihan menu tidak valid! Silakan pilih 1-6.")