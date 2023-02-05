# Set-4 Practical-13 : Write a Python function that takes two lists and returns True if they have at least one common
# member.

def common_inlist(L1, L2):
    for i in L1:
        for j in L2:
            if i is j:
                return True
    else:
        return False


L1 = [1, 2, 3, 4, 5]
L2 = [6, 7, 8, 9, 5]

print(common_inlist(L1, L2))
