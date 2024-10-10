import datetime

mahasiswa1 = {
    "nama" : "Adelwis Laos Shinta",
    "nim" : "411221125",
    "sks_lulus" : 145,
    "beasiswa" : False,
    "lahir" : datetime.datetime(2004,1,7)
}
print(mahasiswa1)
mahasiswa2 = {
    "nama" : "Louis Pitong",
    "nim" : "411221122",
    "sks_lulus" : 145,
    "beasiswa" : True,
    "lahir" : datetime.datetime(2002,9,27)
}
print(mahasiswa2)

data_mhs = {
    "MHS001" : mahasiswa1,
    "MHS002" : mahasiswa2,
}

print(f"{'KEY':<6} {'Nama':<24} {'SKS':<8} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*60)

for mahasiswa in data_mhs:
    KEY = mahasiswa

    NAMA = data_mhs[KEY]['nama']
    NIM = data_mhs[KEY]['nim']
    SKS = data_mhs[KEY]['sks_lulus']
    BEASISWA = data_mhs[KEY]['beasiswa']
    LAHIR = data_mhs[KEY]['lahir'].strftime('%x')

    print(f"{KEY:<6} {NAMA:<24} {SKS:<8} {BEASISWA:<9} {LAHIR:<10}")
    print("-"*60)