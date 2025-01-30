class student:
    def abc(self,name):
        print(name)
      
try:
    student().abc("ajay")
except Exception as e:
    print(f'an error occured: {e}')
finally:
    print('executed complete code')



i = "queue"

if type(i) is not int:
    raise TypeError("type is not an integer")


