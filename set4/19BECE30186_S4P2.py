# Set-4 Practical-2 : Write a Python program to append a list to the second list.

L1 = [1, 2, 3, 4, 5]
L2 = [11, 22, 33, 44, 55]

L2.append(L1)
print(L2)

L1 = [1, 2, 3, 4, 5]
L2 = [11, 22, 33, 44, 55]

L2.extend(L1)
print(L2)
