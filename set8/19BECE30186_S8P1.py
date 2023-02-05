# Set-8 Practical-1 : Write a Python program which will throw exception if the value entered by user is less than zero.

n = int(input("Enter a Number: "))

if n < 0:
    raise Exception("Error: Entered Number is less then zero.")
