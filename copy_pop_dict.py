matkul = {
    "AP2":"Algoritma dan Pemrograman",
    "KSI":"Keamanan Sistem Informasi",
    "STD":"Struktur Data dan Algoritma"
}

mk = matkul.copy()
print (f"Mata Kuliah : {matkul}\n")
print (f"Matkul : {mk}\n")

matkul["AP2"] = "Algoritma dan Pemrograman 2"
print (f"Mata Kuliah : {matkul}\n")
print (f"Matkul : {mk}\n")

#pop dict
data_mk = mk.pop("AP2")
print (f"Data Matkul : {data_mk}\n")
print (f"Matakuliah : {mk}\n")

#pop item dictionary
dataTerakhir = mk.popitem()
print(f"Data Terakhir : {dataTerakhir}\n")
print(f"Matakuliah : {mk}\n")