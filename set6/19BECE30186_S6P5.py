# Set-6 Practical-5 : Write a Python program to apply two functions (square and cube) simultaneously on a specific
# range using map.

def square(num):
    return num * num


def cube(num):
    return num * num * num


func = [square, cube]
for i in range(10):
    ans = list(map(lambda x: x(i), func))
    print(ans)
