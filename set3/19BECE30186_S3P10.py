# Set-3 Practical-10 : Write a Python program to check whether given number is Palindrome or not.

rev = 0
n = int(input("Enter number : "))
temp = n
while n != 0:
    rev = rev * 10 + n % 10
    n = n // 10
if rev == temp:
    print(temp, "is palindrome")
else:
    print(temp, "is not palindrome")
