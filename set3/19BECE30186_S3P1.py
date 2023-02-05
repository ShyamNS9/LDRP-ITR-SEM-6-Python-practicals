# Set-3 Practical-1 : Write a Python program to find sum of first N numbers.

su = 0
n = int(input("Enter the number: "))
a = n
while n > 0:
    su = su + n
    n = n - 1
print("The sum of first", a, "numbers is:", su)
