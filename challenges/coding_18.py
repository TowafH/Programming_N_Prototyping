# Towaf Hossain
# PD 1-2

def gcd(a, b):
    if b == 0:
        print(f"The GCD is {a} when b is 0\n")
        return a  # Return the GCD when b is 0
    else:
        print(f"Calculating GCD of {a} and {b}, remainder is {a % b}")
        gcd(b, a % b) 

gcd(48, 18)  # 6
gcd(56, 98)  # 14
gcd(101, 10)  # 1
gcd(42, 56)  # 14
gcd(17, 13)  # 1
