import math

radius = float(input("Enter radius of the circle: "))
area = math.pi * math.pow(radius, 2)
circumference = 2 * math.pi * radius
area_sqrt = math.sqrt(area)

print("Area of circle:", area)
print("Circumference:", circumference)
print("Square root of area:", area_sqrt)
