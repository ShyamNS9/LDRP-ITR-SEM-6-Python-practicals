# Set-5 Practical-1 : Create a set of integers as follows:
#  initialize the set directly
#  initialize empty set and then add values
#  from a list
#  from another set
#  using range
#  update an existing set using another set
#  print the elements of set iteratively
#  check the functionality of remove and discard

set1 = {1, 2, 3}
set2 = set()

'''using add func'''
set2.add(5)
set2.add(6)

print("Adding elements in empty set :\n", set2)

list1 = [10, 20, 30]

'''using update func to add value from list'''

set2.update(list1)
print("\nUpdated from another list : \n", set2)

'''using update func to add value from another set'''
set3 = {11, 22, 33}
set2.update(set3)
print("\nUpdated from another set : \n", set2)

''' print the elements of set iteratively'''

print("\nPrinting elements of set :\n")
for i in set2:
    print(i)

'''using remove func'''
set2.remove(10)
print("Removed\n", set2)

'''using discard func'''
set2.discard(20)
print("Discard\n", set2)
