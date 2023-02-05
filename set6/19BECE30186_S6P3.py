# Set-6 Practical-3 : Write a Python program to find maximum from a list using reduce.
from functools import reduce

list1 = [2, 3, 5, 6, 7, 9, 11, 12, 15, 17, 19, 23, 55, 43]
print(reduce(max, list1))
