#Je zachovano poradi ve kterem jsou prvky kolekce vkladany?
thisset = {"karel", "Honza", "Ema"}
print(thisset)
#u cisel se to nemeni
#Jsou hodnoty ulozene v serazenem poradi od nejmensiho po nejvetsi?
thissett = {2,1,4,3,10,7}
print(thissett)
#Používá se pro přístup k hodnotám index?
"""print(thissett.index(thisset))"""
#Je mozne ulozit dva stejné prvky?
thissettt = {2,1,4,3,10,7,7, None}
print(thissettt)
#mozne vlozit hodnotu None?
#viz kod o dva radky vys
#Je možné kolekce vnořovat, tedy vložit jako prvek kolekce další kolekci s několika prvky?
"""thissetttt = {thissettt}
print(thissetttt) """
#Je možné za běhu programu změnit velikost kolekce?
thisset.add("karlos")
print(thisset)

#Jakým způsobem zjistím počet prvků v kolekci?
print(len(thisset))
#Jakymi všemi metodami je možné smazat/odebrat
thisset.remove("karlos")
print(thisset)
#Jakymi všemi metodami je možné upravit hodnotu existujícího prvek v kolekci a jaké mají tyto metody vstypy?
my_set = {1, 2, 3}
my_set1 = {"Michal"}
my_set.update([3, 4, 5])
my_set1.update(["Marek"])
print(my_set)
print(my_set1)
#
listik = {1,2,3,4,5,6,5,5}
kontrola = 6 in listik
kontrola2 = 7 in listik
print(kontrola, kontrola2)
#print(listik.count(5))
#print(listik.count(10))
#print(listik.index(3))

