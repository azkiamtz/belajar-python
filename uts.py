print("================================================================")
print("\t\t\tUJIAN TENGAH SEMESTER")
print("Nama : M Azkia Hakim")
print("================================================================")
nisn = input("Masukkan NISN : ")
nama = input("Masukkan Nama Lengkap : ")
no_hp = input("Masukkan No. Hp : ")
domsili = input("Masukkan Alamat Domisili : ")
cek_fakultas = True
while cek_fakultas == True :
    fakultas = input("Pilih Fakultas [FTI/FBIS] : ")
    if fakultas not in ["FTI","FBIS"] :
        print("Fakultas tidak tersedia!")
        cek_fakultas = True
    else :
        cek_fakultas = False
cek_prodi = True
while cek_prodi == True :
    prodi = input("Pilih Jurusan [TI/TE/TS/TM/MJ/AKT/BING/ILKOM] : ")
    if prodi not in ["TI","TE","TS","TM","MJ","AKT","BING","ILKOM"] :
        print("Jurusan tidak tersedia!")
        cek_prodi = True
    else :
        cek_prodi = False
cek_kelas = True
while cek_kelas == True :
    kelas = input("Pilih Jurusan [Reguler 1/Reguler 2] : ")
    if kelas not in ["Reguler 1","Reguler 2"] :
        print("Kelas tidak tersedia!")
        cek_kelas = True
    else :
        cek_kelas = False
print("================================================================")
print("\t\tFormulir Pendaftaran Mahasiswa")
print("================================================================")
print("NISN\t\t\t :",nisn)
print("Nama Lengkap\t\t :",nama)
print("No. Hp\t\t\t :",no_hp)
print("Alamat\t\t\t :",domsili)
if prodi == "TI" :
    biaya_kuliah = 4900000
    prodi = "Teknik Informatika"
elif prodi == "TE" :
    biaya_kuliah = 4600000
    prodi = "Teknik Elektro"
elif prodi == "TS" :
    biaya_kuliah = 4800000
    prodi = "Teknik Sipil"
elif prodi == "TM" :
    biaya_kuliah = 4700000
    prodi = "Teknik Mesin"
elif prodi == "MJ" :
    biaya_kuliah = 4200000
    prodi = "Manajemen"
elif prodi == "AKT" :
    biaya_kuliah = 4150000
    prodi = "Akutansi"
elif prodi == "BING" :
    biaya_kuliah = 4100000
    prodi = "Bahasa Inggris"
elif prodi == "ILKOM" :
    biaya_kuliah = 4250000
    prodi = "Ilmu Komunikasi"
print("Jurusan\t\t\t :",prodi)
biaya_tambahan = 0
total = 0
if kelas == "Reguler 2":
    biaya_tambahan = 700000


total = biaya_kuliah+biaya_tambahan
print("Biaya\t\t\t : Rp.",f"{biaya_kuliah:,}")
print("Kelas\t\t\t :",kelas)
print("Biaya Tambahan\t\t : Rp.",f"{biaya_tambahan:,}")
print("Jumlah Biaya\t\t : Rp.",f"{total:,}")
print("================================================================")
print("\t\tUTS by Bias Yulisan Geni, S.Kom., M.Kom.")
print("================================================================")





