data_list = ['Naufal','Galih','Ivan']
print(data_list[0])

data_dict = {
    "key":'value',
    "NF":"Naufal",
    "IV":"Ivan",
    "GL":"Galih",
    "No":"26",
    "list":data_list
}

data_dict["oke"] = "oke"

print(data_dict['NF'])
print(data_dict['No'])
print(data_dict['list'])

for data in data_dict:
    print(data_dict[data])