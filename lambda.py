x= lambda a,b,c : a+b*c

print(x(3,4,5))

print('------------------------')

def age():
    return lambda a,b: a+b

a = age()
print(a(3,4))

print('------------------------')

def sal(n):
    return lambda s : s* n

x= sal(4)
print(x(3000))

print('------------------------')


