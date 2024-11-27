# Towaf Hossain
# PD 1-2
# 11/27/24

import simplegui

def draw_handler(canvas):
    #canvas.draw_circle((center), radius, line_width, "color")
    canvas.draw_circle((100, 100), 50, 5, "Black")

# Code to Modify the Frame
    # Creates the frame w/ Title & Dimensions
frame = simplegui.create_frame("Happy Circles", 200, 200)
    # Modify the background color of the frame
frame.set_canvas_background("White")                         
    # Set the draw handler
frame.set_draw_handler(draw_handler)


# Nothing will run until we .start() the frame
frame.start()
