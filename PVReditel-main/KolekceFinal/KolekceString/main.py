#Je zachovano poradi ve kterem jsou prvky kolekce vkladany?
text = "ahoj"
for i in range(len(text)):
    print(f"Index {i}: {text[i]}")
#Jsou hodnoty ulozene v serazenem poradi od nejmensiho po nejvetsi
text1 = "2,4,10,3"
print(text1)
#Je mozne ulozit dva stejné prvky?
text2 = "10, 10"
print(text2)
# Je mozne vlozit hodnotu None
text3 = None #uz neni string
text35 = "None"
print(text3, text35)
# Je možné kolekce vnořovat, tedy vložit jako prvek kolekce další kolekci s několika prvky
text4 = "Ahoj", text3
print(text4)
# Je možné za běhu programu změnit  velikost kolekce
text = "ahoj"
novy_text = text.replace("h", "")
print(novy_text) #Neni tam funkce na to
# Jakým způsobem zjistím počet prvků v kolekci?
print(len(novy_text))
# Jakymi všemi metodami je možné vložit nový prvek do kolekce a jaké mají tyto metody vstypy?
print(dir(novy_text))
#
text = "ahoj"
novy_text = text.replace("h", "ooj")  # timto se da teoreticky vlozit novy prvek
print(novy_text)
#
text = "ahoj"
obsahuje = "ahoj" in text #Vypise True
print(obsahuje)
index = text.find("svět")
print(index) # vystup -1 protoze neobsahuje
try:
    index = text.index("světe")
    print(index)
except ValueError:
    print("neni") #vystup neni
#
text = "ahoj"
treti_znak = text[2]
print(treti_znak)