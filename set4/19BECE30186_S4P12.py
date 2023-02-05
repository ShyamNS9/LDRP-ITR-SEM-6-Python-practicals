# Set-4 Practical-12 : Write a Python program to find the list of words that are longer than n from a given string.

L1 = []


def str_find(n, str):
    str1 = str.split(" ")
    for i in str1:
        if n < len(i):
            L1.append(i)


str = "I am inevitable"
str_find(2, str)
print(L1)

