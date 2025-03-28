# Towaf Hossain
# PD 1-2
def first_letter(s):
    first = s[0]
    print(f"The first letter of {s}: {first}")
    return first
    
def last_letter(s):
    last = s[len(s) - 1]
    print(f"The last letter of {s}: {last}")
    return last
    
def middle_letter(s):
    total_letters = len(s)
    middle_letter = total_letters // 2
    middle = s[middle_letter]
    print(f"The middle letter of {s}: {middle}\n")

def palindrome(s):
    print(f"Calculating if {s} is a Palindrome!")
    
    if first_letter(s).capitalize() == last_letter(s).capitalize():
        print("True!\n")
    else:
        print("False!\n")          

# First, Last, and Middle Test Cases
first_letter("Cristiano Ronaldo") # Output: C
last_letter("Lionel Messi") # Output: i
middle_letter("Instagram") # Output: a

# Palindrome Test Cases
palindrome("noon") # True
palindrome("redivider") # True
palindrome("hello") # False
palindrome("a") # True
palindrome(" ") # True
