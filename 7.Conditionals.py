# If/ else conditions are used to decide to do something based on someething being true or false

x, y = 5, 8
# Comparison opeartors ( ==.!=,>,<,>=,<=) used to compare values

# Simple if
if x == y:
    print(f"{x} is equal to {y}")
else:
    print(f"{x} is not equal to {y}")


# Simple if/else
if x > y:
    print(f"{x} is greater to {y}")
else:
    print(f"{x} is less to {y}")


# Simple if/else/elif
if x > y:
    print(f"{x} is greater to {y}")
elif x == y:
    print(f"{x} is equal to {y}")
else:
    print(f"{x} is less than {y}")


# Nested if

if x > 2:
    if x <= 10:
        print(f"{x} is greater than 2 & less than 10")


# Logical Operators (and,or,not) -Used to combine conditional statement

# and
if x > 2 and x <= 10:
    print(f"{x} is greater than 2 and less than 10")

# or
if x > 2 or x <= 10:
    print(f"{x} is greater than 2 OR less than 10")

# not
if not (x == y):
    print(f"{x} is not equal to {y}")


# Identity Operators (not,not in ) -Membership operators are used to test if a sequence is presented in object

numbers = [1, 2, 3, 5]
numbers2 = [1, 2, 3, 9, 7]

# in
if x in numbers:
    print(x in numbers)

# not in
if x not in numbers2:
    print(x not in numbers2)


# Identity operators (is ,is not)
# Compare the objects, not if they are equal ,but if they are actually the same object,  with the same  memory location

# is
if x is y:
    print(x is y)
    print("is")

# is not
if x is not y:
    print(x is not y)
    print("is not")
