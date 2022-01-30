# A list is a collection which is ordered and changeable. Allows duplicate members


numbers = [1, 2, 3, 4, 5, 6]


# Using a constructor
numbers2 = list((1, 5, 6))
fruits = ["Apples", "Grapes", "Pears", "Guavas", "Mangoes"]

# Get specific value by index
print(fruits[0])

# Get Len of list
print(len(numbers2))

# Append to list
fruits.append("pineapples")
print(fruits)

# Remove a specific value of list
fruits.remove("Grapes")
print(fruits)

# Insert into a specific position
fruits.insert(2, "Strawberry")
print(fruits)

# Remove from postion
fruits.pop(1)  # pears is gone
print(fruits)

# Reverse a list
fruits.reverse()
print(fruits)

# Sorted
fruits.sort()
print(fruits)

# Reverse sort
fruits.sort(reverse=True)
print(fruits)
