# Set-3 Practical-11 : Write a Python program to print the following:
# 1) 1                  2) * * * * *
#    1 2                   * * * *
#    1 2 3                 * * *
#    1 2 3 4               * *
#    1 2 3 4 5             *

n = int(input("Enter the number : "))
for i in range(n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

n = int(input("Enter the number : "))
for i in range(n + 1):
    for j in range(i, n):
        print("*", end=' ')
    print()
