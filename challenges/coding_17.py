# Towaf Hossain
# PD 1-2
def is_power(a, b):
    if a < b:
        print(f"{a} is not a power of {b}: False\n")
    
    if a == b:
        print(f"{a} is a power of {b} and can be raised to the 1: True\n")
    
    if a % b == 0:
        print(f"{a} is divisible by {b}: True\n")
    
    else:
        print(f"{a} is not divisible by {b}: False\n")
        
is_power(16, 2) # True
is_power(27, 3) # True
is_power(9, 2) # False
is_power(81, 3) # True
is_power(32, 5) # False

