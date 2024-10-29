# 10/29/24
# PD 1-2
# Towaf Hossain

password = "simonsnyc"
guess = ""
num_guess = 0

while guess != password and num_guess != 3:

    guess = input("Enter a Password!")
    num_guess += 1

    if guess == password:
        print("Correct, You may enter!")
    elif num_guess == 3:
        print("Incorrect, You may not enter!")
    else:
        print("Wrong Password")
