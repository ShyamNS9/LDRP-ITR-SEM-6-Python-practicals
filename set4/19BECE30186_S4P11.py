# Set-4 Practical-11 : Write a Python program to remove duplicates from a list.

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))
