# A dic is a collection which is unordered ,changeable and indexed No duplicate members

# Simple dic
# person = {"firstname": "john", "lastname": "doe", "age": 21}


# Using constructor
person = dict(firstname="manas", lastname="rathore", age=23)


# Access get specific value
print(person["firstname"])

# Access using get specific value
print(person.get("firstname"))

# Add Key/value
person["phone"] = "123-456-789"

# Get item
print(person.items())

# Get key
print(person.keys())


# Make a copy
person2 = person.copy()
person2["city"] = "Bhopal"

# Remove a item
del person2["age"]

# Remove a item

person2.pop("phone")
# Get len
print(len(person))

# Clear dic
# person2.clear()

# List of dict
peoples = [
    {"name": "Martha", "age": 20},
    {"name": "Mary", "age": 21},
    {"name": "Many", "age": 22},
    {"name": "Michael", "age": 14},
    {"name": "jenny", "age": 28},
]

print(peoples[1]["name"])
# print(person2)
