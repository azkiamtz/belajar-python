print("PROGRAM DAFTAR GAJI KARYAWAN")

jumlah_karyawan = int(input("Masukan Jumlah Karyawan \t\t : "))
bulan = input("Masukan Bulan \t\t : ")
list_karyawan = []
print("="*39)
print("="*10,"INPUT DATA KARYAWAN","="*10)
print("="*39)
i = 0
while i<jumlah_karyawan :
    print("Data Karyawan ke - ",i+1)
    nip = input("NIP Karyawan = ")
    nama = input("Nama Karyawan = ")
    kode_jabatan = input("Kode Jabatan [1/2] = ")
    kode_status = input("Kode Status [M/S] = ")
    karyawan_baru = [nip,nama,kode_jabatan,kode_status]
    list_karyawan.append(karyawan_baru)
    i = i+1

print("="*50)
print("\t\t\t\t\t DAFTAR GAJI KARYAWAN \t\t\t\t\t")
print("\t\t\t\t\t PT BEYEGE \t\t\t\t\t")
print("Bulan = ",bulan)
print("="*50)
print("No. | NIP Karyawan | Nama Karyawan | Jabatan | Status | Gaji Pokok | Tunjangan | Total Gaji")
z = 1
total_gaji = 0
for data in list_karyawan:
    kode_jab = data[2]
    kode_stat = data[3]
    if kode_jab == "1" :
        jabatan = "Administrasi"
        gapok = 1700000 
        if kode_stat == "M":
            tunjangan = 500000
            status = "Menikah"
        else:
            tunjangan = 250000
            status = "Single"
    else:
        jabatan = "Operasional" 
        gapok = 2000000 
        if kode_stat == "M":
            status = "Menikah"
            tunjangan = 700000
        else:
            status = "Single"
            tunjangan = 350000
    total = int(gapok+tunjangan)
    total_gaji += total
    print(f"{z+1} | {data[0]} | {data[1]} | {jabatan} | {status} | {gapok} | {tunjangan} | {total}")
    z = z+1
print("\t\t\t\t\t\t\t\t Total Gaji Karyawan Rp",total_gaji)
