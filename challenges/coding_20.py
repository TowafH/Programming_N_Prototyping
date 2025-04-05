# Towaf Hossain
# PD 1-2
# Python Coding Challenge 20
'''
This program prompts the user to enter a set of forbidden letters and five words, 
then checks each word to see if it contains any forbidden letters, printing a 
message for each word.
'''
def avoids(s, f):
    for i in range(len(s)):
        if s[i] in f:
            return f"'{s[i]}' is forbidden from the set '{f}'\n"
    return "No forbidden letters found\n"

def user():
    f_input = input("Enter a string of forbidden letters: ")
    words = []

    for i in range(5):
        s_input = input("Enter a word: ")
        words.append(s_input)
    for i in words:
        print(f"Checking word: '{i}'")
        print(avoids(i, f_input))

user()
