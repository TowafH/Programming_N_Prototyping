# 9/30/24
# PD 1-2
# Towaf Hossain

'''
Task:
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

# Recieve Input
print("Welcome to the Loony Bank of Canada, We can calculate how many coins and loonies you have!\n")
penny = int(input("How many pennies do you have?"))
nickel = int(input("How many nickels do you have?"))
dime = int(input("How many dimes do you have?"))
quarter = int(input("How many quarters do you have"))
loonies = int(input("How many loonies do you have?"))
toonies = int(input("How many toonies do you have?"))

# Cents Conversion
penny_in_cents = penny * 1
nickel_in_cents = nickel * 5
dimes_in_cents = dime * 10
quarters_in_cents = quarter * 25
loonies_in_cents = loonies * 100
toonies_in_cents = toonies * 200

# Total Amount Of Money
total_cents = penny_in_cents + nickel_in_cents + dimes_in_cents + quarters_in_cents + loonies_in_cents + toonies_in_cents
total_value = total_cents / 100




totalDollars = total_value // 1 #Gives the Total Whole $
print(totalDollars)
change = total_value - totalDollars
change_quarter = (change) % 4

inQurts = int(change*4)
inDimes = int(change*10) - inQurts
inNickels = int(change*20) - (inDimes*2) 
inCents = int(change*100) - (inNickels*5) - (inDimes*10)
print(f"Your total is : ${totalDollars}, {inQurts} Quarters, {inDimes} Dimes, {inNickels} Nickels, {inCents} Cents")
# i.e: 13.67 or 13$ and 2 quarters, 1 dime, 1 nickel, 2 cents


# Print the money and display the amount of each
# print("You have a total of $" + str(totalDollars) + "\n\nYou had " + str(penny) + " pennies, " + str(nickel) + " nickels, " + str(dime) + " dimes, " + str(quarter) + " quarters, " + str(loonies) + " loonies, and " + str(toonies) + " toonies.") 
