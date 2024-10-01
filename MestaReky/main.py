# Definice řek a jejich atributů
reky = {
    "Vltava": {
        "pramen": "Šumava",
        "mesta": ["České Budějovice", "Praha", "Mělník"]
    },
    "Labe": {
        "pramen": "Krkonošsko",
        "mesta": ["Hradec Králové", "Ústí nad Labem", "Děčín"]
    },
    "Morava": {
        "pramen": "Králíky",
        "mesta": ["Olomouc", "Zlín", "Brno"]
    }
}


# Funkce pro získání řeky podle města
def ziskat_reku_podle_mesta(mesto):
    reky_pro_mesto = []


for reka, info in reky.items():
    if mesto in info["mesta"]:
        reky_pro_mesto.append(reka)
        return reky_pro_mesto


# Funkce pro získání měst podle řeky
def ziskat_mesta_podle_reky(reka):
    if reka in reky:
        return reky[reka]["mesta"] + [reky[reka]["pramen"]]

else:
return []

while True:
    volba = input(
        "Zadejte město pro získání řeky nebo název řeky pro získání měst (nebo 'konec' pro ukončení): ").strip()

if volba.lower() == 'konec':
    break

# Zkontrolujeme, zda je volba město nebo řeka
if volba in [mesto for info in reky.values() for mesto in info["mesta"]]:
    reky_v_meste = ziskat_reku_podle_mesta(volba)
if reky_v_meste:
    print(f"Městem '{volba}' protékají řeky: {', '.join(reky_v_meste)}.")
else:
    print(f"Městem '{volba}' žádná řeka neprotéká.")
elif volba in reky:
mesta_reky = ziskat_mesta_podle_reky(volba)
print(f"Řeka '{volba}' protéká městy: {', '.join(mesta_reky)}.")
else:
print("Zadaná hodnota není platné město nebo řeka.")
