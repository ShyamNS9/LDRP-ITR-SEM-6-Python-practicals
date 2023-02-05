# Set-5 Practical-11 : Write a Python program to merge two Python dictionaries.

dic1 = {'a': 100, 'b': 200}
dic2 = {'x': 300, 'y': 200}
d = dic1.copy()
d.update(dic2)
print(d)