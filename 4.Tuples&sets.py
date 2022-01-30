# A tuple is a collection which is ordered and unchangeable. Allows duplicate members

# Simple tuple

fruits_tuple = ("Apple", "Orange", "Mango")

# using constructor
animals = tuple(("Donkey", "Horse", "Rhino", "Dog", "Giraffe"))
print(fruits_tuple)

print(animals)

# Get single value
print(animals[2])

# Cannot change value
# animals[2]="owl"

# Tuples with on value should trailling comma
fruits_tuple2 = ("Apple",)
print(fruits_tuple2)

# Get len of tuple
print(len(fruits_tuple2))

del fruits_tuple2
# print(fruits_tuple2)


# SETS
# A set is collection which is unordered and unindexed .No duplicate memebers.

# box={"Apple","Banana"}

# Using constructor
box = set(("mango", "banana", "orange", "mango"))  # no duplicate members


# Check if in set
if "mango" in box:
    print("yes mango is there")
else:
    print("no")

# Add to set
box.add("pineapple")

# Remove in set
box.remove("mango")

# Clear set
# box.clear()

# Complete delete
# del box
# print(box)


print(box)
