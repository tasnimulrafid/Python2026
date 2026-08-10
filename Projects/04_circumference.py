import math

print("----------Circumference Calculator----------")
radius = float(input("enter radius: "))

circumference = 2 * math.pi * radius

print(f"Circumference of the circle: {round(circumference, 2)}")