# 10/10/24
# PD 1-2
# Towaf Hossain
# CFU-7 Functions+Math

'''
Create a program that asks the user for three numbers.The main program should send those three numbers as arguments to a function to calculates and prints 
“The sum of your three numbers is:  XXX”

The main program should then send those same numbers to a second function which calculates and prints 
“The average of your three numbers is:  XXX”
'''


print("Welcome to the Addition & Average Calculator!\n")

def calculate_addition(x1, x2, x3):
    sum = x1 + x2 + x3
    print("Addition:", x1, "+", x2, "+", x3)
    print("The sum of your three numbers is:", sum, "\n")
    return sum

def calculate_average(sum):
    average = sum / 3
    print("Average Calculation:", sum, "/ 3")
    print("The average of your three numbers is:", average)
    return average

# User input
num1 = int(input("Enter a Number:"))
num2 = int(input("Enter a Number:"))
num3 = int(input("Enter a Number:"))

# Calculate Sum
sum = calculate_addition(num1, num2, num3)

# Calculate Average
calculate_average(sum)
