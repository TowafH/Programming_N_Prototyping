# 9/30/24
# PD 1-2
# Towaf Hossain

'''
A little Canadian kid broke their Piggy Bank.
You are to create a program to help him figure
out how much money they have.
# Pennies = 1¢
# Nickels = 5¢
# Dimes = 10¢
# Quarters = 25¢
# Loonies = 1$ or 100¢
# Toonies = 2$ or 200¢
1. Ask the kid how many coins they have of each kind.
2. Calculate the total and give the answer in decimals and in a combo
Ex: $13.67 <-- Decimal Form
Ex: $13, 2 quarters, 1 dime, 1 nickel, 2 pennies
'''

print("Welcome to the Loony Bank of Canada, We can calculate how many coins and loonies you have!\n")
penny = int(input("How many pennies do you have?"))
nickel = int(input("How many nickels do you have?"))
dime = int(input("How many dimes do you have?"))
quarter = int(input("How many quarters do you have"))
loonies = int(input("How many loonies do you have?"))
toonies = int(input("How many toonies do you have?"))

# Total Amount Of Money
total_amount = ((.01 * penny) + (.05 * nickel) + (.10 * dime) + (.25 * quarter) + (1.0 * loonies) + (2.0 * toonies))

# Print the money and display the amount of each
print("You have a total of $" + str(total_amount) + "\n\nYou had " + str(penny) + " pennies, " + str(nickel) + " nickels, " + str(dime) + " dimes, " + str(quarter) + " quarters, " + str(loonies) + " loonies, and " + str(toonies) + " toonies.") 
