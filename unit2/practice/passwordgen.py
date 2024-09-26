import random

# Random
num_100 = random.randint(1,100)

# Lists
animal = ["Dog", "Cat", "Mouse", "Rabbit", "Horse"]
number = [999, 555, 444, 333, 222, 111, 888]

# Inputs
input_animal = input("Enter an Animal: ")
input_number = int(input("Enter a Number: "))

# Add Items to list
animal.append(input_animal)
number.append(input_number)

# Display Password
print("Your password is:", str(num_100) + random.choice(animal) + str(random.choice(number)))
