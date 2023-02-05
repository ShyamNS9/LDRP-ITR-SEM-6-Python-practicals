# Set-5 Practical-2 : Create two sets of integers and find their difference, intersection, union and symmetric
# difference. Also find subset and superset from these two. Apply methods as well as operators for all operations.

set1 = {10, 20, 30}
set2 = {20, 40, 50}

'''difference between two sets'''
print(set1 - set2)

'''intersection between two set'''
print(set1.intersection(set2))

''' union '''
print(set1.union(set2))

''' symmetric difference '''
print(set1.symmetric_difference(set2))

''' subset '''
set3 = {40, 50, 10, 20, 30}
print(set1.issubset(set3))

''' super set'''
print(set3.issuperset(set1))
