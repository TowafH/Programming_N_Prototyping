# Towaf Hossain
# PD 1-2
# 11/28/29

import simplegui

def draw_handler(canvas):
    turkey_color = "#C9592E"

    def turkeyFace():
        # Draw eyes
        canvas.draw_circle((285, 280), 15, 2, "black", "black")  # Left Eye
        canvas.draw_circle((315, 280), 15, 2, "black", "black")  # Right Eye

    def turkeyBody():
        # Draw body and beak
        canvas.draw_circle((300, 300), 150, 2, turkey_color, turkey_color)  # Turkey Body
        canvas.draw_polygon([(275, 270), (300, 330), (325, 270)], 2, "Orange", "Orange")  # Turkey Beak

    def draw_leg(base_x, base_y):
        # Draw individual leg and toes
        canvas.draw_line((base_x, base_y), (base_x, base_y + 60), 8, "Black")  # Leg
        canvas.draw_line((base_x, base_y + 60), (base_x - 30, base_y + 75), 8, "Black")  # Left Toe
        canvas.draw_line((base_x, base_y + 60), (base_x + 30, base_y + 75), 8, "Black")  # Right Toe
        canvas.draw_line((base_x, base_y + 60), (base_x, base_y + 90), 8, "Black")  # Middle Toe

    def draw_feathers():
        # Existing feathers as rectangles
        canvas.draw_polygon([(150, 180), (210, 180), (210, 300), (150, 300)], 2, "#FF6F61", "#FF6F61")  # Feather 1
        canvas.draw_polygon([(195, 120), (255, 120), (255, 240), (195, 240)], 2, "#FFA500", "#FFA500")  # Feather 2
        canvas.draw_polygon([(240, 90), (300, 90), (300, 210), (240, 210)], 2, "#FFD700", "#FFD700")  # Feather 3
        canvas.draw_polygon([(285, 60), (345, 60), (345, 240), (285, 240)], 2, "#8B0000", "#8B0000")  # Feather 4
        canvas.draw_polygon([(330, 90), (390, 90), (390, 300), (330, 300)], 2, "#6B8E23", "#6B8E23")  # Feather 5
        canvas.draw_polygon([(375, 120), (435, 120), (435, 330), (375, 330)], 2, "#4B0082", "#4B0082")  # Feather 6

    def draw_leaves():
        # Smaller, non-overlapping leaves
        canvas.draw_polygon([(60, 420), (90, 390), (120, 420), (90, 450)], 2, "#228B22", "#228B22")  # Green Leaf 1
        canvas.draw_polygon([(480, 420), (510, 390), (540, 420), (510, 450)], 2, "#228B22", "#228B22")  # Green Leaf 2
        canvas.draw_polygon([(90, 510), (120, 480), (150, 510), (120, 540)], 2, "#FFD700", "#FFD700")  # Yellow Leaf 1
        canvas.draw_polygon([(150, 540), (180, 510), (210, 540), (180, 570)], 2, "#FF6347", "#FF6347")  # Red Leaf 1
        canvas.draw_polygon([(390, 480), (420, 450), (450, 480), (420, 510)], 2, "#FFD700", "#FFD700")  # Yellow Leaf 2
        canvas.draw_polygon([(360, 540), (390, 510), (420, 540), (390, 570)], 2, "#FF6347", "#FF6347")  # Red Leaf 2
        canvas.draw_polygon([(510, 540), (540, 510), (570, 540), (540, 570)], 2, "#8B4513", "#8B4513")  # Brown Leaf 1

    def draw_pumpkin():
        canvas.draw_polygon([(90, 45), (105, 30), (120, 60), (105, 75)], 2, "#8B4513", "#8B4513")  # Pumpkin Stem
        canvas.draw_circle((120, 120), 60, 2, "#FFA500", "#FFA500")  # Pumpkin
        canvas.draw_line((90, 120), (150, 120), 4, "#FF8C00")  # Pumpkin Detail 1
        canvas.draw_line((105, 90), (135, 150), 4, "#FF8C00")  # Pumpkin Detail 2
        canvas.draw_line((150, 90), (90, 150), 4, "#FF8C00")  # Pumpkin Detail 2

    draw_leg(240, 420)  # Turkey Left Leg
    draw_leg(360, 420)  # Turkey Right Leg
    draw_feathers()
    draw_leaves()
    draw_pumpkin()
    turkeyBody()
    turkeyFace()

# Code to Modify the Frame
frame = simplegui.create_frame("Thanksgiving Motif", 600, 600)  # Create frame
frame.set_canvas_background("#573921")  # Set background color
frame.set_draw_handler(draw_handler)  # Set draw handler

# Start the frame
frame.start()
