class GeneratorKrasovychJezer:
    jezera = [
        ["Dyje", ["Křivé jezero", "Květné jezero", "Kutnar", "Mahenovo jezero"]],
        ["Labe", ["Babinecká tůň", "Hrbáčkovy tůně"]],
        ["Bílina", ["Komořanské jezero"]],
        ["(bez řeky)", ["Antošovické jezero", "Holásecká jezera", "Krňák", "Kurfürstovo rameno", "Malá říčka", "Podhradská tůň"]]
    ]

    def __init__(self):
        self.i = 0
        self.j = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > (len(GeneratorKrasovychJezer.jezera) - 1):
            raise StopIteration()

        pomocnaPromenna = GeneratorKrasovychJezer.jezera[self.i]
        self.i = self.i + 1
        return pomocnaPromenna


for jezero in GeneratorKrasovychJezer():
    print(jezero)