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
else:
    # If the above conditon is false, then run this
    print("NO?! SO who is cooking!")
