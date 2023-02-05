# Set-6 Practical-4 : Write a Python program to find Armstrong number in a specific range using map.

list1 = [153, 370, 371, 1634, 125, 207, 100, 310, 407]


def armstrong(a):
    temp = a
    count = 0
    sum = 0
    while a != 0:
        count += 1
        a = a // 10
    a = temp
    while a != 0:
        rev = a % 10
        sum = rev ** count + sum
        a = a // 10
    if sum == temp:
        return temp


list2 = list(map(armstrong, list1))
print(list2)
