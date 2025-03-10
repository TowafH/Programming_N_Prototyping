# Towaf Hossain
# PD 1-2
# 3/10/25

def is_triangle(n1, n2, n3):
    if n1 == n2 and n2 == n3 and n1 == n3:
        print("Yes")
    else:
        print("No")

def prompt():
    user1 = int(input("Enter #1"))
    user2 = int(input("Enter #2"))
    user3 = int(input("Enter #3"))
    is_triangle(user1, user2, user3)
    
prompt()
