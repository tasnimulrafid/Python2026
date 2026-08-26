credit_card = input("enter your credit card number: ")

last_four = credit_card[-4:]

masked_number = "XXXX-XXXX-XXXX-"+ last_four

print(f"you credit card number is: {masked_number}")