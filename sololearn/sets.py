# Sets --> UNORDERED Collections
# Sets --> IGNORES duplicate items
# Sets --> Mutable
# Sets --> Cannot use .append() b/c Sets are UNORDERED Collections
# Sets --> Functions: .add() || .remove() || .clear || .union() || .difference()
# Sets --> Created using Curly Brackets {}
guests = {1, 2, 3, 4}

# Sets --> CANNOT be Indexed, results in an Error
# print(guests[0])


# Sets CANNOT have duplicate items
# The duplicate item will be ignored
# print(guests)



# Items can be added/removed from Sets using .add() || .remove()
guests.add(5)
print("Add 5:", guests)
guests.remove(1)
print("Remove 1:", guests, "\n")

# Sets can be combined using .union()
set1 = {777, 555}
set2 = {888, 999}
combine_sets = set1.union(set2)
print("Combination of set1 & set2:", combine_sets, "\n")

# Sets can be differenced using .difference()
# The sets are compared
# set3 is compared to set4
# set3 & set4 have "Basketball", it is removed from the output
# set3 has Soccer, while set4 doesn't have it. {'Soccer'} --> Output
# variable_name.difference(argument_var_name)
# variable_name --> Dominates argument_var_name
set3 = {"Soccer", "Basketball"}
set4 = {"Basketball", "Volleyball"}
unique_sets = set3.difference(set4)
print("Difference of set3 & set4", unique_sets)
