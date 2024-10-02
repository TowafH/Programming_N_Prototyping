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
print("Total $",total_value)


totalDollars = total_value // 1  # Get the whole dollars
print("Whole #: $", int(totalDollars))

total_change = total_value - totalDollars  # Get the change amount
print("Change Amount: $", format(total_change, '.2f'))  # 0.67

# Convert the change amount to cents
change_in_cents = int(total_change * 100)

# Calculate the number of each coin type
inQuarts = change_in_cents // 25  # Number of quarters
remaining_cents = change_in_cents % 25  # Remaining cents after quarters

inDimes = remaining_cents // 10  # Number of dimes
remaining_cents = remaining_cents % 10  # Remaining cents after dimes

inNickels = remaining_cents // 5  # Number of nickels
inCents = remaining_cents % 5  # Remaining cents after nickels

# Display 
print("Quarters:", inQuarts) 
print("Dimes:", inDimes)       
print("Nickels:", inNickels)   
print("Cents:", inCents)
print(f"You have a total of ${total_value:.2f}. You had {penny} pennies, {nickel} nickels, {dime} dimes, {quarter} quarters, {loonies} loonies, and {toonies} toonies.")

