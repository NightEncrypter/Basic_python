obj1 = {"name": "manas", "age": 20}
obj2 = {"skills": ["react", "python"]}


# Combine two dict
obj3 = {**obj1, **obj2}
print(obj3)


# Combine two dict
res = obj1 | obj2

print(res, "combine dict")

# print(obj3.items())

# ITERATE DICT using items method
# for key, value in obj3.items():
#     print(key, value)

# ITERATE DICT using keys method
# for key in obj3.keys():
#     print(obj3[key],key)


# # Converting list to dict
# test_list = [{"Gfg": 3, 4: 9}, {"is": 8, "Good": 2}, {"Best": 10, "CS": 1}]

# # printing original list
# print("The original list : " + str(test_list))

# # dictionary comprehension encapsulating result as one liner
# res = {idx: val for idx, val in enumerate(test_list)}

# # printing result
# print("The constructed dictionary : " + str(res))


def helper_fnc(test_str, sep):
    if sep not in test_str:
        return test_str
    key, val = test_str.split(sep, 1)
    print(key, val, '"key-val"')
    return {key: helper_fnc(val, sep)}


# initializing string
test_str = "gfg_is_best_for_geeks"

# printing original string
print("The original string is : " + str(test_str))

# initializing separator
sep = "_"

# Convert String to Nested Dictionaries
# Using loop
res = helper_fnc(test_str, sep)

# printing result
print("The nested dictionary is : " + str(res))


strPara = test_str.split(sep, 1)
print(strPara)


# List of tuple to dict
d9 = {x: y for x, y in [("brad", "traversey"), ("dev", "ed")]}

print(d9)

# objDynamic={}
# for x,y in [("brad","traversey"),("dev","ed")]:
#     objDynamic[x]=y

# print(objDynamic)
# # List of tuple to dict
# d8={y["name"]:x for y, x in [{"name":"traversey"},{"name":"ed"}]}

# print(d8)
