# Towaf Hossain
# PD 1-2
# Python Coding Challenge 21
'''
This program checks if a given word contains only letters 
from a specified set of allowed letters and returns a message accordingly.
'''
def uses_only(word, allowed_letters):
    for letter in word:
        if letter not in allowed_letters:
            return False  # Found a letter not in the allowed set
    return True  # All letters are in the allowed set

def user():
    allowed_letters = input("Enter allowed letters: ")
    word = input("Enter a word to check: ")
    
    # Check if the word uses only the allowed letters
    result = uses_only(word.lower(), allowed_letters.lower())
    if result:
        print(f"The word '{word}' uses only the allowed letters.")
    else:
        print(f"The word '{word}' contains forbidden letters.")

# Run the test function
user()
