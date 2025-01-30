def student():
    print("first function")

student()
print("======================")

def student(name):
    print("my name is " + name)

student("prathap")
print("======================")

class student():
    def emp(name,age,salary):
        i=5
        print("emp name is "+ name + " and age is "+ str(age) + " and salary "+str(salary))
        if i ==5:
            for j in range(0,11):
                print(j) 

class result:
    student.emp('ajay',23,23456)
    student.emp('vijay',27,43456)
print("======================")
#known number of arguments
def student(name,age,grade):
    print("my name is "+ name + " and age is "+ str(age) + ". i have scored " +  grade  + " grade")

student('prathap',27,"a")
student('ajay',23,'d')
print("======================")
#unknown number of arguments
def emp(*kid):
    print(kid[4])

emp("n",'d','f','d','e')
print("======================")
#known number of keyword argument
def student(name2,name3,name1):
    print(name3)

student(name1='a',name2='b',name3='c')

print("======================")
#unknown number of keyword arguments
def emp(**kid):
    print(kid['lname'])

emp(fname="a",lname='b')

print("======================")
#return function

def age():
    return "age bar"
print(age())

def age():
    return 5*6
print(age())

def age(x):
    return 23+x
print(age(4))

def age():
    pass
print("-------------------")
# def solve():
#     n= list(input())
#     print(n)
#     # i = list((input(n)))
#     a = max(n)
#     b = n.remove(a)
#     c = max(n)
#     print(c)
    
# solve()

print("-------------------")
def fun():
    n= list(input())
    n.sort()
    print(n)
    a = dict.fromkeys(n)
    b= set(a)
    print(b)
    print(b[-2])

fun()
    