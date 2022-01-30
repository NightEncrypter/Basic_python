# A  variable is a container for a value , which can be of various types

"""
This is a multiline comment or docstring ( used to define a functions purpose )
can be single or double quoates
"""

"""
VARIABLE RULES:
    --Variable names aree case sensitive (name and NAME are different variables)
    --Must start with a letter or an underscore
    --Can have numbers but can not start with one
"""

# x = 1  # int
# y = 2.5  # float
# name = "Manas"  # string
# is_cool = True  # bool


# Multiline Assigment
x, y, name, is_cool = (1.5, 2, "Manas", False)


# print(type(x))


# Basic Maths
a = x + y

print(a)
# Check type
print(type(a))


# Casting
print(int(a))  # float to int

x = str(x) #float to str
y = float(y)
is_cool = float(y)

print(type(x))
print(type(y))
print(type(is_cool), is_cool)
