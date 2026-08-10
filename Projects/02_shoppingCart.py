print("-------Simple Shopping Cart--------")

item = input("What item would you like to buy? ")
price = float(input("What is the price of the item? $"))
quantity = int(input("How many would you like to purchase? "))

total = price * quantity

print("\n" + "="*30)
print(f"You have bought {quantity} {item}(s)")
print(f"Your total is: ${total:.2f}")
print("="*30)