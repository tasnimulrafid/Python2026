# strings are immutable sequence of characters

name = "rafid"
print(name[0]) # this is possible

# name[0] = "T" # this is not possible as strings are immutable
name = "tasnimul"

capitalizedName = name.capitalize()
print(capitalizedName)
print(name.upper())

print(name.find("m"))
print(name.find("T")) # prints -1 as it does not contain the capital T

helloStr = "hello world"
print(helloStr.rfind("l"))
print(len(helloStr)) # prints total count of characters, including spaces
print(f"No of l's: {helloStr.count("l")}")

phone = "01797-830128"

print(phone.replace("-", ""))