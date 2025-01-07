groceries = ["Eggs", "Apples", "Milk", "Bread"]
students = ["Brithany", "Rohaan", "Jannatul", "Aliyah", "David", "Micah", "Armina", "Tasfia", "Rafael", "Nabila", "Nataly", "Michael", "Betsy", "Devesh", "Towaf", "Vashti", "Syeda"]
ages = [17.1, 16.6, 16.2, 16.1, 17.2, 16.4, 16.1, 16.2, 17.2, 16.5, 16.1, 16.3, 16.2, 16.1, 16.6, 17.4, 16.5]
# I'm 16.6 years old

# Printing individual indices
print(groceries[0])
print(str(students[0]) + " is " + str(ages[0]) + " years old\n")

# Printing Ranges
print(groceries[0:3])
print(str(students[1:5]) + " are " + str(ages[1:5]) + " years old, respectively")

# For Loop
print("")
for i in range(len(students)):
    print(f"{i}: {students[i]} is {ages[i]} years old")
