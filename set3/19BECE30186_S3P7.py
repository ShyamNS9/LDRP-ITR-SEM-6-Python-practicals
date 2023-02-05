# Set-3 Practical-7 : Write a Python program to print all even numbers between 1 to n except the numbers divisible by 6.

n = int(input("Enter a range: "))
for i in range(2, n, 2):
    if i % 6 != 0:
        print(i)
