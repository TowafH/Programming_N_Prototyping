# https://trinket.io/turtle/6febe4578276
# Towaf Hossain
# PD 1-2
# 3/14/25
# PY-Challenge 7


import turtle

# Base Code
def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.forward(length*n)
    t.left(angle)
    draw(t, length, n-1)
    t.right(2*angle)
    draw(t, length, n-1)
    t.right(angle)
    t.backward(length*n)

# Forward Function w/ turtle and number as parameters
def fd(t, n, length):
  t.forward(length * n)

# Left Function w/ turtle and number as parameters
def lt(t, n, length):
  t.left(length * n)

# Square function
# Added new angle and length parameter
def square(t, angle, length):
  for i in range(4):
    fd(t, angle, length)
    lt(t, angle, length)

# Setup screen
screen = turtle.Screen
# Create the Turtle
t = turtle.Turtle()
# Base Speed
t.speed(0)

# Function calls
draw(t, 10, 5)

# Create bob variable to pass as an argument
bob = turtle.Turtle()
square(bob, 90, 2)

screen.mainloop
