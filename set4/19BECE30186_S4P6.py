# Set-4 Practical-6 : Write a Python program to check whether the given list is palindrome or not.

l = [10, 20, 10]
r = l[::-1]
print(r)
if l == r:
    print("Palindrome")
else:
    print("Not palindrome")
