import math

user_name = input("What is your name?")
a = int(input("Enter a-value"))
b = int(input("Enter b-value"))
c = int(input("Enter c-value"))
top_of_quadratic = (-b + math.sqrt(b**2 - 4(a*c)))
bottom_of_quadratic = 2*a

x = top_of_quadratic / bottom_of_quadratic
print(x)
