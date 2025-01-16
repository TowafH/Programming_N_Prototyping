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
well_icon = simplegui.load_image("")
house_icon = simplegui.load_image("")

# Screen
current_screen = "menu"

# Resources
meat_num = 25
stone_num = 40
wood_num = 50
water_num = 45
population_num = 10
house_num = 0

built_well = False
built_house = False

# Response
response = "Welcome to the Eastern Woodlands!"

# Win/Loss Conditions
# Win
def win():
    global response
    if meat_num >= 100 and stone_num >= 100 and wood_num >= 100 and water_num >= 100 and population_num >= 50 and house_num >= 5:
        response = "Congratulations! You Won!"
        return True
    return False

# Loss
def loss():
    global response
    if meat_num <= 0 and stone_num <= 0 and wood_num <= 0 and water_num <= 0 and population_num <= 0:
        response = "Game Over! You've lost all your resources!"
        return True 
    
    if meat_num <= 0:
        response = "You've run out of meat!"
        return True
    if stone_num <= 0:
        response = "You've run out of stone!"
        return True
    if wood_num <= 0:
        response = "You've run out of wood!"
        return True
    if water_num <= 0:
        response = "You've run out of water!"
        return True
    if population_num <= 0:
        response = "Your population has perished!"
        return True

    return False

# Update the draw handler function to check for losses
def draw(canvas):
    global current_screen, response
    
    if current_screen == "menu":
        menu(canvas)
    elif current_screen == "eastern_woodlands":
        eastern_woodlands(canvas, response, stone_icon)
        
    global meat_num, stone_num, wood_num, water_num, population_num, built_well, house_num

# Menu
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
    if meat_img.get_width() > 0 and meat_img.get_height() > 0:
        canvas.draw_image(meat_img, 
                      (meat_img.get_width() / 2, meat_img.get_height() / 2), 
                      (meat_img.get_width(), meat_img.get_height()),    
                      (370, 165),  
                      (30, 25))  
    # Stone
    canvas.draw_polygon([(400, 205), (720, 205)], 15, "#FFFFFF") 
    canvas.draw_polygon([(400, 205), (650, 205)], 15, "#48C09A")
    if stone_img.get_width() > 0 and stone_img.get_height() > 0:
        canvas.draw_image(stone_img, 
                      (stone_img.get_width() / 2, stone_img.get_height() / 2),
                      (stone_img.get_width(), stone_img.get_height()),     
                      (370, 205),  
                      (30, 25)) 

    # Wood
    canvas.draw_polygon([(400, 245), (720, 245)], 15, "#FFFFFF") 
    canvas.draw_polygon([(400, 245), (700, 245)], 15, "#48C09A")
    if wood_img.get_width() > 0 and wood_img.get_height() > 0:
        canvas.draw_image(wood_img, 
                      (wood_img.get_width() / 2, wood_img.get_height() / 2),
                      (wood_img.get_width(), wood_img.get_height()),     
                      (370, 245), 
                      (30, 25))  
    # Water
    canvas.draw_polygon([(400, 285), (720, 285)], 15, "#FFFFFF") 
    canvas.draw_polygon([(400, 285), (710, 285)], 15, "#48C09A")
    if water_img.get_width() > 0 and water_img.get_height() > 0:
        canvas.draw_image(water_img, 
                      (water_img.get_width() / 2, water_img.get_height() / 2), 
                      (water_img.get_width(), water_img.get_height()),      
                      (370, 285),  
                      (20, 25))

# Eastern Woodlands Content
def eastern_woodlands(canvas, response, stone_icon):
    # Title
    canvas.draw_text("Eastern Woodlands", (75, 50), 40, "Black")

    # Box for Regions
    canvas.draw_polygon([(50, 85), (750, 85), (750, 700), (50, 700)], 2, "#CDC7C7", "#CDC7C7")
    
    # Display responses to events
    canvas.draw_text(response, (55, 725), 25, "Black")

    # Population
    if population_img.get_width() > 0 and population_img.get_height() > 0:
        canvas.draw_image(population_img, 
                      (population_img.get_width() / 2, population_img.get_height() / 2), 
                      (population_img.get_width(), population_img.get_height()),      
                      (750, 35),
                      (40, 40))  
    # Population Text Counter
    canvas.draw_text(str(population_num), (695, 45), 30, "#1C274C", "sans-serif")
    
# Resources Inventory
    # Meat
    if meat_img.get_width() > 0 and meat_img.get_height() > 0:
        canvas.draw_image(meat_img, 
                      (meat_img.get_width() / 2, meat_img.get_height() / 2), 
                      (meat_img.get_width(), meat_img.get_height()),       
                      (500, 725),  
                      (30, 30))
    # Meat Text Counter
    canvas.draw_text(str(meat_num), (525, 733), 30, "#A64D4D", "sans-serif")

    # Stone
    if stone_img.get_width() > 0 and stone_img.get_height() > 0:
        canvas.draw_image(stone_img, 
                      (stone_img.get_width() / 2, stone_img.get_height() / 2), 
                      (stone_img.get_width(), stone_img.get_height()),     
                      (500, 770),  
                      (30, 30)) 
    # Stone Text Counter
    canvas.draw_text(str(stone_num), (525, 780), 30, "#99AAB5", "sans-serif")
    
    # Wood
    if wood_img.get_width() > 0 and wood_img.get_height() > 0:
        canvas.draw_image(wood_img, 
                      (wood_img.get_width() / 2, wood_img.get_height() / 2),  
                      (wood_img.get_width(), wood_img.get_height()),     
                      (650, 725),
                      (40, 30))
    # Wood Text Counter
    canvas.draw_text(str(wood_num), (675, 735), 30, "#9E5A23", "sans-serif")

    # Water
    if water_img.get_width() > 0 and water_img.get_height() > 0:
        canvas.draw_image(water_img, 
                      (water_img.get_width() / 2, water_img.get_height() / 2), 
                      (water_img.get_width(), water_img.get_height()),        
                      (650, 770),  
                      (30, 40)) 
    # Water Text Counter
    canvas.draw_text(str(water_num), (675, 780), 30, "#4796E7", "sans-serif")

    
    
    # Stone Icon
    if stone_icon.get_width() > 0 and stone_icon.get_height() > 0:
        canvas.draw_image(stone_icon, 
                      (stone_icon.get_width() / 2, stone_icon.get_height() / 2),
                      (stone_icon.get_width(), stone_icon.get_height()),
                      (180, 600),
                      (220, 200))
    # Well Icon
    if built_well == True and well_icon.get_width() > 0 and well_icon.get_height() > 0:
        canvas.draw_image(well_icon, 
                          (well_icon.get_width() / 2, well_icon.get_height() / 2), 
                          (well_icon.get_width(), well_icon.get_height()), 
                          (630, 575),
                          (250, 250))
    if built_house == True and house_icon.get_width() > 0 and house_icon.get_height() > 0:
        for i in range(house_num):
            x_pos = 700 - (i * 140)
            canvas.draw_image(house_icon, 
                          (house_icon.get_width() / 2, house_icon.get_height() / 2), 
                          (house_icon.get_width(), house_icon.get_height()), 
                          (x_pos, 175),
                          (100, 100))
#E-W Functionality

# Hunt action
def hunt():
    global meat_num, response, house_num

    # Random Events w/ List
    events = ["You got a deer! +3 Meat", "You failed to hunt! -2 Meat", "You got a Salmon! +2 Meat", "You lost a fish! -2 Meat"]
    values = [3, -2, 2, -2]
    
    random_event = random.randint(0, len(events) - 1)
    
    # Event
    if current_screen == "eastern_woodlands":
        response = events[random_event]
        # If the player invests in houses, they gain more resources
        if house_num == 1:
            meat_num += 3 + values[random_event]
        elif house_num == 2:
            meat_num += 4 + values[random_event]
        elif house_num == 3:
            meat_num += 5 + values[random_event]
        elif house_num == 4:
            meat_num += 6 + values[random_event]
        elif house_num == 5:
            meat_num += 7 + values[random_event]
    else:
        print("Please select Eastern Woodlands before hunting.")

# Mine action
def mine():
    global stone_num, stone_icon, response, house_num

    # Random Events w/ List
    events = ["You got diamonds! +4 Stone", "You fell into a cave! -1 Stone", "You got coal! +2 Stone!", "You broke your pickaxe! -2 Stone"]
    values = [4, -1, 2, -2]
    
    random_event = random.randint(0, len(events) - 1)
    
    # Load Stone Icon
    if current_screen == "eastern_woodlands" and stone_num >= 75:
        new_icon = simplegui.load_image("https://i.imgur.com/GYC1mQk.png")
        if new_icon.get_width() > 0 and new_icon.get_height() > 0:
            stone_icon = new_icon
    
    # Event
    if current_screen == "eastern_woodlands":
        response = events[random_event]
        # If the player invests in houses, they gain more resources
        if house_num == 1:
            stone_num += 3 + values[random_event]
        elif house_num == 2:
            stone_num += 4 + values[random_event]
        elif house_num == 3:
            stone_num += 5 + values[random_event]
        elif house_num == 4:
            stone_num += 6 + values[random_event]
        elif house_num == 5:
            stone_num += 7 + values[random_event]
    else:
        print("Please select Eastern Woodlands")

# Logging action
def logging():
    global wood_num, response, house_num

    # Random Events w/ List
    events = ["You cut down a tree! +4 Wood", "You got stuck in the woods! -1 Wood", "You collected some sticks! +1 Wood", "You lost some wood! -1 Wood"]
    values = [4, -1, 1, -1]
    
    random_event = random.randint(0, len(events) - 1)

    # Event
    if current_screen == "eastern_woodlands":
        # Event Player
        response = events[random_event]
        # If the player invests in houses, they gain more resources
        if house_num == 1:
            wood_num += 3 + values[random_event]
        elif house_num == 2:
            wood_num += 4 + values[random_event]
        elif house_num == 3:
            wood_num += 5 + values[random_event]
        elif house_num == 4:
            wood_num += 6 + values[random_event]
        elif house_num == 5:
            wood_num += 7 + values[random_event]
    else:
        print("Please select Eastern Woodlands")

# Water action
def well():
    global built_well, water_num, response, house_num
    
    events = ["You collected water! +9 Water", "Your pail fell in the well! -1 Water", "You collected some dirty war! -1 Water", "You lost some water! -2 Water"]
    values = [9, -1, -1, -2]
    
    random_event = random.randint(0, len(events) - 1)
    
    # Event
    if current_screen == "eastern_woodlands" and built_well == True:
        response = events[random_event]
        if house_num == 1:
            water_num += 3 + values[random_event]
        elif house_num == 2:
            water_num += 4 + values[random_event]
        elif house_num == 3:
            water_num += 5 + values[random_event]
        elif house_num == 4:
            water_num += 6 + values[random_event]
        elif house_num == 5:
            water_num += 7 + values[random_event]
    else:
        response = "You need to build a well!"
        
# Populate action
def population():
    global population_num, response
    
    # Random Events w/ List
    events = ["You gained population! +2 People", "You built a house! +5 People", "Someone left town! -1 Population", "One person died! -1 Population"]
    values = [2, 5, -1, -1]
    
    random_event = random.randint(0, len(events) - 1)
    
    # Event
    if current_screen == "eastern_woodlands":
        response = events[random_event]
        population_num += values[random_event]
    else:
        print("Please select Eastern Woodlands")

# Build Actions
def home():
    global built_house, house_icon, house_num, wood_num, water_num, stone_num, response
    
    # Event
    if current_screen == "eastern_woodlands" and wood_num >= 20 and water_num >= 20 and stone_num >= 20:
        wood_num -= 20
        water_num -= 20
        stone_num -= 20
        house_num += 1
        built_house = True
        house_icon = simplegui.load_image("https://i.imgur.com/kPiBeX8.png")
        response = "You successfully built one house!"
    else:
        response = "You don't have enough materials!"


def build():
    global built_well, well_icon, meat_num, wood_num, water_num, stone_num, response
    
    # Event
    if current_screen == "eastern_woodlands":
        if built_well == True:
            response = "You've already built a well!"
        elif wood_num >= 20 and meat_num >= 20 and stone_num >= 20:
            wood_num -= 20
            meat_num -= 20
            stone_num -= 20
            built_well = True
            well_icon = simplegui.load_image("https://i.imgur.com/EJjhDSN.png")
            response = "You successfully built the well!"
        else:
            response = "You don't have enough resources!"

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
frame.add_button("Use the well", well, 200)
frame.add_button("Populate", population, 200)
frame.add_button("Make a house", home, 200)
frame.add_button("Make a well", build, 200)

# Background Color
frame.set_canvas_background("White")

# Set the draw handler
frame.set_draw_handler(draw)

# Start the frame
frame.start()
