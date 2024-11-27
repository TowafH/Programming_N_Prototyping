# Towaf Hossain
# PD 1-2
# 11/27/24

import simplegui

def draw_handler(canvas):
    turkey_color = "#C9592E"

    #canvas.draw_point([x,y], "color")
    #canvas.draw_line([x1,y1],[x2,y2], line_width, "color")
    #canvas.draw_polygon([(x1, y1), (x2,y2), (x3,y3)], line_width, "color")
    #canvas.draw_circle((x1, y1), radius, line_width, "color")
    #def turkeyFeathers():
        #canvas.draw_polygon([],[], 5, "color")
    def turkeyFace():
        canvas.draw_circle((85, 80), 3, 2, "black", "black") # Turkey Left Eye
        canvas.draw_circle((115, 80), 3, 2, "black", "black") # Turkey Left Eye

    def turkeyBody():
        canvas.draw_circle((100, 100), 50, 2, turkey_color, turkey_color) # Turkey Body
        canvas.draw_polygon([(85, 90), (100, 110), (115, 90)], 2, "Orange", "Orange") # Turkey Beak
        
    def turkeyLeftLeg():
        canvas.draw_line([80,140],[80,160], 5, "Black") # Turkey leg
        canvas.draw_line([80,160],[70, 165], 5, "Black") # Turkey Left Foot
        canvas.draw_line([80,160],[90, 165], 5, "Black") # Turkey Right Foot
        canvas.draw_line([80, 160],[80,170], 5, "Black") # Turkey Middle Foot

    def turkeyRightLeg():
        canvas.draw_line([120, 140], [120, 160], 5, "Black")
        canvas.draw_line([120,160],[110, 165], 5, "Black") # Turkey Left Foot
        canvas.draw_line([120,160],[130, 165], 5, "Black") # Turkey Right Foot
        canvas.draw_line([120, 160],[120,170], 5, "Black") # Turkey Middle Foot
    turkeyBody()
    turkeyFace()
    turkeyLeftLeg()
    turkeyRightLeg()

# Code to Modify the Frame
    # Creates the frame w/ Title & Dimensions
frame = simplegui.create_frame("Thanksgiving Motif", 200, 200)
    # Modify the background color of the frame
frame.set_canvas_background("White")                         
    # Set the draw handler
frame.set_draw_handler(draw_handler)


# Nothing will run until we .start() the frame
frame.start()
