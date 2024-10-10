print("\tTUGAS ALGORITMA DAN PEMROGRAMAN 2 PERTEMUAN KE-6")
print("----------------------------------------------------------------")
print()

list_buku = []
while True:
    print("INPUTKAN DATA BUKU")
    judul = input("Masukan Judul Buku\t : ")
    penulis = input("Masukan Nama Penulis\t : ")
    harga = int(input("Masukan Harga Buku\t : "))

    buku_baru = [judul, penulis, harga]
    list_buku.append(buku_baru)
    lanjut = input("Apakah ada tambahan buku? [Y/T]")
    print()
    if lanjut.lower() == "t":
        break
print("--------------------------------------------------")
print("\t\tData Buku")
print("--------------------------------------------------")
print()
for data in list_buku:
    print("- Judul Buku   :", data[0])
    print("- Nama Penulis :", data[1])
    print("- Harga Buku   :", data[2])
    print()
print("--------------------------------------------------")
print("\t\tTransaksi Pembelian Buku")
print("--------------------------------------------------")
total_bayar = 0
while True:
    beli = input("\nMasukan judul buku yang dibeli (ketik 'selesai' jika ingin menyelesaikan transaksi)  : ")
    if beli.lower() == "selesai":
        break
    for data in list_buku:
        if beli.lower() == data[0].lower():
            jumlah_buku_dibeli = int(input("Masukan jumlah buku yang dibeli : "))
            total_harga = int(data[2] * jumlah_buku_dibeli)
            total_bayar += int(total_harga)
            print("Total harga                     :", total_harga)
            break
print("Total bayar                     :", total_bayar)
cek_bayar = True
while cek_bayar == True:
    jumlah_uang = int(input("Masukan jumlah uang             : "))
    if jumlah_uang < total_bayar:
        print("Uang Bayar Kurang!!")
    else:
        cek_bayar = False        
kembalian = jumlah_uang - total_bayar    
print("Uang kembali anda                 : ", kembalian)