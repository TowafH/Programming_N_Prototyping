#Towaf Hossain
#PD 1-2
#10/22/24

import time
import random

# Inputs
rounds = int(input("How many rounds do you want to play? "))
difficulty = input("Pick the Difficulty: 1-10 || 1-50 || 1-1000 ")

# Generate a random number based on the gamemode
if difficulty == "1-10":
    random_num = random.randint(1, 10)
elif difficulty == "1-50":
    random_num = random.randint(1, 50)
elif difficulty == "1-1000":
    random_num = random.randint(1, 1000)
else:
    print("Invalid gamemode selected.")
    


def game(rounds, random_num, difficulty):
    # Initialize Variables
    attempts = 0
    total_time = 0

    while rounds > 0:
        attempts += 1
        
        # Variables for Time
        start_time = time.time()
        user_guess = int(input(f"Guess a number between {difficulty}: "))
        end_time = time.time()
        
        # Time Calculation
        time_taken = end_time - start_time
        total_time += time_taken
        
        if user_guess == random_num:
            print(f"Correct! It took you {attempts} attempts.")
            print(f"Total time taken: {total_time:.2f} seconds")
            return  # Exit after a correct guess
        elif user_guess < random_num:
            print("Too Low!")
        else:
            print("Too High!")
        
        rounds -= 1
        
        if rounds == 0:
            print(f"Game over! The number was {random_num}. You took {attempts} attempts.")
            print(f"Total time taken: {total_time:.2f} seconds")

game(rounds, random_num, difficulty)
