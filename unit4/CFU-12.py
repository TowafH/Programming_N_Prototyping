# 10/30/24
# PD 1-2
# Towaf Hossain
 
#V1
def version1():
    password = "simonsnyc"
    user_guess = input("Enter the Password")
    
    while user_guess != password:
        print("Wrong Password")
        user_guess = input("Enter a Password")
    print("Correct! You May Enter!")

#V2
def version2():
    password = "simonsnyc"
    user_guess = ""
    num_guess = 0

    while user_guess != password and num_guess < 3:

        user_guess = input("Enter a Password!")
        num_guess += 1

        if user_guess == password:
            print("Correct, You may enter!")
        elif num_guess == 3:
            print("You didn't get it in 3 tries! Try Again Later!")
        else:
            print(f"Wrong Password - Try: #{num_guess}")

# Give user the option to choose which version
version = int(input("Which version would you like to play | 1 or 2 |"))

if version == 1:
    version1()
elif version == 2:
    version2()
