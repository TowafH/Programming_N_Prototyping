# Towaf Hossain
# PD 1-2
# 11/30/24

import simplegui

def draw_handler(canvas):
    canvas.draw_polygon([(70, 60), (75, 50), (85, 50), (90, 60), (85, 70), (75, 70)], 2, "Black") # Eye 1
    canvas.draw_polygon([(110, 60), (115, 50), (125, 50), (130, 60), (125, 70), (115, 70)], 2, "Black") # Eye 2
    canvas.draw_polygon([(95, 75), (105, 80), (95, 90)], 2, "Black")  # Nose
    canvas.draw_polygon([(75, 100), (100, 125), (125, 100)], 2, "Black")  # Mouth

# Code to Modify the Frame
frame = simplegui.create_frame("CFU 15 - Happy Shapes", 200, 200)
frame.set_canvas_background("White")                         
frame.set_draw_handler(draw_handler)
frame.start()
