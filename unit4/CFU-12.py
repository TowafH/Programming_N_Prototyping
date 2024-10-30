# 10/29/24
# PD 1-2
# Towaf Hossain

password = "simonsnyc"
guess = ""
num_guess = 0

while guess != password and num_guess < 3:

    guess = input("Enter a Password!")
    num_guess += 1

    if guess == password:
        print("Correct, You may enter!")
    elif num_guess == 3:
        print("You didn't get it in 3 tries! Try Again Later!")
    else:
        print(f"Wrong Password - Try: #{num_guess}")
