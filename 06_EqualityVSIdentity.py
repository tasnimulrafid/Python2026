# == asks if these two variables hold equal values
# is asks if these two variables points to the exact same object in memory

list_a = [1, 2, 3]
list_b = [1, 2, 3] # list_b is a separate object from list_a with the same contents

list_c = list_a # list_c is the same object as list_a

print(list_a == list_b) # True (same values)
print(list_a is list_b) # False (not same objects in memory)
print(list_a is list_c) # True (same object)