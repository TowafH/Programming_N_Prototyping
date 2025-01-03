def leap_year(y):
    if y % 4 and y % 100 and y % 400:
        return 1
    else:
        return 0
        
def number_of_days(m, y):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31 # Jan, March, May, July, Aug, Oct, December
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return 30 # April, June, September, November
    elif m == 2:
        if leap_year(y):
            return 29 # Feb w/ Leap Year
        else:
            return 28 # Feb w/o Leap Year

def days_passed(d, m, y):
    days = 0
    
    for i in range(1, m):
        days += number_of_days(i, y)
    days += d
    
    return days

# Variables
Day = int(input("Enter a day: "))
Month = int(input("Enter a month: "))
Year = int(input("Enter a year: "))
menu = int(input(f"Menu:\n 1) Calculate the number of days in the given month.\n 2) Calculate the number of days passed in the given year.\nPlease choose an option: "))

if menu == 1:
    print(number_of_days(Month, Year))
elif menu == 2:
    print(days_passed(Day, Month, Year))
else:
    print("Invalid")
