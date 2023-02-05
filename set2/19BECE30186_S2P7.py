# Set-2 Practical-7 : Write a Python program to check whether entered input is character, digit or special symbol
# using ladder if-else.

a = input("Enter : ")
if a.isalpha():
    print(a, "is a Character")
elif a.isnumeric():
    print(a, "is a Number")
else:
    print(a, "is a Special Symbol")
