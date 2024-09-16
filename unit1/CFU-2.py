# 9/16/24
# 1-2
# Towaf Hossain


from datetime import datetime

current_datetime = datetime.now()
current_year = current_datetime.year
fname = str(input("Enter your first name"))
lname = str(input("Enter your last name"))
age = int(input("How old are you?"))
soccer_time = int(input("How many years have you been playing soccer?"))
soccer_years = current_year - soccer_time

print("Hello! " + str(fname) + " " + str(lname) + " You're " + str(age) + " years old! \n" + "You've played soccer for " + str(soccer_time) + " years. \nYou've been playing since " + str(soccer_years) + "!")
