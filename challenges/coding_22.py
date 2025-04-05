# Towaf Hossain
# PD 1-2
# PY Challenge 22
'''
This program checks if words contain all required letters and counts
how many in a given list include all the vowels (a, e, i, o, u) or 
all vowels plus y.
'''

# Function to check if a word contains all required letters
def uses_all(word, required):
    # Loop through each letter in the required letters string
    for i in required:
        # If any required letter is not found in the word, return False
        if i not in word:
            return False
    # If all required letters are found in the word, return True
    return True

word_list = [
    "education", "house", "facetiously", "beautiful", "quiet",
    "sequoia", "audiovisual", "abstemious", "rhythm", "automobile"
]

# Function to count how many words contain all the required letters
def count_words_with_all_vowels(words, required_letters):
    count = 0  # Tracker
    # Loop through each word in the word list
    for i in words:
        # If the current word contains all required letters, increment the counter
        if uses_all(i, required_letters):
            count += 1
    # Return the total count of words that match the criteria
    return count

# Num of words that with all vowels (a, e, i, o, u)
print("Words with all vowels (a, e, i, o, u):", count_words_with_all_vowels(word_list, "aeiou"))
print("Words with all vowels (a, e, i, o, u, y):", count_words_with_all_vowels(word_list, "aeiouy"))
