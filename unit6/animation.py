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
        
        for i in range(1):
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
        canvas.draw_polygon([(100, 450), (100, 200), (0, 200), (0, 450)], 1, "Black", "#FAF9DE") # Rear
        canvas.draw_polygon([(100, 200), (150, 175), (150, 375), (100, 450)], 1, "Black", "#FAF9DE") # Front 
        canvas.draw_polygon([(150, 175), (0, 175), (0, 200), (100, 200)], 1, "Black", "#FAF9DE") # Roof
        # Details
        canvas.draw_polygon([(10, 440), (90, 440), (90, 215), (10, 215)], 1, "Black", "#d8e4e9") # Window
        canvas.draw_polygon([(115, 430), (115, 370), (130, 355), (130,410)], 1, "Black", "#d8e4e9") # Door
        
    def skyscraper2():
        canvas.draw_polygon([(500, 450), (500, 200), (600, 200), (600, 450)], 1, "Black", "#a5a5a5") # Rear
        canvas.draw_polygon([(500, 200), (450, 175), (450, 375), (500, 450)], 1, "Black", "#a5a5a5") # Front 
        canvas.draw_polygon([(450, 175), (600, 175), (600, 200), (500, 200)], 1, "Black", "#a5a5a5") # Roof
        # Details
        canvas.draw_polygon([(510, 440), (590, 440), (590, 215), (510, 215)], 1, "Black", "#d8e4e9") # Window
        canvas.draw_polygon([(485, 430), (485, 370), (470, 355), (470, 410)], 1, "Black", "#d8e4e9") # Door

    def tree():
        canvas.draw_line((40, 500), (40, 350), 5, "#694b37") # Log
        canvas.draw_polygon([(10, 400), (40, 300), (70, 400)], 1, "#587e60", "#587e60") # Top Leaf
        canvas.draw_polygon([(10, 425), (40, 325), (70, 425)], 1, "#587e60", "#587e60") # Mid-1 Leaf
        canvas.draw_polygon([(5, 450), (40, 350), (75, 450)], 1, "#587e60", "#587e60") # Mid-1 Leaf
    
    def tree2():
        canvas.draw_line((560, 500), (560, 350), 5, "#694b37")  # Log
        canvas.draw_polygon([(530, 400), (560, 300), (590, 400)], 1, "#587e60", "#587e60")  # Top Leaf
        canvas.draw_polygon([(530, 425), (560, 325), (590, 425)], 1, "#587e60", "#587e60")  # Mid-1 Leaf
        canvas.draw_polygon([(525, 450), (560, 350), (595, 450)], 1, "#587e60", "#587e60")  # Bottom Leaf

        # Details
        canvas.draw_circle((545, 390), 5, 1, "Red", "Red")  # Top Ornament
        canvas.draw_circle((575, 410), 5, 1, "Gold", "Gold")  # Right Ornament
        canvas.draw_circle((545, 440), 5, 1, "Blue", "Blue")  # Bottom Ornament
        canvas.draw_circle((575, 430), 5, 1, "Silver", "Silver")  # Left Ornament
        canvas.draw_circle((560, 360), 7, 1, "Yellow", "Yellow")  # Star at the top

    def snowman():
        # Body
        canvas.draw_circle((300, 450), 40, 2, "Black", "White")  # Bottom
        canvas.draw_circle((300, 400), 30, 2, "Black", "White")  # Middle
        canvas.draw_circle((300, 360), 20, 2, "Black", "White")  # Head

        # Face Details
        canvas.draw_circle((292, 355), 3, 2, "Black", "Black")  # Left Eye
        canvas.draw_circle((308, 355), 3, 2, "Black", "Black")  # Right Eye
        canvas.draw_polygon([(300, 360), (315, 363), (300, 365)], 1, "Orange", "Orange")  # Nose

        # Buttons
        canvas.draw_circle((300, 395), 3, 2, "Black", "Black")  # Top Button
        canvas.draw_circle((300, 415), 3, 2, "Black", "Black")  # Bottom Button

        # Arms
        canvas.draw_line((270, 390), (220, 380), 2, "#8B4513")  # Left Arm
        canvas.draw_line((330, 390), (380, 380), 2, "#8B4513")  # Right Arm

        # Hat
        canvas.draw_polygon([(265, 345), (335, 345), (335, 350), (265, 350)], 1, "Black", "Black")  # Foundation
        canvas.draw_polygon([(275, 315), (325, 315), (325, 345), (275, 345)], 1, "Black", "Black")  # Hat Top

    # Call all functions
    sun()
    horizon()
    street()
    skyscraper()
    skyscraper2()
    snowman()
    tree()
    tree2()
    snowflakes()

frame = simplegui.create_frame("Christmas St.", width, height)
frame.set_canvas_background("Snow")
frame.set_draw_handler(draw_handler)
frame.start()
