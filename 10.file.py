# Python has function for creating, reading, updating, and deleting files

# Open a file
myFile = open("test.txt", "w")

# Get some info
# print("Name: ", myFile.name)
# print("Is closed: ", myFile.closed)
# print("Openning Mode: ", myFile.mode)
# print("Name: ", myFile)


# Write to file
myFile.write("I love python")
myFile.write(" and Javascript")
myFile.close()


#  Append to file
myFile = open("test.txt", "a")
myFile.write(" I also like PHP")
myFile.close()


# Read from file
myFile = open("test.txt", "r+")
text = myFile.read(100)
print(text)


# print("Name: ", myFile.name)
# print("Is closed: ", myFile.closed)
# print("Openning Mode: ", myFile.mode)
# print("Name: ", myFile)
