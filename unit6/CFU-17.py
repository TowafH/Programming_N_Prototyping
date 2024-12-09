# Towaf Hossain
# PD 1-2
# 12/9/24

import simplegui

# Frame Size
frame_width = int(input("Enter Width: "))
frame_height = int(input("Enter Height: "))  # Fixed input prompt

frame = None

# Shape Visibility
show_circle = True
show_square = True
show_triangle = True
show_ellipse = True

def draw_circle(canvas, cx, cy, size):
    half_size = size / 2
    canvas.draw_circle((cx,cy), half_size, 2, "#f25022", "#f25022")

def draw_square(canvas, cx, cy, size):
    half_size = size / 2
    canvas.draw_polygon([(cx - half_size, cy - half_size),
                         (cx + half_size, cy - half_size),
                         (cx + half_size, cy + half_size),
                         (cx - half_size, cy + half_size)],
                         half_size, "#7fba00", "#7fba00")

def draw_triangle(canvas, cx, cy, size):
    half_size = size / 2
    canvas.draw_polygon([(cx, cy - half_size),  # Top vertex
                         (cx - half_size, cy + half_size),  # Bottom-left vertex
                         (cx + half_size, cy + half_size)],  # Bottom-right vertex
                         half_size, "#00a4ef", "#00a4ef")

    
def draw_ellipse(canvas, cx, cy, size):
    half_size = size / 2
    canvas.draw_polygon([(cx, cy + half_size),
                        (cx + half_size, cy - half_size),
                        (cx - half_size, cy - half_size),
                        (cx - half_size, cy - half_size)],
                        half_size, "#ffb900", "#ffb900")
    
def draw(canvas):
    # Calculate Quadrants
    quadrant_width = frame_width / 2
    quadrant_height = frame_height / 2
    
    # Toggle Each Quadrant
    if show_circle:
        draw_circle(canvas, quadrant_width * 0.5, quadrant_height * 0.5, 25)  # Top-left Circle

    if show_square:
        draw_square(canvas, quadrant_width * 1.5, quadrant_height * 0.5, 25)  # Top-right Square

    if show_triangle:
        draw_triangle(canvas, quadrant_width / 2, quadrant_height * 1.5, 25)  # Bottom-left Triangle
        
    if show_ellipse:
        draw_ellipse(canvas, quadrant_width * 1.5, quadrant_height * 1.5, 25) # Bottom-right ellipse


# Button Handlers
def toggle_triangle():
    global show_triangle
    show_triangle = not show_triangle

def toggle_square():
    global show_square
    show_square = not show_square

def toggle_circle():
    global show_circle
    show_square = not show_circle
   
def toggle_ellipse():
    global show_ellipse
    show_ellipse = not show_ellipse


# Frame Creation
def create_frame():
    global frame
    frame = simplegui.create_frame("Shape Drawing w/ Toggles", frame_width, frame_height)
    frame.set_draw_handler(draw)
    
    frame.add_button("Toggle Circle", toggle_circle, 150)
    frame.add_button("Toggle Square", toggle_square, 150)
    frame.add_button("Toggle Triangle", toggle_triangle, 150)
    frame.add_button("Toggle Ellipse", toggle_ellipse, 150)
    frame.start()

create_frame()
