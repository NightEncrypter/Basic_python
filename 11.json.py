# JSON is commonly used with data APIS. Here how we can parse JSON into aa python dictionary

from json import loads, dumps

# Sample JSON
userjson = '{"firstname":"John","lastname":"Doe","age":25}'

# json to dict
user = loads(userjson)
print(user["firstname"], user["age"])
print(user)


# Sample of dict
user2 = {"firstname": "William", "lastname": "Doe", "age": 25}

# Object to json
user2Json = dumps(user2)


print(user2Json)
