a_side = int(input("Enter side A: "))
b_side = int(input("Enter side B: "))
c_side = int(input("Enter side C: "))
d_side = int(input("Enter side D: "))
e_side = int(input("Enter side E: "))

# Bottom Rectangle Area = Length * Width
b_rectangle_area = c_side * b_side

# Middle Rectangle Area = Length * Width
m_rectangle_length = a_side - c_side
m_rectangle_width = d_side - e_side
m_rectangle_area = m_rectangle_length * m_rectangle_width

# Triangle Area = 0.5 * base * height
triangle_area= 0.5 * e_side * m_rectangle_length

total_area = b_rectangle_area + m_rectangle_area + triangle_area
print("Room Area: " + str(total_area))
