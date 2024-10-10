print("LIST PENERBANGAN")
print("Kode Penerbangan    |Tujuan    |Harga Tiket    ")
print("===============================================")
print("A01                 |AUS       |Rp. 5.800.000  ")
print("B02                 |US        |Rp. 7.800.000  ")
print("C03                 |JPN       |Rp. 7.500.000  ")
print("D04                 |MLY       |Rp. 1.000.000  ")
print("===============================================")

print("")
nama = input("Nama Pembeli : ")
no_hp = input("No HP : ")
asal = input("Asal Kota : ")
jurusan = input("Kode Tujuan : ")
tujuan = []
harga = []

if jurusan == "A01":
    tujuan.append("AUSTRALIA")
    harga = 5800000
elif jurusan == "B02":
    tujuan.append("AMERIKA")
    harga = 7800000
elif jurusan == "C03":
    tujuan.append("JEPANG")
    harga = 7500000
elif jurusan == "D04":
    tujuan.append("MALAYSIA")
    harga = 1000000
else:
    tujuan.append("KODE TIDAK DITEMUKAN")

jumlah = int(input("Jumlah Pembelian : "))
print()
if jumlah == 2:
    potongan = int(jumlah*harga)*0.1
elif jumlah == 3:
    potongan = int(jumlah*harga)*0.2
elif jumlah == 4:
    potongan = int(jumlah*harga)*0.5
else:
    potongan = 0

total = int(jumlah*harga)-potongan
pajak_total = 0.05
jumlah_bayar = (total*pajak_total)+total

def garis():
    print("===================================")
garis()
print("PEMBELIAN TIKET")
garis()
print("Nama Pembeli : ",nama)
print("No Handphone : ",no_hp)
print("Asal Negara : ",asal)
print("Kode Negara : ",jurusan)
print("Negara Tujuan : ",tujuan)
print("Jumlah Beli : ",jumlah)
garis()
print("Harga Tiket : ",harga)
print("Potongan : ",potongan)
print("PPN % : ",pajak_total)
garis()
print("Pelunasan Pembayaran Tiket")
print("Jumlah Bayar : ", jumlah_bayar)
