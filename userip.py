name = input("enter a name: ")

if name == "capgemini":
    print(f"my company name is {name}")
else:
    print(f"{name.upper()} is not my company")

print("---------------------------------")

n = int(input("Enter a number: "))

for i in range(1,11):
    a = n*i
    print(int(a))

print("---------------------------------")

n = list(input("Enter a number: "))

print(n)

