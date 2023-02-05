# Set-6 Practical-2 : Write a Python program to make sum of particular range using reduce.

from functools import reduce

list1 = [2, 3, 5, 6, 7, 9, 11, 12, 15, 17, 19, 23, 55, 43]
sum = reduce(lambda x, y: x + y, list1)
print(sum)
