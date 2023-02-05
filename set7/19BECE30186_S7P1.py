# Set-7 Practical-1 : Write a Python program to read the text file using read (), readlines() and readline() methods.

f = open('try.txt', 'r')
print(f.read())
f.close()

f = open('try.txt', 'r')
print(f.read(25))
f.close()

f = open('try.txt', 'r')
print(f.readline())
print(f.readline())
f.close()

f = open('try.txt', 'r')
print(f.readlines())
f.close()
