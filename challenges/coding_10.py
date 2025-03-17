# Towaf Hossain
# PD 1-2

import turtle
import math

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.forward(length * n)
    t.left(angle)
    draw(t, length, n - 1)
    t.right(2 * angle)
    draw(t, length, n - 1)
    t.right(angle)
    t.backward(length * n)

# Forward Function w/ turtle and number as parameters
def fd(t, n):
    t.forward(n)

# Left Function w/ turtle and number as parameters
def lt(t, n = 90):
    t.left(n)

# Right Function w/ turtle and number as parameters
def rt(t, n = 90):
    t.right(n)

# Square function
def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

# Polygon function
def polygon(t, length, n):
    angle = 360 / n
    for i in range(n):
        fd(t, length)
        lt(t, angle)

# Circle function
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

# Setup screen
screen = turtle.Screen()

# Create the Turtle
t = turtle.Turtle()
# Base Speed
t.speed(0)

# Test the polygon and circle functions with various values
bob = turtle.Turtle()
circle(bob, 50)       # Circle with radius 50
circle(bob, 100)      # Circle with radius 100

screen.mainloop()
