# 10/30/24
# PD 1-2
# Towaf Hossain
# CFU 12 While Loops
'''
Version 1:
-Write a program that asks the user for the password.
-The Password should initially be set to “simonsnyc”
-It keeps asking them for the password until they get it correct.
-For the incorrect password, it should say “Wrong Password!)
-For correct password it should say “Correct! You may enter….”
-And then it ends the program

Version 2 : 
Modify Version 1 so that the User gets only 3 chances.
 HINTS:  Use a variable to keep track of the number of guesses.
The User is stuck in the While loop as long as num_guesses < 3 and guess != PW
''' 


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
