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

print(reduce(lambda x, y: x + y, map(lambda s: s["grade"], grades)))  # 232
