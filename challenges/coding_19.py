# Towaf Hossain
# PD 1-2
# Python Coding Challenge 19
'''
This program calculates the percentage of words that 
do not contain the letter 'e' and prints the list of
words that do not contain 'e'
'''
def has_no_e(word):
    for i in range(len(word)):
        if word[i] == "e":
            return False # Word contains 'e'
    return True # Word doesn't contain 'e'

def filter_words_without_e(words):
    # Length of the list
    num_words = len(words)
    # No 'e' list
    no_e_list = []
    
    # Iteration
    for i in range(num_words):
        if has_no_e(words[i]) == True:
            no_e_list.append(words[i])

    # Number of letters w/o the letter 'e'
    no_e_num = len(no_e_list)

    # Calculate Percentage
    if num_words == 0:
        no_e_word_percentage = 0
    else:
        no_e_word_percentage = (no_e_num / num_words) * 100

    print(f"{no_e_list}")
    print(f"{no_e_word_percentage:.2f}% of words don't contain the letter 'e'")
        
                  
filter_words_without_e(["A", "small", "dog", "ran", "fast.", "A", "boy", "saw", "it", "and", "ran", "after", "the", "dog"])

