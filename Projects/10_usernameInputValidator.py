print("-----Username Input Validator-----")

username = input("enter your username: ").strip()

if len(username) > 12:
    print("Registration Error! Username must not exceed 12 characters!")
elif not username.find(" ") == -1:
    print("Registration Error! Username must not contain spaces!")
elif not username.isalpha():
    print("Registration Error! Username must not contain numbers! ")
else:
    print(f"Congratulations! You are registered with {username} as your username.")