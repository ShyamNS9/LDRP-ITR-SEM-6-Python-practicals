# Set-6 Practical-6 : Write python programs using (i) map/filter and function (ii) map/filter and lambda
# (iii) list comprehension
#  Create a list to store the cube of all the elements in a given list.
#  Create a list of equivalent Celsius degree from Fahrenheit.
#  Create a list that stores only positive numbers from given list.
#  Create a list that stores only alphabets from given list.

print("using list and function")


def cu(a):
    return a * a * a


list1 = [2, 3, 4, 5, 6, 7, 8]
cube = list(map(cu, list1))
print(cube)
print("using list and lambda")
list1 = [2, 3, 4, 5, 6, 7, 8]
cube = list(map(lambda x: x * x * x, list1))
print(cube)
print("using list comprehensions")
list2 = [i ** 3 for i in range(1, 10)]
print(list2)
