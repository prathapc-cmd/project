#ordered,unchangeable, allow duplicate

tuple1 = ('banana',1,2,"apple")

print(tuple1)
print(type(tuple1))
print(tuple1[3])

#add the item
# tuple1.append("nanu")
# print(tuple1)
y= list(tuple1)
y.append("org")
tuple2 = tuple(y)
print(tuple2)

#unpack the tuple
(a,b,c,d) = tuple1
print(b)
print(d)
print(c)





