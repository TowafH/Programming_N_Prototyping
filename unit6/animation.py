# Towaf Hossain
# PD 1-2
# 12/12/24
# Animation of a cityscape during christmas season. There are buildings, christmas trees, snowflakes, and sidewalks


import simplegui
import random

width = 600
height = 600

# Global Variables for Moon
y1 = 250

# Global Variables for snowflakes
snow_flakes = 5
snowfall_speed = 0.5


def draw_handler(canvas):
    def snowflakes():
        global width
        global height
        
        global snowflakes
        global snowfall_speed
        global snow_y
        
        canvas.draw_polygon([(0,0), (width, 0), (width, height / 2), (0, height / 2)], 1, "White", "Skyblue")
        for i in range(snow_flakes):
            snowflakeX = random.randint(0, width)
            snowflakeY = random.randint(0, height)
            canvas.draw_circle((snowflakeX, snowflakeY), 5, 2, "Black", "White")
    
    def sun():
        global y1
        if y1 > 100: 
            y1 -= 1
        canvas.draw_circle((300, y1), 25, 2, "Black", "#FFE484")
    
    def horizon():
        canvas.draw_line((0, 300), (600, 300), 1, "Black")
    
    def street():
        canvas.draw_polygon([(0, 600), (200, 300)], 1, "Black")  # Left Street
        canvas.draw_polygon([(20, 600), (210, 300)], 1, "Black")
        canvas.draw_polygon([(600, 600), (400, 300)], 1, "Black")  # Right Street
        canvas.draw_polygon([(580, 600), (390, 300)], 1, "Black")
    def skyscraper():
        canvas.draw_polygon([(100, 450), (100, 200), (0, 200), (0, 450)], 1, "Red") # Far Frame
        canvas.draw_polygon([(100, 200), (150, 175)], 1, "Green")
    
    snowflakes()
    sun()
    horizon()
    street()
    skyscraper()

frame = simplegui.create_frame("Christmas St.", width, height)
frame.set_canvas_background("LightGray")
frame.set_draw_handler(draw_handler)
frame.start()
