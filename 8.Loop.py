# A for loop is used for iterating over a sequence ( that is either a list ,a tuple,a dictionary,a set,or a string)


peoples = ["John", "Will", "Janet", "Carol"]

animals = ["donkey", "monkey", "lion"]

# for people in peoples:
#     print(people)


# # break the loop
# for people in peoples:
#     print(people)
#     if people=="Will":
#         break

# skip the loop the loop
for people in peoples:
    if people == "Will":  # skip will in a loop
        continue
    print(people)


# Range
for i in range(len(animals)):
    print(animals[i])


# Range
for i in range(0, 11):
    print(i)

# While loops execute a set of statments as long as a condition is true
x = 0
while len(peoples) - 1:
    print(peoples[x])
    x = x + 1
