# Towaf Hossain
# PD 1-2
# 11/25/24
# CFU 13 - Happy Dots w/ simplegui

import simplegui

def draw_handler(canvas):
    # Function to handle drawings
    
    # Draw a point
    # canvas.draw_point([x,y], "color")

    # Smiley mouth
    canvas.draw_point([92,96], "rgb(4, 106, 56)")
    canvas.draw_point([94,98], "rgb(4, 106, 56)")

    canvas.draw_point([96,100], "rgb(4, 106, 56)")
    canvas.draw_point([98,100], "rgb(4, 106, 56))")
    canvas.draw_point([100,100], "rgb(4, 106, 56)")
    canvas.draw_point([102,100], "rgb(4, 106, 56)")
    canvas.draw_point([104,100], "rgb(4, 106, 56)")

    canvas.draw_point([106,98], "rgb(4, 106, 56)")
    canvas.draw_point([108,96], "rgb(4, 106, 56)")

    # Smiley Eyes
    canvas.draw_point([95, 85], "rgb(4, 106, 56)")
    canvas.draw_point([105, 85], "rgb(4, 106, 56)")

    # C
    canvas.draw_point([29,23], "rgb(4, 106, 56)")
    canvas.draw_point([27,23], "rgb(4, 106, 56)")
    canvas.draw_point([25,24], "rgb(4, 106, 56)")
    canvas.draw_point([25,26], "rgb(4, 106, 56)")
    canvas.draw_point([25,28], "rgb(4, 106, 56)")
    canvas.draw_point([25,30], "rgb(4, 106, 56)")
    canvas.draw_point([27,32], "rgb(4, 106, 56)")
    canvas.draw_point([29,32], "rgb(4, 106, 56)")


    # R
    canvas.draw_point([39,23], "rgb(4, 106, 56)")
    canvas.draw_point([37,23], "rgb(4, 106, 56)")
    canvas.draw_point([35,23], "rgb(4, 106, 56)")
    canvas.draw_point([35,25], "rgb(4, 106, 56)")
    canvas.draw_point([35,27], "rgb(4, 106, 56)")
    canvas.draw_point([35,29], "rgb(4, 106, 56)")
    canvas.draw_point([35,31], "rgb(4, 106, 56)")
    canvas.draw_point([35,23], "rgb(4, 106, 56)")

    # 7 
    canvas.draw_point([45,23], "rgb(4, 106, 56)")
    canvas.draw_point([47,23], "rgb(4, 106, 56)")
    canvas.draw_point([49,23], "rgb(4, 106, 56)")
    canvas.draw_point([48,25], "rgb(4, 106, 56)")
    canvas.draw_point([47,27], "rgb(4, 106, 56)")
    canvas.draw_point([46,29], "rgb(4, 106, 56)")
    canvas.draw_point([45,31], "rgb(4, 106, 56)")

    

# Create a Frame
frame = simplegui.create_frame("CFU #13 - Happy Dots", 200, 200)
# Background Color
frame.set_canvas_background("White")
# Draw Handler
frame.set_draw_handler(draw_handler)

# Initialize the Frame
frame.start()
    
