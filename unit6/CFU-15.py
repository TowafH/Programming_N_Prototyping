import simplegui

def draw_handler(canvas):
    #canvas.draw_polygon([(x1, y1), (x2,y2), (x3,y3)], line_width, "color")
    canvas.draw_polygon([(80, 50), (80,75), (80,50)], 2, "Black") # Eye1
    canvas.draw_polygon([(120, 50), (120,75), (120,50)], 2, "Black") # Eye2
    canvas.draw_polygon([(95,75), (105,80), (95, 90)], 2, "Black") # Nose
    canvas.draw_polygon([(75, 100), (100,125), (125,100)], 2, "Black") # Mouth

# Code to Modify the Frame
    # Creates the frame w/ Title & Dimensions
frame = simplegui.create_frame("CFU 15 - Happy Shapes", 200, 200)
    # Modify the background color of the frame
frame.set_canvas_background("White")                         
    # Set the draw handler
frame.set_draw_handler(draw_handler)


# Nothing will run until we .start() the frame
frame.start()
