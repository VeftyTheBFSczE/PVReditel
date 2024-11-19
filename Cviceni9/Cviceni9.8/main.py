def vydej_obedu():
    napoje = ["vitamínový nápoj"]

    menu1 = ["polévka česneková s bramborem", "segedínský guláš, houskové knedlíky", "jablko"]
    menu2 = ["polévka vývar s nudlemi", "pečená kachna, bramborová kaše", "pomeranč"]

    yield napoje
    print("Chcete menu 1?")
    odpoved = yield
    if odpoved == "ano":
        yield menu1
    elif odpoved == "ne":
        yield menu2
    else:
        yield "musite pouzit ano nebo ne"

corutina1 = vydej_obedu()
print(next(corutina1))
next(corutina1)
print(corutina1.send("ano"))
corutina1.close()