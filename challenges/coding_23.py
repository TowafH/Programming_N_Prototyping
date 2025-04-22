# Towaf Hossain
# PD 1-2
# 4/22/2025
'''
This program counts how many words in a list are abecedarian, 
meaning their letters appear in alphabetical order. It uses a
built-in Python function to check each word and prints the total count.
'''

def is_abecedarian(s):
    if sorted(s) == list(s):
        return True
    else:
        return False

words = ["abc", "aeg", "boat", "almost", "ghost", "act", "loop", "billowy", "chimps", "biopsy", "ad"]

count = 0
for i in words:
    if is_abecedarian(i) == True:
        count += 1

print("Total abecedarian words:", count)
