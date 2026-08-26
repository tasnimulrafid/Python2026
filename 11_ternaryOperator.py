# X if condition else Y
# single line shortcut for if-else

num = int(input("enter a number: "))
print("even" if num % 2 == 0 else "odd")
result = "positive" if num > 0 else "negative"
print(result)

age = int(input("enter your age: "))
status = "adult" if age >= 18 else "child"
print(status)

user_role = input("type your role (admin or guest): ")
access_level = "full access" if user_role == "admin" else "limited access"
print(access_level)