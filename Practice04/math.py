import math

#1 Degree to radians
degree = int(input("Input degree: "))
radians = math.radians(degree)

print(radians)

#2 Area of the trapezoid
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
area = ((base1 + base2) / 2 )* height

print(area)

#3 Area of the polygon
sides = int(input("Number of sides: "))
length = int(input("Length of the side: "))
area = (sides * length ** 2) / (4 * math.tan(math.pi / sides))

print(round(area))

#4 Area of the parralelogram
base = float(input("Base of parralelogram"))
h = float(input("Height of parralelogram"))
area = base * h

print(area)
