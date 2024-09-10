import math
import cmath


a = int(input("Zadejte koeficient a: "))
b = int(input("Zadejte koeficient b: "))
c = int(input("Zadejte koeficient c: "))

try:
    diskriminant = b**2 - 4*a*c
    if diskriminant < 0:
        raise ValueError("Diskriminant je zaporny")

    x1 = (-b + math.sqrt(diskriminant))/(2*a)
    x2 = (-b - math.sqrt(diskriminant))/(2*a)

except ValueError:
    x1 = (-b + cmath.sqrt(diskriminant)) / (2 * a)
    x2 = (-b - cmath.sqrt(diskriminant)) / (2 * a)
    print("resime v komplexnich cislech")

else:
    print("resime v celych cislech")

finally:
    print(f"vysledek: x1 je = {x1} x2 je {x2}")




