# Implementasi Tipe Data
print("----------------Tipe Data-------------")
tipe_integer = 20
print("data : ", tipe_integer)
print("- bertipe", type(tipe_integer))

tipe_float = 4.5
print("data : ", tipe_float)
print("- bertipe", type(tipe_float))

tipe_string = "Mumtaz Azkia"
print("data : ", tipe_string)
print("- bertipe", type(tipe_string))

tipe_bool = True
print("data : ", tipe_bool)
print("- bertipe", type(tipe_bool))

tipe_complex = complex(1,2)
print("data : ", tipe_complex)
print("- bertipe", type(tipe_complex))

from ctypes import c_double,c_char

tipe_c_double = c_double(29.55)
print("data : ", tipe_c_double)
print("- bertipe", type(tipe_c_double))
print("----------------------------")

# Implementasi Variable
print("----------------Implementasi Variable-------------")
x = 5
y = 0
ribu100 = 100000
print('Nilai x : ',x)
print('Nilai y : ',y)
x = y
y = x
print('Nilai x : ',x)
print('Nilai y : ',y)
print('Nilai ribu100 : ',ribu100)
print("----------------------------")

# Implementasi Operasi
print("----------------Implementasi Operasi-------------")
nil1 = 500
nil2 = 300
nil3 = 2

penjumlahan = nil1+nil2
print(f"{nil1} + {nil2} : ",penjumlahan)
pengurangan = nil1-nil2
print(f"{nil1} - {nil2} : ",pengurangan)
perkalian = nil1*nil2
print(f"{nil1} * {nil2} : ",perkalian)
pembagian = nil1/nil2
print(f"{nil1} / {nil2} : ",pembagian)
modulus = nil1%nil2
print(f"{nil1} % {nil2} : ",modulus)
perpangkatan = nil1**nil3
print(f"{nil1} ** {nil3} : ",perpangkatan)
pembagian_bulat = nil1//nil2
print(f"{nil1} // {nil2} : ",pembagian_bulat)
print("----------------------------")

# Implementasi Operasi I/O
print("----------------Implementasi Operasi i/O-------------")
nama = input("Nama : ")
nim = input("NIM : ")
nilai1 = int(input("Nilai 1 : "))
nilai2 = int(input("Nilai 2 : "))
print("Nama : ", nama)
print("NIM : ", nim)
jmlh = nilai1+nilai2
print(f"{nilai1} + {nilai2} : ",jmlh)
kurang = nilai1-nilai2
print(f"{nilai1} - {nilai2} : ",kurang)
kali = nilai1*nilai2
print(f"{nilai1} * {nilai2} : ",kali)
bagi = nilai1/nilai2
print(f"{nilai1} / {nilai2} : ",bagi)
mod = nilai1%nilai2
print(f"{nilai1} % {nilai2} : ",mod)
pangkat = nilai1**nilai2
print(f"{nilai1} ** {nilai2} : ",pangkat)
pemb = nilai1//nilai2
print(f"{nilai1} // {nilai2} : ",pemb)
print("-----------------------------")
