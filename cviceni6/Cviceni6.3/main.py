def formatuj_prijimeni_prvni_jmeno(prijimeni, jmeno):
    return f"{prijimeni.upper()}, {jmeno.capitalize()}"
formatuj_prijimeni_prvni_jmeno("Novák", "jan")

def formatuj_monogram(prijimeni, jmeno):
    return f"{prijimeni[0].upper()} {jmeno[0].upper()}."
formatuj_monogram("Novák", "jan")

def vyber_formatovani_funkci(delka):
    if delka < 4:
        return formatuj_monogram
    else:
        return formatuj_prijimeni_prvni_jmeno

formatovac = vyber_formatovani_funkci(3)
print(formatovac("Jan", "Novak"))  # Výstup: J.N.

formatovac = vyber_formatovani_funkci(155)
print(formatovac("Jan", "Novak"))