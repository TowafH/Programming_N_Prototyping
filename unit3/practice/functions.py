# def --> Function Definition
# multi_function --> Function Name
# x,y --> Parameters
# : --> Required Colon
# Indents --> Required
def mult_function(x,y):
    z = x*y # Operation
    print("I Heart Math")
    return z # Return Statement

# 5,4 --> Arguments
print(mult_function(5,4))

def my_first_func():
    print("Testing...")
    print("It works!")
    
my_first_func()

input_name = input("Enter Name")

def happy_bday(name):
    print("Happy Birthday", name)
    
happy_bday(input_name)
happy_bday("Ramirez")

def mult_2_nums(num1, num2):
    print(num1 * num2)
    
mult_2_nums(5,4)
mult_2_nums(10, -3.5)

def find_rect_area(w, l):
    area = w*l
    print("Calculating Area...")

answer = find_rect_area(4,7)
print(answer)
