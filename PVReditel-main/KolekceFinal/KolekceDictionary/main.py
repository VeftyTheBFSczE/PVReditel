#Je zachovano poradi ve kterem jsou prvky kolekce vkladany?
thistuple = ("apple", "banana", "cherry", "apple")
thisdict = {
"model": "Mustang",
  "brand": "Ford",
   "brand": "Ford",
  "year": 1964,
 None: None
}
print(thisdict)
# Je možné kolekce vnořovat, tedy vložit jako prvek kolekce další kolekci s několika prvky
thisdictt = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"],
   "thisdict": thistuple
}
print(thisdictt)
# Je možné za běhu programu změnit  velikost kolekce
my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3
print(my_dict)
#  Jakým způsobem zjistím počet prvků v kolekci
print(len(thisdict))
# Jakymi všemi metodami je možné vložit nový prvek do kolekce a jaké mají tyto metody vstypy?
thisdict["years"] = 2002
print(thisdict)
# Jakymi všemi metodami je možné smazat/odebrat existující prvek do kolekce a jaké mají tyto metody vstypy
thisdict.pop("model")
print(thisdict)
thisdict.update({"year": 2020})
print(thisdict)
# Jakymi všemi metodami je možné ověřit jestli kolekce bsahuje nějaký prvek
my_dict = {'a': 1, 'b': 2, 'c': 3}
if 'b' in my_dict:
    print("je tam")
#
    my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
    third_item = list(my_dict.items())[2]
    print(third_item)





