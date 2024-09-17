import math


def calculate_resistance(voltage, current):
    return voltage / current


def calculate_voltage(resistance, current):
    return resistance * current


def calculate_current(resistance, voltage):
    return voltage / resistance


def main():
    print("Ohmův zákon kalkulačka")

    while True:
        print("\n1. Výpočet odporu")
        print("2. Výpočet napětí")
        print("3. Výpočet proudu")
        print("4. Konec programu")

        volba = input("Zadejte číslo pro výběr: ")

        if volba == "4":
            break

        try:
            r = float(input("Zadejte hodnotu první veličiny: "))
            i = float(input("Zadejte hodnotu druhé veličiny: "))

            if volba == "1":
                result = calculate_resistance(r, i)
                print(f"Výsledná hodnota: {result} Ω")
            elif volba == "2":
                result = calculate_voltage(r, i)
                print(f"Výsledná hodnota: {result} V")
            elif volba == "3":
                result = calculate_current(r, i)
                print(f"Výsledná hodnota: {result} A")
            else:
                raise ValueError("Neplatná volba")
        except ValueError:
            print("Neplatný vstup. Prosím, zkontrolujte své údaje.")
        except ZeroDivisionError:
            print("Chyba: Nelze vypočítat nulový odpor!")
        except NotImplementedError:
            print("Tato funkce není implementována. Prosím, vyberte jinou možnost.")


if __name__ == "__main__":
    main()