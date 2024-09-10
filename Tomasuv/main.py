import math
from math import sqrt


while True:
    try:
        L = int(input("Zadej indukcnost [H]:"))
        C = int(input("Zadej kapacitu [F]:"))
        F = 1 / (2 * 3.14 * math.sqrt(L * C))
        if L < 0 or C < 0:
            raise ValueError



        print("Frekvence je: " + str(F) + "Hz")
        break
    except ValueError:
        print("spatne cislo nebo znak napiste znovu")
    except ZeroDivisionError:
        print("Cislo nesmi byt nula")




