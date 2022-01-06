from model.Constantes import *
from random import randint

def ChoisirCaseIa(lst:list) -> :

    if not len(lst) > 0
        lst = CoordonneesIaInit()
    randint(0,len(lst))

    return


def CoordonneesIaInit() -> list:

    lst = []
    print("1")
    for k in range(0, const.DIM):
        print("2")
        lst.append([])

    for i in range(0, const.DIM):
        print("3")
        for j in range(0, const.DIM):
            print("4")
            lst[i].append(([i],[j]))

    return lst

print("test")
print(CoordonneesIaInit())