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
      
        for i in range(snow_flakes):
            snowflakeX = random.randint(0, width)
            snowflakeY = random.randint(0, height)
            canvas.draw_circle((snowflakeX, snowflakeY), 5, 2, "Black", "White")
    
    def sun():
        global width
        global height
        global y1
        
        canvas.draw_polygon([(0,0), (width, 0), (width, height / 2), (0, height / 2)], 1, "White", "Skyblue")
        
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
        canvas.draw_polygon([(100, 450), (100, 200), (0, 200), (0, 450)], 1, "Black", "Pale") # Rear
        canvas.draw_polygon([(100, 200), (150, 175), (150, 375), (100, 450)], 1, "Black", "Pale") # Front 
        canvas.draw_polygon([(150, 175), (0, 175), (0, 200), (100, 200)], 1, "Black", "Pale") # Roof
        # Details
        canvas.draw_polygon([(10, 440), (90, 440), (90, 215), (10, 215)], 1, "Black", "White") # Window
        canvas.draw_polygon([(115, 430), (115, 370), (130, 355), (140,355)], 1, "Black", "White")
    
    sun()
    horizon()
    street()
    skyscraper()
    snowflakes()

frame = simplegui.create_frame("Christmas St.", width, height)
frame.set_canvas_background("LightGray")
frame.set_draw_handler(draw_handler)
frame.start()
