# 10/2/24
# PD 1-2
# Towaf Hossain

import math
import random

print("Welcome to the Random Number calculator")
print("Our calculator can generate a random number between 1 and 100\n")

user_randomNum = int(input("Enter a Number"))
gen_randomNum = 64

sum = gen_randomNum + user_randomNum
difference = gen_randomNum - user_randomNum
product = gen_randomNum * user_randomNum
quotient = gen_randomNum / user_randomNum
remainder = gen_randomNum % user_randomNum
square_root = math.sqrt(gen_randomNum)
power = math.pow(user_randomNum, gen_randomNum)

print("Results:")
print("Random Number: " + str(gen_randomNum))
print("Your Number: " + str(user_randomNum))
print(f"\nSum: {gen_randomNum} + {user_randomNum} = {sum}")
print(f"Difference: {gen_randomNum} - {user_randomNum} = {difference}")
print(f"Product: {gen_randomNum} * {user_randomNum} = {product}")
print(f"Quotient: {gen_randomNum} / {user_randomNum} = {quotient}")
print(f"Remainder: {gen_randomNum} % {user_randomNum} = {remainder}")
print(f"Square Root of Random Number: sqrt({gen_randomNum}) = {square_root}")
print(f"Your Number to the Power of Random Number: {user_randomNum}^{gen_randomNum} = {power}")
