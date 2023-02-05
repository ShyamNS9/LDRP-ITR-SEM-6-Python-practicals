# Set-9 Practical-1 : Write a Python program to create class KSV with attributes like class variable cnt,
# instance variables x and y, instance methods get_value and print_value.

class KSV:
    def __init__(self, clg1, clg2):
        self.clg1 = clg1
        self.clg2 = clg2

    def get_value(self):
        print("First College: ", self.clg1, "\nSecond College: ", self.clg2)


x = KSV("LDRP", "VSITR")
x.get_value()
