# Towaf Hossain
# PD 1-2
# 12/12/24
# Animation of a city scape during christmas. There are christmas trees, snowflakes, and a snowman in the drawing.

import simplegui

y1 = 250  # Start value for the sun's position

def draw_handler(canvas):
    def sun():
        global y1
        if y1 > 100: 
            y1 -= 1
        canvas.draw_circle((300, y1), 25, 2, "Black", "LightGray")
    
    def horizon():
        canvas.draw_line((0, 300), (600, 300), 1, "Black")
    
    def street():
        canvas.draw_polygon([(0, 600), (200, 300)], 1, "Black")  # Left Street
        canvas.draw_polygon([(20, 600), (210, 300)], 1, "Black")
        canvas.draw_polygon([(600, 600), (400, 300)], 1, "Black")  # Right Street
        canvas.draw_polygon([(580, 600), (390, 300)], 1, "Black")
    def skyscraper():
        canvas.draw_polygon([(100, 450), (100, 200), (0, 200), (0, 450)], 1, "Red") # Far Frame
        canvas.draw_polygon([])
    sun()
    horizon()
    street()
    skyscraper()

frame = simplegui.create_frame("Christmas St.", 600, 600)
frame.set_canvas_background("White")
frame.set_draw_handler(draw_handler)
frame.start()
