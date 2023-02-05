# Set-3 Practical-4 : Write a Python program to print Fibonacci series upto n terms.

def fibo(i):
    if i <= 1:
        return i
    else:
        return fibo(i - 1) + fibo(i - 2)


num = int(input("Enter a Number: "))
if num <= 0:
    print("Enter a positive number.")
else:
    print("Fibonacci series: ", end=" ")
    for n in range(num):
        print(fibo(n), end=" ")
