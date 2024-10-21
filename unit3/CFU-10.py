# Towaf Hossain
# PD 1-2
# 10/21/24


import random

def game():
    random_num = random.randint(1, 10)
    attempts = 0

    while True:
        user_guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1
        
        if user_guess == random_num:
            print(f"Correct! It took you {attempts} attempts.")
            break
        elif user_guess > random_num:
            print("The guess was Too High!")
        elif user_guess < random_num:
            print("The guess was Too Low!")

game()
