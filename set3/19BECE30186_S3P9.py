# Set-3 Practical-9 : Write a Python program to check whether given number is Armstrong or not.

sum = 0
count = 0
n = int(input("Enter number : "))
temp = n
while n != 0:
    count += 1
    n = n // 10
n = temp
while n != 0:
    rev = n % 10
    sum = rev ** count + sum
    n = n // 10
if sum == temp:
    print(temp, "is Armstrong")
else:
    print(temp, "is not Armstrong")
