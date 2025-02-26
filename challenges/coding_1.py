import math

def sphere_volume(radius):
  volume = (4/3) * math.pi * (radius ** 3)
  return volume

volume_result = sphere_volume(5)
print(f"#1: The volume of a sphere of 5 radius is {volume_result:.2f}")

def w_cost(copies):
    cover_price = 24.95
    discount = 0.40
    shipFirst = 3
    shipAfter = 0.75
    discount_price = cover_price * (1 - discount)
    total_book_cost = discount_price * copies
    total_shipping = shipFirst + (shipAfter * (copies - 1))
    total = total_book_cost + total_shipping
    return total
cost = w_cost(60)
print(f"#2: Your total is {cost:.2f}")
