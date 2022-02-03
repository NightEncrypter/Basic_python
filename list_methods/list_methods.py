from functools import reduce


fruits = [
    {"name": "mango", "price": 25, "day": "monday"},
    {"name": "orange", "price": 14, "day": "tuesday"},
    {"name": "banana", "price": 17, "day": "tuesday"},
    {"name": "strawberry", "price": 16, "day": "friday"},
    {"name": "pineapple", "price": 26, "day": "friday"},
]
fruitsTuple = (
    {"name": "mango", "price": 25},
    {"name": "orange", "price": 14},
    {"name": "banana", "price": 17},
    {"name": "strawberry", "price": 16},
    {"name": "pineapple", "price": 26},
)

fruitsDict = {"mango": "1kg", "orange": "2kg"}


# #Todo Map method
def mapper(x):
    return x["day"]


fruitsMapped = list(map(mapper, fruits))
print(fruitsMapped)

# Using lamba func
fruitsMapped = list(map(lambda x: x["name"], fruits))

print(fruitsMapped)

# Todo  Filter
def filterer(x):
    return x["price"] > 20 and x["day"] == "friday"


fruitsFiltered = list(filter(filterer, fruits))

# Using lamba func
fruitsFiltered = list(filter(lambda x: x["name"] == "mango", fruits))
print(fruitsFiltered)

nums = [1, 2, 3]

# TODO Reduce
def reducer(x, y):
    return x + y["price"]


sumer = reduce(reducer, fruits, 0)

print(sumer, "reducer")

# using def
print(reduce(lambda acc, y: acc + y["price"], fruits, 0))
grades = [
    {
        "subject": "math",
        "grade": 97,
    },
    {
        "subject": "chemistry",
        "grade": 60,
    },
    {
        "subject": "grammar",
        "grade": 75,
    },
]

# print(reduce(lambda x, y: x + y, map(lambda s: s["grade"], grades)))


# TODO ADD TWO LISTS
var1 = [1, 2, 3]
var2 = [2, 8, 9]


# METHOD-1
var3 = [*var1, *var2]
print(var3,"cobine")

# METHOD-2
var4 = var1 + var2

# Method-3
# using list.extend() to concat
var1.extend(var2)

# print(var1.slice())

print(str(var3))
print(var3)
print(var4)


# Initializing list of dictionaries
lis = [
    {"name": "Nandini", "age": 20},
    {"name": "Manjeet", "age": 20},
    {"name": "Nikhil", "age": 17},
]

print("The list printed sorting by age: ")


# Sorting the list in name and age
sortedList = sorted(lis, key=lambda i: (i["age"]))


print(sortedList)

# print(str(lis))
