import turtle

def draw_spiral(t, n, length, a, b):
  """
  Arguments:
    n: how many line segments to draw
    length: how long each segment is
    a: how loose the initial spiral starts out (larger is looser)
    b: how loosely coiled the spiral is (larger is looser)
    """
  angle_thetha = 0.0  
  for i in range(n):
    t.forward(length)  
    angle_dtheta = 1 / (a + b * angle_thetha)  
    t.left(angle_dtheta)  
    angle_thetha += angle_dtheta  

cr7 = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("yellow")
cr7.speed(0)
cr7.pencolor("red")

draw_spiral(cr7, 10, 20, 2, 0.1)

screen.exitonclick()
