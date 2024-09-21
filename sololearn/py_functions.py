# .lower() 
# .upper()
print(".lower() & .upper()\n")
print('sMaRtPhOnE'.lower())
print('sMaRtPhOnE'.upper())

# sMaRtPhOnE --> String
# . --> Dot
# lower() --> Function

# .capitalize()
print("\n.capitalize()")
print("happy birthday".capitalize())

# .find() --> Returns INDEX # in the String
print("\n.find()")
print("Bee".find("e"))

# .count() --> Returns AMOUNT of an item within a list
print("\n.count()")
scores = [7, 9, 10, 7, 7, 11, 133]
print(scores.count(7))

#.append() --> Adds a new item to the END of a list
#.append() --> Strings are IMMUTABLE, will not append to strings
print("\n.append()")
songs = ["Rats", "Heatwaves"]
songs.append("SPECIALZ")
print(songs)

#.pop() --> Removes an element from a list
# The index is the only accepted argument
# variable_name.pop(1)
print("\n.pop()")
books = ["Thief of Always", "Blue Lock", "Jujutsu Kaisen"]
books.pop(0)
print(books)
print(books[1])

#.insert() --> Add element to a SPECIFIC position in a list
# 2 Required Arguments
# insert(index, item) (string/bool/num)
print("\n.insert()")
items = ["Book", "Pen", "Pencil"]
items.insert(2, "marker")
print(items)
print(items[2])


#len() --> Returns AMOUNT of items in a list  *NO DOT NOTATION
print("\nlen()")
movies = ["Shang Chi", "Your Name"]
print(len(movies))

#max() --> Returns HIGHEST NUMBER in a list *NO DOT NOTATION
print("\nmax()")
points = (12, 14, 19, 3, 5)
winner = max(points)
print(winner)
