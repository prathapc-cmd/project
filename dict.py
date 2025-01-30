#ordered,changeable,no duplicate allowed

dict1 = {
    "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(dict1)
print(type(dict1))

#access
print(dict1['brand'])
print('the brand is',dict1['brand'],'and year of launch',dict1['year'])
print(dict1.keys())
print(dict1.values())

#update
dict1['brand'] = 'xuv'
print(dict1)
#add
dict1['color'] = 'red'
print(dict1)
#remove
dict1.pop("year")
print(dict1)

dict1.popitem()
print(dict1)

#delete
# del dict1['model']
# print(dict1)
# del dict1()
# print(dict1)

#clear
# dict1.clear()
# print(dict1)

for x in dict1.items():
    print(x)
