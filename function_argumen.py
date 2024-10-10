def hello_world(nama):
    print(f"Hello World {nama}")

def tambah(angka1,angka2):
    hasil = angka1+angka2
tambah(1,5)
tambah(2023,2021)

def say_hi(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Yang terhormat {peserta}")

mhsti = ["Ananda", "Salwa","Anisa","Naufal","Galih","Rifai"]

say_hi(mhsti)