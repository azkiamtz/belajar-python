#list
list1 = ["Rifda", "Salwa", "Elia", 2021, 2023]
print (list1[0])

#penulisan tuples
data = ("PHP", "Python", "Ruby", "Boostrap", "CSS", "R", "HTML")
print (data)

#mengakses tuple dengan range
data = ("a", "b", "c", "d", 1, 2, 3, 4)
#data 1 sampai 4
print (data[:4])

#data 4 sampai 8
print (data[4:8])

#menghitung jumlah nilai tuple
data = ("a", "b", "c", "d", 1, 2, 3, 4)
#melihat jumlah nilai
print (len(data))

#menguji keanggotaan tuple
data = ("a", "b", "c", "d", 1, 2, 3, 4)
#cek apakah c termasuk kedalam nilai tuple
print ("c" in data)

#cek apakah c tidak termasuk kedalam nilai tuple
print ("c" not in data)

#cek apakah z termasuk kedalam nilai tuple
print ("z" in data)