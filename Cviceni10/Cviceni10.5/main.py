from audioop import reverse

zbozi = [
    {
        "name" : "IPHONE 14",
        "price" : 22169.0,
        "category" : (12, "Mobilní telefony")
    },
    {
        "name" : "Fujifilm XT30",
        "price" : 22269.0,
        "category" : (2, "Fotoaparáty")
    },
    {
        "name" : "Niceboy HIVE Pins Black",
        "price" : 999.0,
        "category" : (4, "Sluchátka")
    }
]

sorted_cena = sorted(zbozi, reverse=(True), key=lambda x: x["price"])
sorted_nazev = sorted(zbozi, key=lambda x: x["name"])
sorted_category = sorted(zbozi, key=lambda x: x["category"])

print(sorted_cena)
print(sorted_nazev)
print(sorted_category)