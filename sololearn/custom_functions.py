# Basic Function Defintion
def greet(): 
    print("Hello from a Function\n")
    # Indentation is KEY in Python

# Function Call
greet()

# Functions MUST be *def*ined before being called



# Function w/ Arguments
def user_greeting(name, age):
    print("Hello!", name)
    print("You are", str(age), "Years Old!\n")

# Function Call, Passing in a name value using input()
user_greeting(input("What is your name?"), 16)




# Return Statements
def bmi(weight, height):
    index = weight / (height * height)
    return index, weight, height 
    # Additional Lines of code after Return will be ignored
    print("I got ignored!")

# Function Call w/ Return value & Multiple Variables
patient_5, p_weight, p_height = bmi(61, 1.83) 
print("BMI:", patient_5, "\nWeight:", p_weight, "\nHeight:", p_height, "\n")




# Function arguments with Default Values
def hello(book="Thief Of Always"):
    print("Welcome", book)

hello() # Displays 'Welcome Thief of Always'
hello("Blue Lock") # Displays 'Welcome Blue Lock'
