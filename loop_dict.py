smester2 = {
    "AP2":"Algoritma dan Pemograman 2",
    "KSI":"Keamanan Sistem Informasi",
    "STD":"Struktur Data dan Algoritma",
}

for kuliah in smester2:
    print(smester2)

keys = smester2.keys()
print(keys)

for key in smester2.keys():
    print(smester2.get(key))

values = smester2.values()
print(values)

for value in smester2.values():
    print(value)

items = smester2.items()
print(items)

for item in smester2.items():
    print(item)

for key,value in smester2.items():
    print(f"key = {key}, value = {value}")
