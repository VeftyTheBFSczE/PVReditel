

#tady ze nemeni poradi
thistuple = ("apple", "banana", "cherry", "apple")
print(thistuple)
print(len(thistuple))
#Tady dokazuju ze nemuzu menit hodnoty za behu v tuple
""" try:
    print(thistuple[0])
    thistuple[0] = 5
except IndexError:

 print(len(thistuple))
"""

#tady dokazuju ze se da pomoci indexu zjistit hodnota
thistuplee = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuplee)
x = thistuplee.index(8)

print(x)

#Tady dokazuju ze se da do kolekce dat kolekce
thistupleee = (thistuple, "ahoj")
print(thistupleee)
#tady ze se da dat list do kolekce


#nejde to pridat dukaz
#thistuple.append(32)

#metody ktere jdou overit jestli obsahuje nejaky prvek
tuple = (1,2,3,4,5,6,5,5)
kontrola = 6 in tuple
kontrola2 = 7 in tuple
print(kontrola, kontrola2)

print(tuple.count(5))
print(tuple.count(10))

print(tuple.index(3))













