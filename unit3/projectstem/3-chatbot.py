import random

user_name = input("What is your first name?")
if user_name == "Towaf":
    print("I like that name!")
else:
    print("That's a nice name")
    
user_shoe = input("What shodes do you like?")
randomShoe = random.randint(1,3)
if randomShoe == 1:
    print("Nice choice of shoes!")
elif randomShoe == 2:
    print("I like those shoes too!")
else:
    print("I don't like those shoes.")
    
user_age = int(input("How old are you?"))
if user_age > 65:
    print("You're a senior")
elif user_age > 18:
    print("You're adult")
else:
    print("You're a minor")
    
user_shirt = input(f"So {user_name}, What's your favorite shirt?")
if user_shirt == "T-Shirts":
    print("I like T-shirts too!")
elif user_shirt == "Jerseys":
    print("I like to wear Jerseys too!")
else:
    print("I like your style")
    
user_pants = input(f"So {user_name}, What's your favorite pants?")
if user_pants == "Jeans":
    print("I like Jeans too!")
elif user_pants == "Shorts":
    print("I like to wear Shorts too!")
else:
    print("I like your style")
    
user_bye = input(f"Anything else you'd like to say")
if user_bye == "Goodbye":
    print("Bye!")
else:
    print("It was nice meeting you!")
