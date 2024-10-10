def kuadrat(input_angka):
    output_kuadrat = input_angka**2;
    return output_kuadrat

y = kuadrat(3)
print(y)

print(kuadrat(6))
z = 10 + kuadrat(7)
print(z)

def fungsitambah(angka1,angka2):
    return angka1+angka2

a = fungsitambah(10,8)
print(a)

def operasi_mtk(angka1,angka2):
    tambah = angka1+angka2
    kurang = angka1-angka2
    kali = angka1*angka2
    bagi = angka1/angka2

    return tambah,kurang,kali,bagi

k, l, m, n = operasi_mtk(10,5)
print(f"Hasil Tambah = {k}")
print(f"Hasil Kurang = {l}")
print(f"Hasil Kali = {m}")
print(f"Hasil Bagi = {n}")