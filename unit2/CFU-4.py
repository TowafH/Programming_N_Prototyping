# 9/23/24
# PD 1-2
# Towaf Hossain

import math

user_name = input("What is your name?")
print("Welcome to the Quadratic Formula Calculator! \n")
a = int(input("Enter a-value"))
b = int(input("Enter b-value"))
c = int(input("Enter c-value"))
print("Quadratic Formula Entered: " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + "\n")
x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
print(user_name + ", Here is your answer!")
print("x1 =", x1, "\n" + "x2 =", x2)
