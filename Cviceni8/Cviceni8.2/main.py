from zlevnene_zbozi import ZlevneneZbozi

# Vytvoření instance třídy ZlevneneZbozi
zlevnene_zbozi = ZlevneneZbozi("ExampleProduct", 1000.0, 0.25)

# Výpis ceny po slevě
print(f"Cena po slevě: {zlevnene_zbozi.get_cena()}")