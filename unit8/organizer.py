eventName = []
eventMonth = []
eventDay = []
eventYear = []

# Validate month input
def validateMonth(month):
    while month < 1 or month > 12:
        month = int(input("Invalid month. Please enter value from 1-12: "))
    return month

# Leap year function
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 1  # Leap year
    else:
        return 0  # Not a leap year

# Validate day based on month and year
def validateDay(day, month, year):
    # Determine the number of days in the given month
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        max_days = 31  # Months with 31 days
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_days = 30  # Months with 30 days
    elif month == 2:
        if leap_year(year):
            max_days = 29  # February in a leap year
        else:
            max_days = 28  # February in a non-leap year

    # Prompt the user until a valid day is entered
    while day < 1 or day > max_days:
        day = int(input(f"Invalid day. Please enter value from 1-{max_days}: "))
    
    return day

# Function to print all events to the user
def printEvents():
    print("\n******************** List of Events ********************")
    for i in range(len(eventName)):
        month_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][eventMonth[i] - 1]
        print(f"{eventName[i]}")
        print(f"Date: {month_name} {eventDay[i]}, {eventYear[i]}")
        print("-" * 30)

# Function to prompt, adjust, and append values to the 4 parallel lists
def addEvent():
    # Prompt the user for the event details
    event = input("What is the event: ")
    year = int(input("What is the year: "))
    month = int(input("What is the month (number): "))
    month = validateMonth(month)  # Ensure month is valid
    day = int(input("What is the date: "))
    day = validateDay(day, month, year)  # Ensure day is valid
    
    # Append the validated details to the lists
    eventName.append(event)
    eventMonth.append(month)
    eventDay.append(day)
    eventYear.append(year)

#*********** MAIN **********
# Add events
while True:
    addEvent()
    # Prompt the user to see if they want to enter more events
    more_events = input("Do you want to enter another date? NO to stop: ").lower()
    if more_events == "no":
        break

# Print all events
printEvents()
