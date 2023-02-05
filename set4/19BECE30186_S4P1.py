# Set-4 Practical-1 : Write a Python program which covers all the methods (functions) of list.

L1 = [1, 2, 3, 4, 5]

# Adds an element at the end of the list
L1.append(6)
print(L1)

# Removes all the elements from the list
L1.clear()
print(L1)

# Returns a copy of the list
L1 = [1, 2, 3, 4, 5]
L2 = L1.copy()
print(L2)

# Returns the number of elements with the specified value
L3 = [10, 20, 30, 10, 10]
n = L3.count(10)
print(n)

# Add the elements of a list (or any iterable), to the end of the current list
L3.extend(L1)
print(L3)

# Returns the index of the first element with the specified value
print(L3.index(30))

# Adds an element at the specified position insert(pos,value)
L3.insert(9, 2)
print(L3)

# Removes the element at the specified position
print(L3.pop(9))

# Removes the item with the specified value
L3.remove(30)
print(L3)

# Reverses the order of the list
L3.reverse()
print(L3)

# sorted list
L3.sort()
print(L3)
