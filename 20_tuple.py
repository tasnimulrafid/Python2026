# immutable: cannot be chaged after creation

roommates = ("samim", "siam", "sakib")

# print(help(roommates)) 

print(roommates.count("siam"))
print(roommates.index("sakib"))

print(roommates[0])

# roommates.add("sifat") # AttributeError: 'tuple' object has no attribute 'add'
# adding, removing, popping, clear  etc are not allowed