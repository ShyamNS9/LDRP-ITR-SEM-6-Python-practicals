# Set-3 Practical-5 : Write a Python program to find the reverse of given numbers (Example 2564-4652).

n = int(input("Enter a Number: "))
rev = 0
while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
print("Reverse of the given number is:", rev)
