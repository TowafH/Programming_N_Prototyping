import random


print("Welcome to the Guessing Game!\n")
rolls = int(input("How many rolls do you want?"))
score = 0

# Use a while loop until there are no more rolls left
while rolls > 0:
    # Generate a Random Number
    random_number = random.randint(1,6)
    guess = int(input("Guess the Number between 1-6"))
    
    # Conditonal Statement
    if guess == random_number:
        score += 6
        print(f"You guessed {random_number} correctly! You gained 6 points")
    elif guess != random_number:
        score -= 1
        print(f"You guessed {random_number} incorrectly! You lost 1 point.")
    else:
        print("Your guess is out of the 1-6 range!")
    rolls -= 1
    
print(f"\nYour final score: {score}")
