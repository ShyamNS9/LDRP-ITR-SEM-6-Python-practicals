# Set-4 Practical-10 : Write a Python program to count the number of strings where the string length is 2 or more and
# the first and last character are same from a given list of strings.

l = ['aba', 'lol', 'hello', 'val', 'hoh']
l1 = []
n = len(l)
for j in range(n):
    a = l[j]
    i = len(a)
    i -= 1

    if a[0] == a[i]:
        l1.append(a)

print(l1)
