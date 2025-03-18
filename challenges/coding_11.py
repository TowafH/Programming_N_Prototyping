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
    angle = 360 // n
    for i in range(n):
        fd(t, length)
        lt(t, angle)

# Circle function
def circle(t, r):
    circumference = int(2 * math.pi * r)
    n = 50  # More sides for smoother circle
    length = circumference // n
    polygon(t, length, n)

# Arc function
def arc(t, r, angle):
    arc_length = int(2 * math.pi * r * (angle / 360))
    n = arc_length // 3
    step_length = arc_length // n
    step_angle = angle // n

    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)

# Setup screen
screen = turtle.Screen()

# Create the Turtle
t = turtle.Turtle()
# Base Speed
t.speed(0)

# Test the polygon, circle, and arc functions with various values
bob = turtle.Turtle()
arc(bob, 50, 180)     # Half circle
arc(bob, 100, 270)    # Three-quarter circle

screen.mainloop()
