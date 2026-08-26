stringToCheck = input("enter a string to check if it's palindrome: ").strip()

reversedString = stringToCheck[::-1]

if stringToCheck.lower() == reversedString.lower():
    print(f"{stringToCheck} is a palindrome!")
else:
    print(f"{stringToCheck} is not a palindrome:(")