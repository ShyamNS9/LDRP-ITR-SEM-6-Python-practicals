# Set-5 Practical-3 : Write a function called find_dups that takes a list of integers as its input argument and
# returns a set of those integers that occur two or more times in the list.

def find_dups(list1):
    list2 = []
    for i in list1:
        n = list1.count(i)
        if n > 1:
            if list2.count(i) == 0:
                list2.append(i)

    return list2


list1 = [10, 20, 10, 30, 20, 30, 40]
print(find_dups(list1))
