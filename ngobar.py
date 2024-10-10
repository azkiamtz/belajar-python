print("         Ayam Goreng Mantul          ")
print("=====================================")
print("     Kode   Jenis Potong    Harga    ")
print("      D          Dada       12000    ")
print("      P          Paha       10000    ")
print("      S          Sayap      11000    ")
print("=====================================")
banyak_jenis = int(input("Banyak Jenis Ayam : "))
kode_potong = []
banyak_potong = []
jenis_potong = []
jumlah = []
harga = []
i=0

while i < banyak_jenis:
    print("Jenis Ke-",i+1)

    kode_potong.append(input("Kode Potong D/P/S : "))
    banyak_potong.append(int(input("Banyak Potong : ")))
    if kode_potong[i] == "D" or kode_potong[i] == "d":
        jenis_potong.append("Dada")
        harga.append(12000)
        jumlah.append(banyak_potong[i]*12000)
    elif kode_potong[i] == "P" or kode_potong[i] == "p":
        jenis_potong.append("Paha")
        harga.append(10000)
        jumlah.append(banyak_potong[i]*10000)
    elif kode_potong[i] == "S" or kode_potong[i] == "s":
        jenis_potong.append("Sayap")
        harga.append(11000)
        jumlah.append(banyak_potong[i]*11000)
    else :
        jenis_potong.append("KODE SALAH")
        harga.append(0)
        jumlah.append(banyak_potong[i]*0)
    i=i+1

print("            Ayam Goreng Mantul           ")
print("=========================================")
print("No.   Jenis    Harga   Banyak   Jumlah   ")
print("      Potong   Satuan  Beli     Harga    ")
print("=========================================")
jumlah_bayar = 0
a=0
while a < banyak_jenis:
    jumlah_bayar = jumlah_bayar+jumlah[a]
    print("%i     %s     %i     %i       %i" % (a+1, jenis_potong[a], harga[a], banyak_potong[a], jumlah[a]))
    a = a + 1

pajak = jumlah_bayar * 0.1
total_bayar = jumlah_bayar + pajak

print("                  Jumlah Bayar Rp.", jumlah_bayar)
print("                  Pajak 10%    Rp.", int(pajak))
print("                  Total Bayar  Rp.", int(total_bayar))


    