# maintain chronological order indexing, slicing, iteration
fruits = ["banana", "mango", "apple", "banana"]
print(f"second item on the list: {fruits[1]}") # accessing by index is allowed

# print(help(fruits)) # prints the allowed method on list "fruits"

# fruits.append("pineapple")
# print(fruits)

# fruits.pop()
# print(fruits)

# fruits.remove("apple")
# print(fruits)

# fruits.insert(0, "cherry")
# print(fruits)

# fruits.sort()
# print(fruits)

# fruits.reverse()
# print(fruits)

# print in reverse sorted order
# fruits.sort()
# fruits.reverse()
# print(fruits)

print(f"no of banana on the list: {fruits.count("banana")}")
print(fruits.index("banana")) # return the index of first occurance