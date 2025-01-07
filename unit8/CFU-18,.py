# Towaf Hossain
# PD 1-2
# 1/7/25

def v1():
    # Adds prices from a fixed list.
    prices = [1.95, 4.5, 0.99, 5.99]   
    total = 0
    
    for price in prices:
        total += price
    
    print("\nVersion 1: Fixed List")
    print(f"Prices: ${prices}")
    print(f"Total price: ${total}")


def v2():
    # Lets user input prices and calculates the total.
    prices = []
    total = 0
    
    user_items = int(input("How many prices do you want to add? "))
    
    for i in range(user_items):
        price = float(input(f"Enter the price for item {i + 1}: "))
        prices.append(price)

    for price in prices:
        total += price
        
    print("\nVersion 2: User Input List")
    print("Prices:", prices)
    print("Total price:", total)


def v3():
    # Asks for item names and prices, and generates a receipt.
    items = []
    prices = []
    user_items = int(input("How many items do you want to add? "))

    for i in range(user_items):
        item_name = input(f"Enter the name of item {i + 1}: ")
        item_price = float(input(f"Enter the price for {item_name}: "))
        items.append(item_name)
        prices.append(item_price)

    print("\nReceipt:")
    print("-" * 20)
    total = 0
    
    for i in range(user_items):
        print(f"{items[i]}: ${prices[i]:.2f}")
        total += prices[i]
    print("-" * 20)
    print(f"Total: ${total:.2f}")


def main():
    print("Choose a version to run:")
    print("1. Version 1: Add prices from a fixed list")
    print("2. Version 2: Add prices by user input")
    print("3. Version 3: Add items and prices, then generate a receipt")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        v1()
    elif choice == "2":
        v2()
    elif choice == "3":
        v3()
    else:
        print("Invalid choice. Please try again.")

main()
