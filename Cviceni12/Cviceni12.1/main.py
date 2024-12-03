import time
import multiprocessing

def vypis_cisel():
    for i in range(0,10):
        print(i)
        time.sleep(1)


if __name__ == "__main__":
        print("ZACATEK PROGRAMU")
        p1 = multiprocessing.Process(target=vypis_cisel)
        p1.start()
        p1.join()
        print("KONEC PROGRAMU")


"""
Program vypisuje najednou ty procesy, protože nečeká na to jestli se dokončí druhý. Tím pádem aby jsme tadyto opravili
tak musíme napsat p1.join() tímto příkazem bude proces čekat než se ten první příkaz dokončí

Procesy tedy běží dva jeden hlavní a druhý p1 
"""