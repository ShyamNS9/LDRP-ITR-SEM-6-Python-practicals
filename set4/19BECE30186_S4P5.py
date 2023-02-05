# Set-4 Practical-5 : Write a Python program to print list of prime numbers upto N using loop and else clause.

l = []
n = int(input("Enter number : "))

for i in range(2, n + 1):
    for j in range(2, (i // 2) + 1):
        if i % j == 0:
            break

    else:
        l.append(i)

print(l)

