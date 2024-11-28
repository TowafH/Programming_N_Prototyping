# Towaf Hossain
# PD 1-2
# 11/27/24
# CFU 16 - Happy Circles


import simplegui

def draw_handler(canvas):
    #canvas.draw_circle(centerXY, radius, line_width, color)
    canvas.draw_circle((100,100), 75, 2, "Red") # Face
    canvas.draw_circle((75,75), 10, 2, "Black") # Left Eye
    canvas.draw_circle((125,75), 10, 2, "Black") # Right Eye
    canvas.draw_circle((100,100), 5, 2, "Black") # Nose
    canvas.draw_circle((75,119), 3, 2, "Black") # Mouth1
    canvas.draw_circle((80,125), 3, 2, "Black") # Mouth2
    canvas.draw_circle((88,125), 3, 2, "Black")
    canvas.draw_circle((94,125), 3, 2, "Black")
    canvas.draw_circle((100,125), 3, 2, "Black")
    canvas.draw_circle((106,125), 3, 2, "Black")
    canvas.draw_circle((112,125), 3, 2, "Black")
    canvas.draw_circle((118,120), 3, 2, "Black")


# Store frame in frame variable
frame = simplegui.create_frame("CFU 16 - Happy Circles", 200, 200)
# Background Color
frame.set_canvas_background("White")
# Set the draw handler
frame.set_draw_handler(draw_handler)
#Initialize Frame
frame.start()
