import math

print("-----Calculate Hypotenuse of a Right Triangle-----")

side_a = float(input("enter length of side a: "))
side_b = float(input("enter length of side b: "))

hypotenuse = math.sqrt(pow(side_a, 2) + pow(side_b, 2))

print(f"Hypotenuse of that triangle is {round(hypotenuse, 2)} unit² ")