# Set-4 Practical-14 : Write a Python program to print the numbers of a specified list after removing even numbers
# from it.

n = int(input("Enter the number :"))
L1 = [i for i in range(n) if i % 2 != 0]
print(L1)
