# Set-2 Practical-3 : Write a Python program to find roots of quadratic equations if roots are real.

def root(a, b, c):
    d = b ** 2 - 4 * a * c
    sqrt_d = abs(d) ** 0.5

    if d > 0:
        print("Quadratic equation has real and distinct roots")
        print((-b + sqrt_d) / (2 * a))
        print((-b - sqrt_d) / (2 * a))

    if d == 0:
        print("Quadratic equation has real and one roots")
        print(-b / (2 * a))

    if d < 0:
        print("Quadratic equation has imaginary and distinct roots")
        print(-b / (2 * a), "+ i", sqrt_d / (2 * a))
        print(-b / (2 * a), "- i", sqrt_d / (2 * a))


p = int(input("Enter number a: "))
q = int(input("Enter number b: "))
r = int(input("Enter number c: "))

if p == 0:
    print("Enter correct quadratic equation.")
else:
    root(p, q, r)
