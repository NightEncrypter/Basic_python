# A block of code which only runs when it is called .In python, we do not use paranthesis and curly brackets, we use indentation with tabs or spaces

# Create func
def sayHello(name):
    """
    prints Hello and then name
    """
    print("hello " + name)


sayHello("manas")

# Return value
def sumFunc(m, n):
    return m + n


print(sumFunc(1, 5))


# A lambda function is a small anonymous function.
# A lambda function can take any no of arguments,but can only have one expression, Very similar to JS arrow functions


getSum = lambda num1, num2: num1 + num2
print(getSum(1, 3))
x = lambda y: y

print(x("manas"))
