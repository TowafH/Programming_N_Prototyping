# Towaf Hossain
# PD 1-2

import turtle

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

# Setup screen
screen = turtle.Screen()

# Create the Turtle
t = turtle.Turtle()
# Base Speed
t.speed(0)

# Test the polygon function with various n values
bob = turtle.Turtle()
bob.color("red")
lt(bob, 60)
fd(bob, 50)
bob.backward(100)
fd(bob, 50)
lt(bob, 50)
fd(bob, 50)
bob.backward(100)
fd(bob, 50)
lt(bob, 60)
fd(bob, 50)
bob.backward(100)
lt(bob, 60)
fd(bob, 50)
lt(bob, -55)
fd(bob, 50)
rt(bob, 65)
fd(bob, 55)
rt(bob, 60)
fd(bob, 50)
rt(bob, 55)
fd(bob, 50)
rt(bob, 65)
fd(bob, 60)
screen.mainloop()
