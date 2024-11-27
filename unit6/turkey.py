# Towaf Hossain
# PD 1-2
# 11/27/24

import simplegui

def draw_handler(canvas):
    turkey_color = "#C9592E"

    #canvas.draw_point([x,y], "color")
    #canvas.draw_line([x1,y1],[x2,y2], line_width, "color")
    #canvas.draw_polygon([(x1, y1), (x2,y2), (x3,y3)], line_width, "color")
    #canvas.draw_circle((x1, y1), radius, line_width, "color")

    canvas.draw_circle((100, 100), 50, 2, turkey_color, turkey_color) # Turkey Body


# Code to Modify the Frame
    # Creates the frame w/ Title & Dimensions
frame = simplegui.create_frame("Thanksgiving Motif", 200, 200)
    # Modify the background color of the frame
frame.set_canvas_background("White")                         
    # Set the draw handler
frame.set_draw_handler(draw_handler)


# Nothing will run until we .start() the frame
frame.start()
