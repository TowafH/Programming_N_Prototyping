# 10/15/24
# PD 1-2
# Towaf Hossain
# CFU - 8 GrubHub App
'''
GrubHub Program - 

First ask the user if they ordered delivery

Version 1
- If the user responds “yes” - say great!If the user responds with anything else say: “NO?! So who is cooking?”

Version 2 
- Builds on ver1If the user responds “yes….
- Ask the user the cost of the food ordered
- Ask the user how many people are splitting the order
- Calculate and print out the cost per person
Ex: “The cost per person is $2.50
'''

print("Welcome to our delivery App!")
delivery = input("Did you order delivery?")

# Conditonal Statement
if delivery == "Yes" or delivery == "yes":
    # Commands to run within the statement
    print("Great! You will be ordering delivery\n")
    cost = float(input("What is the total cost of the ordered food?"))
    people = int(input("How many people are splitting the order"))
    average_cost = cost / people 
    print(f"The total cost of the order is: ${cost}")
    print(f"You're splitting the order with {people} people\n")
    print(f"The cost per person is ${average_cost}")
    # We can do ${average_cost:.2f} to recieve only 2 decimal places
else:
    # If the above conditon is false, then run this
    print("NO?! SO who is cooking!")
