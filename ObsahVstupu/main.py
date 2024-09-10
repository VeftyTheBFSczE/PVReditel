import math

radius =  float(input("Type the radius of the circle: "))
if radius <= 0:
    raise ArithmeticError("Only numbers that are positive")


area = math.pi * radius**2
print("The area of the circle is:", area)




