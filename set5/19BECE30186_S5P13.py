# Set-5 Practical-13 : Write a Python program to create a dictionary from two lists.

key_val = ['a', 'b']
val_list = [1, 2]
zip_list = zip(key_val, val_list)
dic = dict(zip_list)
print(dic)
