# Set-4 Practical-17 : Flatten a nested list structure.
# Example: if list1 = [1, [2, 3], [4, 5, [6, 7] ] ] then try to convert it in 1-dimensional
# [1, 2, 3, 4, 5, 6, 7]

L2 = []


def convert_1_dimension(L):
    for i in L:
        if type(i) == list:
            convert_1_dimension(i)
        else:
            L2.append(i)
    return L2


L1 = [1, [2, 3], [4, 5, [6, 7]]]
print(convert_1_dimension(L1))
