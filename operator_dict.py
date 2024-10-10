data_dict = {
    "RF"  : "Rifda",
    "MZ"  : "Mumtaz",
    "AM"  : "Audami"
}

#panjang dict
LENDICT = len (data_dict)
print (f"Panjang Dictionary : {LENDICT}")

#cek key exist atau tidak
KEY = "RF"
CHECKKEY = KEY in data_dict
print (f"Apakah {KEY} ada di data_dict : {CHECKKEY}")

#akses value (read) dengan get
print(data_dict["RF"])
print(data_dict.get("RF"))
print(data_dict.get("IY", "Key tidak ditemukan"))

#mengupdate data
data_dict["RF"] = "Rifda adalah mahasiswa Teknik Informatika"
print(data_dict)
data_dict["BYG"] = "Dosen Algoritma dan Pemrograman 2"
print(data_dict)

data_dict.update({"RF":"Rifda adalah mahasiswa Tekknik Informatika"})
print(data_dict)
data_dict.update({"TI":"Teknik Informatika"})
print(data_dict)

#delete
del data_dict["BYG"]
print(data_dict)