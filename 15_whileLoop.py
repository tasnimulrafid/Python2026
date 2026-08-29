name = input("enter your name: ")

while name == "":
    print("you did not entered your name!")
    name = input("enter your name: ")
print(f"Hello, {name}")