# name = input("enter your name: ")

# while name == "":
#     print("you did not entered your name!")
#     name = input("enter your name: ")
# print(f"Hello, {name}")


# age = int(input("enter your age: "))

# while age < 0 or age == " ":
#     print("Age cannot be negative!")
#     age = int(input("enter your age: "))
# print(f"You are {age} years old.")


food = input("enter a food you like (Q to quit) ")

while not food.upper() == "Q":
    print(f"You like {food}")
    food = input("enter a food you like (Q to quit) ")
print("Bye bye!")