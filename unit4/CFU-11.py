# 10/25/24
# PD 1-2
# Towaf Hossain

'''
1) Using For Loop Create a program that prints out the numbers:  10, 20, 30, 40, 50 up to 70
2)  Using For Loop create a program that prints out the numbers: 0, 0.5 , 1 , 1.5, 2 ….   up to 10.0
3)  Sing the 99 bottles of beer song
'''


def integers_to_10():
    print("Our Program prints the numbers 10-70 in steps of 10!")
    for i in range(10, 71, 10):
        print(f"x = {i}")
        
def decimals_to_10():
    print("Our Program prints the number 0.5-10 in steps of 0.5!")
    for i in range(0, 21):
        i = i / 2
        print(f"x = {i}")
        
def bottles_of_beer():
    for i in range (99, 0, -1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer\nTake one down and pass it around, {i - 1} bottles of beer on the wall\n")
        if i == 1:
            print(f"No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some, 99 bottles on beer on the wall.")

question = int(input("Which function do you want to be ran? || Type 1, 2, or 3 ||"))

if question == 1:
    integers_to_10()
elif question == 2:
    decimals_to_10()
elif question == 3:
    bottles_of_beer()
else:
    while True:
        question = int(input("You typed wrong! Try Again || Type 1, 2, or 3 ||"))
