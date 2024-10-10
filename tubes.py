class Lapangan:
    def __init__(self, nomor, kapasitas):
        self.nomor = nomor
        self.kapasitas = kapasitas
        self.status = "tersedia"
        self.pemesan = None

    def pesan(self, pemesan):
        self.status = "dipesan" 
        self.pemesan = pemesan

    def batal(self):
        self.status = "tersedia"
        self.pemesan = None

    def __str__(self):
        return f"Lapangan {self.nomor} - {self.status}"


class SistemBooking:
    def __init__(self):
        self.lapangan = []

    def tambah_lapangan(self, nomor, kapasitas):
        lap = Lapangan(nomor, kapasitas)
        self.lapangan.append(lap)

    def cek_lapangan(self):
        for lap in self.lapangan:
            print(lap)

    def pesan_lapangan(self, nomor, pemesan):
        for lap in self.lapangan:
            if lap.nomor == nomor:
                if lap.status == "tersedia":
                    lap.pesan(pemesan)
                    print(f"Lapangan {nomor} berhasil dipesan oleh {pemesan}.")
                else:
                    print(f"Lapangan {nomor} sedang tidak tersedia.")
                return
        print(f"Lapangan {nomor} tidak ditemukan.")

    def batal_pesan(self, nomor):
        for lap in self.lapangan:
            if lap.nomor == nomor:
                if lap.status == "dipesan":
                    pemesan = lap.pemesan
                    lap.batal()
                    print(f"Pemesanan lapangan {nomor} oleh {pemesan} berhasil dibatalkan.")
                else:
                    print(f"Lapangan {nomor} tidak dalam status pemesanan.")
                return
        print(f"Lapangan {nomor} tidak ditemukan.")


# Inisialisasi sistem booking
sistem_booking = SistemBooking()

# Menambahkan lapangan
sistem_booking.tambah_lapangan(1, 4)
sistem_booking.tambah_lapangan(2, 2)
sistem_booking.tambah_lapangan(3, 1)

while True:
    print("=== Sistem Booking Lapangan Badminton ===")
    print("1. Cek Lapangan")
    print("2. Pesan Lapangan")
    print("3. Batal Pesan Lapangan")
    print("0. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        print("Status Lapangan:")
        sistem_booking.cek_lapangan()
    elif pilihan == "2":
        nomor_lapangan = int(input("Masukkan nomor lapangan: "))
        pemesan = input("Masukkan nama pemesan: ")
        sistem_booking.pesan_lapangan(nomor_lapangan, pemesan)
    elif pilihan == "3":
        nomor_lapangan = int(input("Masukkan nomor lapangan: "))
        sistem_booking.batal_pesan(nomor_lapangan)
    elif pilihan == "0":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
    print()

print("Terima kasih telah menggunakan sistem booking lapangan badminton.")
