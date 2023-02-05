# Set-5 Practical-7 : Write a Python program to find multiple items of a tuple

tuple1 = [int(x) for x in input("Enter values: ").split()]
tuple1 = tuple(tuple1)
t = tuple1
print("Repeated values: ")
for i in range(0, len(t)):
    for j in range(i+1, len(t)):
        if t[i] == t[j]:
            print(t[j], end=" ")
