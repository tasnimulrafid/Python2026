import math

print("-----Area of Circle Calculator-----")
raidus = float(input("enter radius: "))

area = math.pi * pow(raidus, 2)
print(f"Area of the circle {round(area, 2)} m")