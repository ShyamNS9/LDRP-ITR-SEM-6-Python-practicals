# Set-5 Practical-10 : Write a Python program to check if a given key already exists in a dictionary.

dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def key_present(x):
    if x in dic:
        print("key is present")
    else:
        print("key is not present")


key_present(5)
key_present(9)
