# Set-3 Practical-8 : Write a Python program to calculate N!.

num = int(input("Enter the number to find factorial: "))
factorial = 1
if num == 0 or num == 1:
    print("Factorial of given number is:", factorial)
else:
    for i in range(1, num+1):
        factorial = factorial * i
    print("Factorial of given number is:", factorial)