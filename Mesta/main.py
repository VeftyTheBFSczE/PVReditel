Czechia = {
    "Jihocesky":"České Budějovice",
    "Jihomoravský kraj": ["Brno", "Blansko"],
    "Ustecky kraj": ["Ustí nad Labem" "Most"]
}
input_value = input("Zadejte název města nebo kraje: ")


if input_value in Czechia:
    print(Czechia[input_value])


else:
    found = False
    for region, cities in Czechia.items():
        if isinstance(cities, list) and input_value in cities:
            print(f"{input_value} se nachází v kraji: {region}")
            found = True
            break
    if not found:
        print("Město nebo kraj nebyl nalezen.")







