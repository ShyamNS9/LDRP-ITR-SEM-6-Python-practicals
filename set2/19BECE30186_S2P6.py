# Set-2 Practical-6 : Write a Python program to calculate the salary of an employee based on following conditions
# (nested if-else):
# 1. if degree = B.E. and experience < 5 years, salary=30000
# 2. if degree = B.E. and experience >= 5 years, salary=40000
# 3. if degree = M.E. and experience < 5 years, salary=50000
# 4. if degree = M.E. and experience >= 5 years, salary= 60000

degree = input("Enter Degree(ME or BE) : ")
exp = int(input("Enter Experience(years) : "))

if degree == 'BE':
    if exp < 5:
        print("salary will be 30000")
    elif exp >= 5:
        print("salary will be 40000")
elif degree == 'ME':
    if exp < 5:
        print("salary will be 50000")
    elif exp >= 5:
        print("salary will be 60000")
else:
    print("Enter valid Degree.")
