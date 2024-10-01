# Definice řek a jejich atributů
reky = {
"Vltava": {
"pramen": "Šumava",
"vliv": "Labe",
"pripojujici": ["Berounka", "Sázava"],
"pokracuje": True
},
"Labe": {
"pramen": "Krkonošsko",
"vliv": "Severní moře",
"pripojujici": ["Vltava", "Ohře", "Elbe"],
"pokracuje": True
},
"Morava": {
"pramen": "Králíky",
"vliv": "Dřevnice",
"pripojujici": ["Bečva", "Bystřice"],
"pokracuje": True
},
"Sázava": {
"pramen": "Sázavské hory",
"vliv": "Vltava",
"pripojujici": [],
"pokracuje": False
},
"Berounka": {
"pramen": "Křivoklátsko",
"vliv": "Vltava",
"pripojujici": [],
"pokracuje": False
},
"Ohře": {
"pramen": "Krušné hory",
"vliv": "Labe",
"pripojujici": [],
"pokracuje": False
}
}

# Funkce pro získání informací o řece
def ziskat_info_o_rece(reka):
if reka in reky:
info = reky[reka]
pripojujici = info["pripojujici"]
vliv = info["vliv"]
pokracuje = "pokračuje" if info["pokracuje"] else "zaniká"

print(f"Řeka: {reka}")
print(f" Pramení: {info['pramen']}")
print(f" Vlije se do: {vliv}")
print(f" Řeka {pokracuje} po spojení.")
if pripojujici:
print(f" Připojující se řeky: {', '.join(pripojujici)}")
else:
print(" Neexistují žádné připojující se řeky.")
else:
print("Zadaná řeka nebyla nalezena.")

# Hlavní část programu bez __main__
while True:
volba = input("Zadejte název řeky pro získání informací (nebo 'konec' pro ukončení): ").strip()

if volba.lower() == 'konec':
break

ziskat_info_o_rece(volba)
