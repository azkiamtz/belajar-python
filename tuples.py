tup1 = ("fisika", "kimia", 1993, 2017)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"

#cara mengakses nilai tuple
tup1 = ("fisika", "kimia", 1993, 2017)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print ("tup1[0] : ", tup1[0])
print ("tup[1:5] : ", tup2[1:5])
tup1 = (12, 34.56)
tup2 = ("abc", "xyz")

#aksi dibawah ini tidak bisa dilakukan pada tuple python
#karena memang nilai pada tuple python tidak bisa diubah
#tup1[0] = 100;
#jadi, buatlah tuple baru sebagai berikut
tup3 = tup1 + tup2
print (tup3)
tup = ("fisika", "kimia", 1993, 2017)
print (tup)

#hapus tuple dengan statement del
del tup
#lalu buat kembali tuple yg baru dengan elemen yg diinginkan
tup = ("Bahasa", "Literasi", 2020)
print ("Setelah menghapus tuple : ", tup)