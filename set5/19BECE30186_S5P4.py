# Set-5 Practical-4 : The following company details are given for analysis: customer acc no, customer name,
# purchased product no, product category, unit price. Marketing is interested in understanding customer purchase
# patterns. Find the answers of following questions:
#  How many customers have purchased bread?
#  How many customers have purchased butter?
#  How many customers have purchased bread and butter?
#  Who has purchased bread but not butter?
#  Which customers have purchased bread, butter and milk?
#  Print the name of the most valuable customers who have purchased all three items.

bread_buyer = {'John', 'Alice', 'Dan', 'Sue'}
butter_buyer = {'Alice', 'Margaret', 'Mary'}
milk_buyer = {'Mary', 'Margaret', 'Dan', 'Alice'}

A = bread_buyer & butter_buyer
B = bread_buyer - butter_buyer
C = bread_buyer & butter_buyer & milk_buyer

print("Bread Buyer: ", bread_buyer)
print("Butter Buyer: ", butter_buyer)
print("Bread & Butter buyer: ", A)
print("Bread but not Butter: ", B)
print("Bread, Butter & Milk: ", C)
print("Most valuable customers: ", C)
