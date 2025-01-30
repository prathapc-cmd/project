def fun():
    x= 30
    def myfun():
        print(x)
    myfun()

fun()

print('_______________________')

class myfun:
    x=300
    def fun():
        x=200
        print(x)
    fun()

    print(x)

print('_______________________')

class myfun:
    
    def fun():
        global x
        x=200
        
    fun()
    
    print(x)




    