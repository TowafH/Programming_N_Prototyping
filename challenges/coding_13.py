import turtle
import math

def iso(T, r, angle):
  y = r * math.sin(math.radians(angle))
  T.rt(angle)
  T.fd(r)
  T.lt(90 + angle)
  T.fd(y * 2)
  T.lt(90 + angle)
  T.fd(r)
  T.lt(180 - angle)

def pie(T, r, n):
  angle = 360 / n
  for i in range(n):
    iso(T, r, angle / 2)
    T.lt(angle)

def pies(T, r, n):
  pie(T, r, n)
  T.pu()
  T.fd(r * 2 + 10)
  T.pd()


T = turtle.Turtle()
pies(T, 10, 5)
pies(T, 10, 6)
pies(T, 10, 7)
pies(T, 10, 8)
