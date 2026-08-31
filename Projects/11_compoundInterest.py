print("----- Compound Interest Calculator -----")

while True:
    principle = float(input("enter the principle amount: "))
    if principle > 0:
        break
    print("Validation Error: Principle amount must be greater than zero")

while True:
    rate = float(input("enter the rate of interest (annual %): "))
    if rate >= 0:
        break
    print("Validation Error: Rate of interest cannot be negative")

while True:
    time = float(input("enter duration (in years): "))
    if time > 0:
        break
    print("Validation Error: Investment time must be greater than zero")

total = principle * pow((1 + rate/ 100 ), time)
ci = total - principle

print("\n" + "="*40)
print(f"Calculated savings after {time} years: {total:,.2f}")
print(f"Earned compound interest = {ci:,.2f}")
print("\n" + "="*40)