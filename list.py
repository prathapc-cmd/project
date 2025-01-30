# ordered,changeable,allow duplicates

list1 = ["mango","apple","banana","chikku","grapes"]
list2 = ['chikku', 'grapes', 'orange', 'mango']
if "apple" in list1:
    print("apple is present")
print(list1)
print(type(list1))
list1.append("orange") #changing the list
print(list1)
list1.append("mango") #allow duplicate
print(list1)
list1.remove("apple") # removing the iten
print(list1)

#access the list
print(list1[2])
print(list1[-2])
print(list1[2:4])
print(list1[2:])

#changing the list
list1[1]="kivi"
print(list1)
list1[1:3]=["banana","watermelon"]
print(list1)

#add the items
list1.append("sapota")
print(list1)
list1.insert(2,"musk")
print(list1)
list1.extend(list2)
print(list1)

#remove the items
list1.remove("musk")
print(list1)
list1.pop(5)
print(list1)
# del list1
# print(list1)
del list1[1]
print(list1)

for x in list1:
    print(x)
    if x == "orange":
        break

list1.sort()
print(list1)

list3=list1.copy()
print(list3)

#comprehensive
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if 'a' in x:
        newlist.append(x)

print(newlist)

file_path =  "C:/Users/prathapc/Documents/personal/internet reimbursement/abc.txt"
file_name = file_path.split('/')[-1]
print(file_name)