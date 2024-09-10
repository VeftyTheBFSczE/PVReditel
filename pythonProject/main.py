try:

    x = input("Zadej cislo: ")
    y = int(x) + 1
    print(y)

except ValueError:
    print("Neni to integer")
