# Set-3 Practical-6 : Write a Python program to check whether entered number is prime or not.

num = int(input("Enter a Number: "))
if num > 2:
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
