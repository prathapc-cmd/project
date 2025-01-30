class college:
    def student():
        for i in range(0,11):
            print(i)
        

class res:
    college.student()

print('---------------------------')

class college:
    def __init__(self,name,age):
        self.name = name
        self.age= age

    def __str__(abc):
        return f"{abc.age,abc.name}"
    
    def student(a):
        print(a.name)
    
class res(college):
    x = college("varun",23)
    print(x.name)
    print(x)
    x.student()

class res(college):
    def __init__(self,name,age,standard):
        super().__init__(name,age)
        self.standard = standard

x= college("prathap",27,10)
print(x.standard)

    