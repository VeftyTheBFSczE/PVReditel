print("Krasjova jezera v CR")


def generatorKrasovychJezerCR():
    try:
        yield "Horní macošské jezírko"
        yield "jezírko v Hranické propasti"
        yield "Další krasové jezírko"
    except GeneratorExit:
        print("!Generovani preruseno!")


jezera = generatorKrasovychJezerCR()

while True:
    try:
        jezero = next(jezera)
        if jezero == "jezírko v Hranické propasti":
            break
        else:
            print(jezero)
    except StopIteration:
        break
