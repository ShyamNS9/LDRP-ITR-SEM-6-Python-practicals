# Set-7 Practical-5 : Write the program-4 for a text file with missing values (missing values are represented as
# hyphen (-)).

f = open('number2.txt', 'r')
data_list = f.readlines()
f.close()
result_list = []
count = 0

for data in data_list:
    data = data.replace('\n', '')
    if data == '-':
        count = count + 1
        data = data.replace('-', '0')
    result_list.append(int(data))
print(count, result_list)
