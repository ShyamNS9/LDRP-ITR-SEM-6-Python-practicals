# Set-7 Practical-2 : Write a Python program to read a file containing pairs of numbers in a file. Create a file that
# contains the pairs of numbers as well as addition and multiplication of the two numbers in the same line.

file1 = open('number.txt', 'r')
print("Elements inside the file are: ")
print(file1.read())
file1.close()

file1 = open('number.txt', 'r')
data_list = file1.readlines()
file1.close()

file1 = open('number.txt', 'w')
result_list = []
for data in data_list:
    data = data.replace('\n', '')
    num1, num2 = data.split(' ')
    result = '{} {} {} {} \n'.format(num1, num2, int(num1)+int(num2), int(num1)*int(num2))
    result_list.append(result)
file1.writelines(result_list)
file1.close()

file1 = open('number.txt', 'r')
print("Elements inside the file are: ")
print(file1.read())
file1.close()
