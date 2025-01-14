import simplegui

def draw(canvas):
    # Function to handle drawings
    pass

# Create a Frame
frame = simplegui.create_frame("CFU #13 - Happy Dots", 800, 800)
# Background Color
frame.set_canvas_background("White")
# Draw Handler
frame.set_draw_handler(draw)
# Initialize the Frame
frame.start()
    
