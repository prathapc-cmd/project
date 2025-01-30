# # class student:
# #     def name(self): 
# #         for i in range (1,11):
# #             # if i==5 and i!=6:
# #                 i = i**3
# #                 i=str(i)
# #                 i = i.replace('8','eight')
# #                 print(i)
        
# # class teacher:
# #     student().name()

# class mylist:
#     list1 = [True, False, False]
#     tuple2 = (1, 5, 7, 9, 3,1)
#     set3 =  {"apple", "banana", "cherry","apple"}
#     dict4 = { 'apple' : 1,
#             'orange' : 2,
#             'mango' : 3}
#     print(type(list1))
#     print(type(tuple2))  
#     print(type(set3)) 
#     print(type(dict4)) 
#     print(list1)
#     print(tuple2)
#     print(set3)
#     print(dict4)  

#     list1.append("True")
#     print(list1)


# i=1
# while i < 10:
#         print(i)
#         if i==3:
#                 break
#         i +=1

# i=1
# while i < 10:
#         i +=1
#         if i==3:
#                 continue
#         print(i) 

   
# i=2
# for i in range(1,11):
#         print(i)  
#         if i ==5:
#                 continue 

x= lambda a,s: a+s
print(x(5,4))

def number(n):
        return lambda a: a*n

num = number(5)
num = number(3)
print(num(3))
print(num(6))