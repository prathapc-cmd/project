#unordered,unchangeable, not allow duplicates

set1 = {"mango","apple","banana","chikku",1,4,5}
set2 = {"baana"}
        
print(set1)
print(type(set1))

print(len(set1))

#add
set1.add("kiwi")
print(set1)
set1.update(set2)
print(set1)

#remove
set1.remove("baana")
print(set1)

