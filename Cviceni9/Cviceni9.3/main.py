def generatorITVelikanu():
    velikani = ["Alan Turing", "Ada Lovelace", "Tim Berners-Lee"]
    for osoba in velikani:
        yield osoba

print("Velikani v IT")
for osoba in generatorITVelikanu():
    print(osoba)