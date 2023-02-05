# Set-5 Practical-9 : Write a Python program to print a dictionary where the keys are numbers between 1 and 15 (both
# included) and the values are square of keys.

dic = dict()
for x in range(1, 10):
    dic[x] = x**2
print(dic)
