import simplegui

def draw_handler(canvas):
    #canvas.draw_point([x,y], "color")
    canvas.draw_point([100,100], "Red")
    #canvas.draw_line([x1,y1],[x2,y2], line_width, "color")
    canvas.draw_line([50,50],[150,150], 20, "Purple")

# Code to Modify the Frame
    # Creates the frame w/ Title & Dimensions
frame = simplegui.create_frame("CFU 15 - Happy Shapes", 200, 200)
    # Modify the background color of the frame
frame.set_canvas_background("White")                         
    # Set the draw handler
frame.set_draw_handler(draw_handler)


# Nothing will run until we .start() the frame
frame.start()
