# Set-7 Practical-4 : Write a Python program to create a function that returns smallest value from the given text file.

f = open('number1.txt', 'r')
data_list = f.readlines()
f.close()
result_list = []

for data in data_list:
    data = data.replace('\n', '')
    result_list.append(int(data))
print(min(result_list))
