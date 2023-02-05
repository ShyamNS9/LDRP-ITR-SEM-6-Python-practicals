# Set-6 Practical-1 : Write a Python program to find the prime numbers in a specific range using filter.

def is_prime(t):
    if t <= 1:
        return False
    for i in range(2, t):
        if t % i == 0:
            return False
    return True


lst = [i for i in range(100)]
lst = list(filter(is_prime, lst))
print(lst)
