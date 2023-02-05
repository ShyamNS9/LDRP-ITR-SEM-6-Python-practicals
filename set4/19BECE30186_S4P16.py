# Set-4 Practical-16 : Write a Python program to transpose a given matrix.

L2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def transpose_matrix(L):
    for i in range(len(L)):
        for j in range(len(L[i])):
            if i == j:
                L2[i][j] = L1[i][j]
            else:
                L2[i][j] = L1[j][i]
    return L2


L1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose_matrix(L1))
