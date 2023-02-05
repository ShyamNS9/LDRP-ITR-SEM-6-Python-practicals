# Set-2 Practical-5 : Write a Python program to find maximum of three numbers (nested if-else).

a = int(input("Enter Number1: "))
b = int(input("Enter Number2: "))
c = int(input("Enter Number3: "))
if a > b:
    if a > c:
        print(a, "is maximum")
    elif c > b:
        print(c, "is maximum")
elif b > c:
    print(b, "is maximum")
else:
    print(c, "is maximum")
