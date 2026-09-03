# unordered: cannot be accessed by index, set[0] raises a typeerror
# duplicates are auto removed

colors = {"red", "green", "blue", "green"}

print(colors) # prints {'red', 'blue', 'green'}

# print(colors[0]) # raises TypeError: 'set' object is not subscriptable

# print(help(colors))  

# colors.pop() # removes a random elements from the list

colors.add("purple")
colors.remove("blue")
print(f"colors: {colors}")

cols = colors.copy()
print(f"cols: {cols}")

cols.add("magenta")

print(f"cols: {cols}")
print(f"colors: {colors}")

colors.clear() # clears the set

# print(cols)