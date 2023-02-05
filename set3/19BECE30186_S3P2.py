# Set-3 Practical-2 : Write a Python program to find sum of N scanned numbers.

su = 0
print("Enter numbers to add them")
print("Press 0 to exit")
while True:
    n = int(input("Enter the number: "))
    if n == 0:
        break
    su = su + n
print("The sum of all given numbers is:", su)
