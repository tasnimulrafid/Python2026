stringToCheck = input("enter a string to check if it is palindrome or not: ").strip()

revString = stringToCheck[::-1]

if stringToCheck.lower() == revString.lower():
    print(f"{stringToCheck} is a palindrome.")
else:
    print(f"{stringToCheck} is not a palindrome.")