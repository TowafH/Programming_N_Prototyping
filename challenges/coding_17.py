# Towaf Hossain
# PD 1-2
# Function checks if 'a' is a power of 'b' by checking divisibility and equality conditions.
def is_power(a, b):
    if a < b:
        print(f"{a} is not a power of {b}: False\n")
    if a == b:
        print(f"{a} is a power of {b} and can be raised to the 1: True\n")
    if a % b == 0:
        print(f"{a} is divisible by {b}: True\n")
    else:
        print(f"{a} is not divisible by {b}: False\n")

# Test cases
is_power(16, 2)  # True, because 16 = 2^4
is_power(27, 3)  # True, because 27 = 3^3
is_power(9, 2)   # False, because 9 is not a power of 2
is_power(81, 3)  # True, because 81 = 3^4
is_power(32, 5)  # False, because 32 is not a power of 5
