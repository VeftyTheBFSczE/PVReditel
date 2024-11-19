def generatorRaselinnaJezeraCR():
    yield "Černé jezero"
    yield "Čertovo jezero"
    yield "Jezero Laka"
    yield "Mrtvé jezero"
    yield "Velké mechové jezírko"

print("Rašelinná jezera v ČR")
for jezero in generatorRaselinnaJezeraCR():
    print(jezero)