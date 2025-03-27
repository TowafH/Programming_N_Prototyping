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

def fd(t, n):
    t.forward(n)

def lt(t, n = 90):
    t.left(n)

def rt(t, n = 90):
    t.right(n)
    
def arc(t, r, angle):
    arc_length = int(2 * math.pi * r * (angle / 360))
    n = arc_length // 3
    step_length = arc_length // n
    step_angle = angle // n

    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

bob = turtle.Turtle()
for i in range(10):
  bob.color("blue")
  bob.circle(50)
  bob.left(60)
  bob.forward(30)

screen.mainloop()
