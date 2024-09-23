import math

# Calculating the Radius of a Circle
r = int(input("What is the radius of your circle?"))
C = 2*r*math.pi
A = math.pi*r**2
print("Circumference=", C, "\n" + "Area=", A)

# Calculating the Volume of a Cylinder
radius = float(input("What is the radius of your cylinder"))
height = int(input("What is the height of your cylinder"))
volume = math.pi * radius ** 2 * height
print("Volume of the Cylinder:", int(volume))
