# Set-4 Practical-18 : Write a Python program to split a list every Nth element.

def split_step(L, n):
    return (L[i::n] for i in range(n))


L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = int(input("Enter the no to split : "))
print(list(split_step(L1, n)))
