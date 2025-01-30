#remove duplicate
mylist = [1,2,5,3,7,'dev','prod','dev']
mylist = list( dict.fromkeys(mylist) )
print(mylist)

#print the output in single line
for i in range(0,11):
    print(i,end="")

#reverse a string
def reverse(n):
    print(n[::-1])

reverse("my name is prathap")
reverse(str(1234))

#split
a = '1Split the string, 2using comma, 3followed by a space, 4as a separator:'
b = a.split(',')
c = a.split(' ')
d = a.split('s')
print(b)
print(c)
print(d)

#replace
a = 'vijay'
b = a.replace('vi','a')
print(b)
