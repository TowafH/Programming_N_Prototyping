# Towaf Hossain
# PD 1-2
# 11/25/24
# CFU 14 - Happy Dots w/ simplegui but lines

import simplegui

def draw_handler(canvas):
    # Function to handle drawings

    # Draw a line
    # canvas.draw_line[point1], [point2], line_width, line_color
    # canvas.draw_line[x1, y1], [x2, y2], line_width, line_color
    canvas.draw_line([50,25], [75,25], 5, "Red") # Left Eye
    canvas.draw_line([120,25], [145,25], 5, "Red") # Right Eye

    canvas.draw_line([90,50],[110,60], 5, "Green") # Nose Top
    canvas.draw_line([110,60],[90,70],5, "Green")

    canvas.draw_line([150, 100], [175, 65], 5, "Purple") # Right Line up
    canvas.draw_line([50, 100], [150, 100], 5, "Purple") # Mouth Line
    canvas.draw_line([50, 100], [25, 75], 5, "Purple") # Left Line up
   

# Create a Frame
frame = simplegui.create_frame("Python Drawing", 200, 200)

# Background Color
frame.set_canvas_background("White")

# Draw Handler
frame.set_draw_handler(draw_handler)

# Initialize the Frame
frame.start()
    
