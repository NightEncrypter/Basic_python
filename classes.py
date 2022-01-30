# A class  is like a blueprint for creating object .An object has properties and methods(functions) associated with it. Almost everything in python is an object


class User:
    # Construtor
    def __init__(self, name, email, age) -> None:
        self.name = name
        self.email = email
        self.age = age

    # set user greeting
    def greeting(self):
        return f"my name is {self.name} and i am {self.age}"

    # birthday age change
    def has_birthday(self):
        self.age += 1


# Init user object
brad = User("Brad Traversey", "brad@gmail.com", 40)
print(brad.name)
print(brad.age)
print(brad.email)
# Edit property

brad.age = 50
print(brad.age)


janet = User("Janet Traversey", "janet@gmail.com", 20)
print(janet.name)
# Call method
print(janet.greeting())
print(janet.has_birthday())
print(janet.greeting())


# Customer
class Customer(User):
    def __init__(self, name, email, age) -> None:
        self.name = name
        self.email = email
        self.age = age
        self.bal = 0

    # set bal method
    def set_bal(self, bal):
        self.bal = bal

    def greeting(self):
        return f"my name is {self.name} and i am {self.age} and i owe a balance of {self.bal}"


# Init customer
maria = Customer("maria", "maria@gmail.com", 20)

print(maria.name)

# set balance from method
maria.set_bal(200)

print(maria.bal)  # set bal to 200
print(maria.greeting())
