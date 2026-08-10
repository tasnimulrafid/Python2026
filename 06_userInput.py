# input() always returns string, if we need to perform any calculations, we must typecast it

username = input("what is your username? ")
print(f"Hello {username}")

num_input = input("enter a number: ")
print(type(num_input))

num = int(input("enter a number: "))
print(type(num))