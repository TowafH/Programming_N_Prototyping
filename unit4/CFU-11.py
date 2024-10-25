
# 10/25/24
# PD 1-2
# Towaf Hossain

'''
1) Using For Loop create a program that prints out the numbers: 10, 20, 30, 40, 50 up to 70
2) Using For Loop create a program that prints out the numbers:
'''


def function1():
    print("Our Program prints the numbers 10-70 in steps of 10!")
    for i in range(10, 71, 10):
        print(f"x = {i}")
        
def function2():
    print("Our Program prints the number 0.5-10 in steps of 0.5!")
    for i in range(0, 21):
        i = i / 2
        print(f"x = {i}")
        
def function3():
    print("")

question = int(input("Which function do you want to be ran? || Type 1, 2, or 3 ||"))

if question == 1:
    function1()
elif question == 2:
    function2()
elif question == 3:
    function3()
else:
    while True:
        question = int(input("You typed wrong! Try Again || Type 1, 2, or 3 ||"))
