class emp:
    print("hello")

print('------------------------')

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
s = student("arun",23)
# print(s) not working
print("his name is " + s.name + ' and age is '+str(s.age))

print('------------------------')

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name,self.age}"
    
s = student("arun",23)
print(s) 
print("his name is " + s.name + ' and age is '+str(s.age))

print('------------------------')

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def emp(abc):
        print(abc.name)
s = student("arun",34)
s.emp()
s.name = 'varun'
print(s.name)