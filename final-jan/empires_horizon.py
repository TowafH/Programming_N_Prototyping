import simplegui
import random

# Images
ew_img = simplegui.load_image("https://i.imgur.com/jNCFe15.png")
meat_img = simplegui.load_image("https://i.imgur.com/l36bx8O.png")
stone_img = simplegui.load_image("https://i.imgur.com/3CJOhOq.png")
wood_img = simplegui.load_image("https://i.imgur.com/w8NBqHC.png")
water_img = simplegui.load_image("https://i.imgur.com/izGzxxF.png")
population_img = simplegui.load_image("https://i.imgur.com/r6vJgA0.png")

# In-game Icons
stone_icon = simplegui.load_image("https://i.imgur.com/bZhX2UI.png")

# Screen
current_screen = "menu"

# Resources
meat_num = 45
stone_num = 60
wood_num = 80
water_num = 70
population_num = 10

built_well = False

# Response
response = "Welcome to the Eastern Woodlands!"


# Draw handler function
def draw(canvas):
    global current_screen, response
    
    if current_screen == "menu":
        menu(canvas)
    elif current_screen == "eastern_woodlands":
        eastern_woodlands(canvas, response, stone_icon)
        
    global meat_num, stone_num, wood_num, water_num, population_num, built_well
    
    if meat_num >= 100 and stone_num >= 100 and wood_num >= 100 and water_num >= 100 and population_num >= 50:
        response = "You Win!"
    elif meat_num <= 0 and stone_num <= 0 and wood_num <= 0 and water_num <= 0 and population_num <= 0:
        response = "You Lost!"



# Menu function
def menu(canvas):
    canvas.draw_text("Empires Horizon", (275, 50), 40, "Black")
    # Box for Regions
    canvas.draw_polygon([(50, 85), (750, 85), (750, 700), (50, 700)], 2, "#CDC7C7", "#CDC7C7")

    # EW - Titles
    canvas.draw_text("Eastern Woodlands", (70, 125), 35, "Black")
    canvas.draw_text("Resources", (475, 125), 35, "Black")

    # Eastern Woodlands Picture
    if ew_img.get_width() > 0 and ew_img.get_height() > 0:
        canvas.draw_image(ew_img, 
                        (ew_img.get_width() / 2, ew_img.get_height() / 2), 
                        (ew_img.get_width(), ew_img.get_height()), 
                        (200, 240), 
                        (250, 200))

    # Eastern Woodlands Resources
    # Meat
    canvas.draw_polygon([(400, 165), (720, 165)], 15, "#FFFFFF") 
    canvas.draw_polygon([(400, 165), (600, 165)], 15, "#48C09A")
    if ew_img.get_width() > 0 and ew_img.get_height() > 0:
        canvas.draw_image(meat_img, 
                      (meat_img.get_width() / 2, meat_img.get_height() / 2),  # Center of the image
                      (meat_img.get_width(), meat_img.get_height()),         # Image size
                      (370, 165),  # Position
                      (30, 25))  # Fixed size
    # Stone
    canvas.draw_polygon([(400, 205), (720, 205)], 15, "#FFFFFF") 
    canvas.draw_polygon([(400, 205), (650, 205)], 15, "#48C09A")
    if ew_img.get_width() > 0 and ew_img.get_height() > 0:
        canvas.draw_image(stone_img, 
                      (stone_img.get_width() / 2, stone_img.get_height() / 2),  # Center of the image
                      (stone_img.get_width(), stone_img.get_height()),         # Image size
                      (370, 205),  # Position
                      (30, 25))  # Fixed size

    # Wood
    canvas.draw_polygon([(400, 245), (720, 245)], 15, "#FFFFFF") 
    canvas.draw_polygon([(400, 245), (700, 245)], 15, "#48C09A")
    if ew_img.get_width() > 0 and ew_img.get_height() > 0:
        canvas.draw_image(wood_img, 
                      (wood_img.get_width() / 2, wood_img.get_height() / 2),  # Center of the image
                      (wood_img.get_width(), wood_img.get_height()),         # Image size
                      (370, 245),  # Position
                      (30, 25))  # Fixed size
    # Water
    canvas.draw_polygon([(400, 285), (720, 285)], 15, "#FFFFFF") 
    canvas.draw_polygon([(400, 285), (710, 285)], 15, "#48C09A")
    if ew_img.get_width() > 0 and ew_img.get_height() > 0:
        canvas.draw_image(water_img, 
                      (water_img.get_width() / 2, water_img.get_height() / 2),  # Center of the image
                      (water_img.get_width(), water_img.get_height()),         # Image size
                      (370, 285),  # Position
                      (20, 25))  # Fixed size




# Eastern Woodlands Content
def eastern_woodlands(canvas, response, stone_icon):
    # Title
    canvas.draw_text("Eastern Woodlands", (75, 50), 40, "Black")

    # Box for Regions
    canvas.draw_polygon([(50, 85), (750, 85), (750, 700), (50, 700)], 2, "#CDC7C7", "#CDC7C7")
    
    # Display responses to events
    canvas.draw_text(response, (55, 725), 25, "Black")

    # Population
    if ew_img.get_width() > 0 and ew_img.get_height() > 0:
        canvas.draw_image(population_img, 
                      (population_img.get_width() / 2, population_img.get_height() / 2),  # Center of the image
                      (population_img.get_width(), population_img.get_height()),         # Image size
                      (750, 35),  # Position
                      (40, 40))  # Fixed size
    # Population Text Counter
    canvas.draw_text(str(population_num), (695, 45), 30, "#1C274C", "sans-serif")
    
# Resources
    # Meat
    if ew_img.get_width() > 0 and ew_img.get_height() > 0:
        canvas.draw_image(meat_img, 
                      (meat_img.get_width() / 2, meat_img.get_height() / 2),  # Center of the image
                      (meat_img.get_width(), meat_img.get_height()),         # Image size
                      (500, 725),  # Position
                      (30, 30))  # Fixed size
    # Meat Text Counter
    canvas.draw_text(str(meat_num), (525, 733), 30, "#A64D4D", "sans-serif")

    # Stone
    if ew_img.get_width() > 0 and ew_img.get_height() > 0:
        canvas.draw_image(stone_img, 
                      (stone_img.get_width() / 2, stone_img.get_height() / 2),  # Center of the image
                      (stone_img.get_width(), stone_img.get_height()),         # Image size
                      (500, 770),  # Position
                      (30, 30))  # Fixed size
    # Stone Text Counter
    canvas.draw_text(str(stone_num), (525, 780), 30, "#99AAB5", "sans-serif")
    
    # Wood
    if ew_img.get_width() > 0 and ew_img.get_height() > 0:
        canvas.draw_image(wood_img, 
                      (wood_img.get_width() / 2, wood_img.get_height() / 2),  # Center of the image
                      (wood_img.get_width(), wood_img.get_height()),         # Image size
                      (650, 725),  # Position
                      (40, 30))  # Fixed size
    # Wood Text Counter
    canvas.draw_text(str(wood_num), (675, 735), 30, "#9E5A23", "sans-serif")

    # Water
    if ew_img.get_width() > 0 and ew_img.get_height() > 0:
        canvas.draw_image(water_img, 
                      (water_img.get_width() / 2, water_img.get_height() / 2),  # Center of the image
                      (water_img.get_width(), water_img.get_height()),         # Image size
                      (650, 770),  # Position
                      (30, 40))  # Fixed size
    # Water Text Counter
    canvas.draw_text(str(water_num), (675, 780), 30, "#4796E7", "sans-serif")

    # Stone Preview
    if ew_img.get_width() > 0 and ew_img.get_height() > 0:
        canvas.draw_image(stone_icon, 
                      (stone_icon.get_width() / 2, stone_icon.get_height() / 2),  # Center of the image
                      (stone_icon.get_width(), stone_icon.get_height()),         # Image size
                      (180, 600),  # Position
                      (220, 200))  # Fixed size
#E-W Functionality

# Hunt action
def hunt():
    global meat_num, response

    events = ["You got a deer! +3 Meat", "You failed to hunt! -2 Meat", "You got a Salmon! +2 Meat", "You lost a fish! -2 Meat"]
    values = [3, -2, 2, -2]
    
    random_event = random.randint(0, len(events) - 1)
    
    if current_screen == "eastern_woodlands":
        # Event Player
        response = events[random_event]
        meat_num += values[random_event]
    else:
        print("Please select Eastern Woodlands before hunting.")

# Mine action
def mine():
    global stone_num, stone_icon, response

    events = ["You got diamonds! +4 Stone", "You fell into a cave! -1 Stone", "You got coal! +2 Stone!", "You broke your pickaxe! -2 Stone"]
    values = [4, -1, 2, -2]
    
    random_event = random.randint(0, len(events) - 1)
    
    if current_screen == "eastern_woodlands" and stone_num >= 75:
        stone_icon = simplegui.load_image("https://i.imgur.com/GYC1mQk.png")
        
    if current_screen == "eastern_woodlands":
        # Event Player
        response = events[random_event]
        stone_num += values[random_event]
    else:
        print("Please select Eastern Woodlands before mining.")


# Logging action
def logging():
    global wood_num
    global response

    events = ["You cut down a tree! +4 Wood", "You got stuck in the woods! -1 Wood", "You collected some sticks! +1 Wood", "You lost some wood! -1 Wood"]
    values = [4, -1, 1, -1]
    
    random_event = random.randint(0, len(events) - 1)
    
    if current_screen == "eastern_woodlands":
        # Event Player
        response = events[random_event]
        wood_num += values[random_event]
    else:
        print("Please select Eastern Woodlands before logging.")

# Populate action
def population():
    global population_num, response
    
    events = ["You gained population! +2 People", "You built a house! +5 People", "Someone left town! -1 Population", "One person died! -1 Population"]
    values = [2, 5, -1, -1]
    
    random_event = random.randint(0, len(events) - 1)
    
    if current_screen == "eastern_woodlands":
        # Event Player
        response = events[random_event]
        population_num += values[random_event]
    else:
        print("Please select Eastern Woodlands before logging.")

# Build Action
def build():
    global built_well, meat_num, wood_num, water_num, stone_num, response
    
    events = ["You successfully built the well!", "You successfully built the well!"]
    values = [-20, -20]
    
    random_event = random.randint(0, len(events) - 1)
    
    if current_screen == "eastern_woodlands" and built_well == False and wood_num >= 20 and water_num >= 20 and meat_num >= 20 and stone_num >= 20:
        # Event Player
        response = events[random_event]
        wood_num += values[random_event]
        water_num += values[random_event]
        meat_num += values[random_event]
        stone_num += values[random_event]
        built_well = True
    else:
        response = "You've built a well already!"

# Water action
def well():
    global built_well, water_num, response
    
    events = ["You collected water! +9 Water", "Your pail fell in the well! -1 Water", "You collected some dirty war! -1 Water", "You lost some water! -2 Water"]
    values = [9, -1, -1, -2]
    
    random_event = random.randint(0, len(events) - 1)
    
    if current_screen == "eastern_woodlands" and built_well == True:
        # Event Player
        response = events[random_event]
        water_num += values[random_event]
    else:
        response = "You need to build a well!"


# Eastern Woodlands button click handler
def select_eastern_woodlands():
    global current_screen
    current_screen = "eastern_woodlands"


# Create a Frame
frame = simplegui.create_frame("Empires Horizon", 800, 800)
# Add buttons to the menu screen
frame.add_button("Eastern Woodlands", select_eastern_woodlands, 200)
frame.add_button("Hunt", hunt, 200)
frame.add_button("Mine", mine, 200)
frame.add_button("Logging", logging, 200)
frame.add_button("Populate", population, 200)
frame.add_button("Make a well", build, 200)
frame.add_button("Use the well", well, 200)


# Background Color
frame.set_canvas_background("White")

# Set the draw handler
frame.set_draw_handler(draw)

# Start the frame
frame.start()
