# Challenge 1
print("--- Challenge 1 ---")
length = int(input("Enter a Length: "))
width = int(input("Enter a Width: "))
total_length_width = length + width
P = 2 * total_length_width
print("Perimeter of a " + str(length) + " x " + str(width) + " rectangle is " + str(P))

# Challenge 2
print("\n--- Challenge 2 ---")
f_temp = int(input("Enter Fahrenheit Temperature: "))
sub_f = f_temp - 32
celsius = sub_f * 5/9
print(str(f_temp) + "°F is " + str(celsius) + "°C")

# Challenge 3
print("\n--- Challenge 3 ---")
vert_velo = int(input("Enter Vertical Velocity: "))
time = int(input("Enter Time: "))
accel_grav = int(input("Enter Acceleration Gravity: "))
vert_time = vert_velo * time
accel_time = accel_grav * time ** 2
v_distance = vert_time - 1/2 * accel_time
print("Vertical Distance is " + str(v_distance))

# Challenge 4
print("\n--- Challenge 4 ---")
x1 = int(input("Enter first X-value: "))
y1 = int(input("Enter first Y-value: "))
x2 = int(input("Enter second X-value: "))
y2 = int(input("Enter second Y-value: "))
x_coords = x2 - x1
y_coords = y2 - y1
x_squared = x_coords ** 2
y_squared = y_coords ** 2
x_and_y = x_coords + y_coords
distance = x_and_y ** 0.5
print("The distance is " + str(distance))
