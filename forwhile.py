#while

i = 4
while i < 10:
    print(i)
    if i == 7 :
        break
    i += 1

i = 4
while i < 10:
    i += 1
    # if i == 7 :
    #     continue
    print(i)
else:
    print("none")

i = 3
while i <31:
    print(i)
    i += 3
#for

for i in range(10):
    print(i)

print("==================")
for i in range(10,21):
    print(i)

print("==================")
for i in range(0,10,2):
    print(i)

print("==================") 

box = [1,2,3,4,5]
tool = [6,7,8,9,0]
for x in box:
    for y in tool:
        print(x,y)
        


