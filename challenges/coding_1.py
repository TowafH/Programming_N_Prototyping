# Import the math library
import math

# Sphere Volume Function w/ one parameter
def sphere_volume(radius):
  volume = (4/3) * math.pi * (radius ** 3) # Volume Formula
  return volume # Return Statement for when the Function is called

# Store the volume in a variable
volume_result = sphere_volume(5)
# Print the volume of a sphere to the user; rounded to the 2nd decimal.
print(f"#1: The volume of a sphere of 5 radius is {volume_result:.2f}")

# Wholesale Cost Function w/ one parameter
def w_cost(copies):
	# Store variables with values given by the Problem
    cover_price = 24.95
    discount = 0.40
    shipFirst = 3
    shipAfter = 0.75
    
    # Calculate the discount price w/ the cover price
    discount_price = cover_price * (1 - discount)
    
    # Calculate the cost of all 60 copies w/ the discount price
    total_book_cost = discount_price * copies
    
    # Calculate the total shipping cost w/ the first Shipping price and after Shipping price
    total_shipping = shipFirst + (shipAfter * (copies - 1))
    
    # Calculate the total wholesale cost
    total = total_book_cost + total_shipping
    
	# Return statement to return the total when the Function is called
	return total
# Store the returned value from the function into a variable
cost = w_cost(60)
# Print the wholesale cost to the user
print(f"#2: Your wholesale cost for 60 books is ${cost:.2f}")

# Running time formula w/ two parameters
def running_time(start_hour, start_min):
    # Converting the minutes and seconds into seconds for each of the paces
    easy_pace = (8*60) + 15
    tempo_pace = (7*60) + 12
    
    # Calculate the total time in second
    total_time_second = (easy_pace * 2) + (tempo_pace * 3)
    
    # Calculate the total_minutes w/ Integer divison to remove the decimal (seconds)
    total_minutes = total_time_second // 60
    # Calculate the total seconds w/ Modulous to remove the minutes, and get the remainder (seconds)
    total_seconds = total_time_second % 60
    
    # Calculate the end minutes, combining the total minutes with the starting minutes
    end_minutes = total_minutes + start_min
    # Set the end_hour variable to the start_hour
    end_hour = start_hour
    
    # Functon to check if the end_minutes exceed an hour (60) and recalculate for a new hour and minute
    if end_minutes >= 60:
        end_hour += end_minutes // 60
        end_minutes = end_minutes % 60
    # Return statement to return the arrival time
    return end_hour, end_minutes

# Storing the end hour and end minutes from the running_time Function
end_hour, end_minutes = running_time(6, 52)
# Print the arrival time for breakfast to the user
print(f"#3: You arrived home for breakfast at {end_hour}:{end_minutes} AM")
