# Tuples are immutable.
# Tuples are a fundamental collection type used for storing an 
# ordered sequence of items that should remain unchanged.
print("Creating Tuples")
birthday_date = (1981, "May", 12)
print(birthday_date)

# Tuple Unpacking
# Values will be assigned in the order they appear in the tuple.
year, month, day = birthday_date
print("\n", year, month, day)

#* operator in tuple unpacking is used to
#  gather multiple elements from the tuple into a LIST. 
scores = (96, 99, 91, 88, 64)
winner, *rest = scores
print("\n Winner:", winner, "\n Losers:", rest)

# winner --> LATEST or Index = 0 in the tuple
# *rest --> Rest of the items in the tuple
