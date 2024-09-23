#je zachovan list a neradi
thislist = [1,6,3,7]
print(thislist, "zachova")
#Vyuziva indexy
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)
#dva stejne prvky
prvky = [1,1]
print(prvky, "ano daj se")
#tady se da dat null
myList = [None]
print(myList)
#tady se da dat list do kolekce
myListt = [myList, "vsechno jde"]
print(myListt)
#je mozne zvetsit za behu
myListt.append("jdepouzit")
print(myListt)
#Jakým způsobem zjistím počet prvků v kolekci?
print(len(thislist))
#Jakymi všemi metodami je možné vložit nový prvek?
myListt.append("ano")
print(myListt)
#Jakymi všemi metodami je možné smazat/odebrat existující prvek do kolekce a jaké mají tyto metody  vstupy
myListt.pop(2)
print(myListt)
#Jakymi všemi metodami je možné upravit hodnotu existujícího prvek v kolekci a jaké mají tyto metody vstupy?
myListt[2] = 30
print(myListt)

#Jakymi všemi metodami je možné ověřit jestli kolekce obsahuje nějaký prvek
listik = [1,2,3,4,5,6,5,5]
kontrola = 6 in listik
kontrola2 = 7 in listik
print(kontrola, kontrola2)
print(listik.count(5))
print(listik.count(10))
print(listik.index(3))

