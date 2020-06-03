import Exemplaires
import Planchette


def cree():
    return {"181": 1,
            "262": 2,
            "343": 3,
            "282": 2,
            "363": 3,
            "444": 4,
            "383": 3,
            "464": 4,
            "545": 5, }


def nombrePlanchettes(pioche):
    somme = 0
    for i in pioche.keys():
        somme += int(pioche[i])
    return somme


def versChaine(pioche):
    ch = ""
    for i in pioche.keys():
        ch += "{}x{} ".format(pioche[i], i)
    return ch


def recherche(pioche, numero):
    i = 0
    if str(numero) in pioche:
        for key in pioche.keys():
            if key == str(numero):
                return i
            else:
                i += 1
    else:
        return -1


def contient(pioche, numero):
    return str(numero) in pioche


def retire(pioche, numero):
    print(numero)
    if contient(pioche, numero) and pioche[str(numero)] > 0:
        pioche[str(numero)] -= 1
    if contient(pioche, numero) and pioche[str(numero)] == 0:
        del pioche[str(numero)]
