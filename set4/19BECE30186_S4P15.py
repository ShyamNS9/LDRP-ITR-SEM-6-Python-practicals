# Set-4 Practical-15 : Write a Python program to add two matrices.

L3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def add_matrix(L1, L2):
    for i in range(len(L1)):
        for j in range(len(L1[i])):
            L3[i][j] = L1[i][j] + L2[i][j]

    return L3


L1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
L2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print(add_matrix(L1, L2))
