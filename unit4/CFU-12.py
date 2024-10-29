# 10/29/24
# PD 1-2
# Towaf Hossain

password = "simonsnyc"

guess = input("Enter a Password")

while guess != password:
    print("Wrong Password!")
    guess = input("Enter a Password!")
    if guess == password:
        print("Correct! You May Enter!")
