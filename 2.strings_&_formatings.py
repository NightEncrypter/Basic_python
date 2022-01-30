# String in python are surrounded by either single or double quotation marks. Let's look at string formating and some string methods

name = "Manas"
age = 17

# Concatenate
print(
    "Hello World " + name + " and i am " + str(age)
)  # we have to cast and then concate


# String Formating
print()

# Arguments by position
print("{2},{1},{0}".format("a", "b", "c"))

# Arguments by name
print("My name is {name} and i am {age}".format(name="Manas", age=21))

# F-string
print(f"My name is {name} and i am {age}")


# String Methods
s = "hello There world"

# Catipatlize First Lettter
print(s.capitalize())

# Make All Uppercase
print(s.upper())

# Make All Lowercase
print(s.lower())

# Swapping the letters
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace("hello", "Hey"))

# Count all letter in a string
sub = "h"
print(s.count(sub))

# Starts with
print(s.startswith("hello"))

# ends with
print(s.endswith("ld"))

# Split into a list
print(s.split())


# Find position of letter
print(s.find("o"))

b = "manas"
# Is All alphanumeric
print(b.isalnum())

# # Is All alphabetic
print(b.isalpha())

# # Is All numeric
print(b.isnumeric())

# print(b.center())
