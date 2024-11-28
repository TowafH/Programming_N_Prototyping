# Towaf Hossain
# PD 1-2
# 11/28/29

import simplegui

def draw_handler(canvas):
    turkey_color = "#C9592E"

    def turkeyFace():
        # Draw eyes
        canvas.draw_circle((85, 80), 3, 2, "black", "black")  # Left Eye
        canvas.draw_circle((115, 80), 3, 2, "black", "black")  # Right Eye

    def turkeyBody():
        # Draw body and beak
        canvas.draw_circle((100, 100), 50, 2, turkey_color, turkey_color)  # Turkey Body
        canvas.draw_polygon([(85, 90), (100, 110), (115, 90)], 2, "Orange", "Orange")  # Turkey Beak

    def draw_leg(base_x, base_y):
        # Draw individual leg and toes
        canvas.draw_line((base_x, base_y), (base_x, base_y + 20), 5, "Black")  # Leg
        canvas.draw_line((base_x, base_y + 20), (base_x - 10, base_y + 25), 5, "Black")  # Left Toe
        canvas.draw_line((base_x, base_y + 20), (base_x + 10, base_y + 25), 5, "Black")  # Right Toe
        canvas.draw_line((base_x, base_y + 20), (base_x, base_y + 30), 5, "Black")  # Middle Toe

    def draw_feathers():
        # Existing feathers as rectangles
        canvas.draw_polygon([(50, 60), (70, 60), (70, 100), (50, 100)], 2, "#FF6F61", "#FF6F61")  # Feather 1
        canvas.draw_polygon([(65, 40), (85, 40), (85, 80), (65, 80)], 2, "#FFA500", "#FFA500")  # Feather 2
        canvas.draw_polygon([(80, 30), (100, 30), (100, 70), (80, 70)], 2, "#FFD700", "#FFD700")  # Feather 3
        canvas.draw_polygon([(95, 20), (115, 20), (115, 80), (95, 80)], 2, "#8B0000", "#8B0000")  # Feather 4
        canvas.draw_polygon([(110, 30), (130, 30), (130, 100), (110, 100)], 2, "#6B8E23", "#6B8E23")  # Feather 5
        canvas.draw_polygon([(125, 40), (145, 40), (145, 110), (125, 110)], 2, "#4B0082", "#4B0082")  # Feather 6

    def draw_leaves():
        # Smaller, non-overlapping leaves
        canvas.draw_polygon([(20, 140), (30, 130), (40, 140), (30, 150)], 2, "#228B22", "#228B22")  # Green Leaf 1
        canvas.draw_polygon([(160, 140), (170, 130), (180, 140), (170, 150)], 2, "#228B22", "#228B22")  # Green Leaf 2
        canvas.draw_polygon([(30, 170), (40, 160), (50, 170), (40, 180)], 2, "#FFD700", "#FFD700")  # Yellow Leaf 1
        canvas.draw_polygon([(50, 180), (60, 170), (70, 180), (60, 190)], 2, "#FF6347", "#FF6347")  # Red Leaf 1
        canvas.draw_polygon([(130, 160), (140, 150), (150, 160), (140, 170)], 2, "#FFD700", "#FFD700")  # Yellow Leaf 2
        canvas.draw_polygon([(120, 180), (130, 170), (140, 180), (130, 190)], 2, "#FF6347", "#FF6347")  # Red Leaf 2
        canvas.draw_polygon([(170, 180), (180, 170), (190, 180), (180, 190)], 2, "#8B4513", "#8B4513")  # Brown Leaf 1

    def draw_pumpkin():
        canvas.draw_polygon([(30, 15), (35, 10), (40, 20), (35, 25)], 2, "#8B4513", "#8B4513") # Pumpkin Stem
        canvas.draw_circle((40, 40), 20, 2, "#FFA500", "#FFA500") # Pumpkin
        canvas.draw_line((30, 40), (50, 40), 2, "#FF8C00") # Pumpkin Detail 1
        canvas.draw_line((35, 30), (45, 50), 2, "#FF8C00") # Pumpkin Detail 2
        canvas.draw_line((50, 30), (30, 50), 2, "#FF8C00") # Pumpkin Detail 2

    draw_leg(80, 140)  # Turkey Left Leg
    draw_leg(120, 140)  # Turkey Right Leg
    draw_feathers()
    draw_leaves()
    draw_pumpkin()
    turkeyBody()
    turkeyFace()

# Code to Modify the Frame
frame = simplegui.create_frame("Thanksgiving Motif", 200, 200)  # Create frame
frame.set_canvas_background("#573921")  # Set background color
frame.set_draw_handler(draw_handler)  # Set draw handler

# Start the frame
frame.start()
