prompt = int(input("How many numbers do you need to check? "))

divisible = 0
not_divisible = 0

for i in range(prompt):
    num = int(input("Enter a number: "))
    
    if num % 3 == 0:
        print(f"{num} is divisible by 3.")
        divisible += 1 
    else:
        print(f"{num} is not divisible by 3.")
        not_divisible += 1  

print(f"You entered {divisible} number(s) that are divisible by 3.")
print(f"You entered {not_divisible} number(s) that are not divisible by 3.")
