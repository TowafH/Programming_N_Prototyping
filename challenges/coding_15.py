import turtle

def koch_curve(t, length):
    if length < 3:
        t.forward(length)
        return
    
    length = length / 3
    koch_curve(t, length)
    t.left(60)
    koch_curve(t, length)
    t.right(120)
    koch_curve(t, length)
    t.left(60)
    koch_curve(t, length)

def draw_snowflake(t, length):
    for i in range(3):
        koch_curve(t, length)
        t.right(120)

cristiano = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("white")
cristiano.speed(0)
cristiano.pencolor("blue")

cristiano.penup()
cristiano.goto(-150, 100)
cristiano.pendown()

draw_snowflake(cristiano, 300)

screen.exitonclick()
