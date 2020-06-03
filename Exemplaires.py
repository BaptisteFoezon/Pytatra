# coding: utf-8
import Planchette


def cree(planchette, nombre):
    return [planchette, nombre]


def planchette(exemplaires):
    return Planchette.numero(exemplaires[0])


def nombre(exemplaires, valeur=None):
    if valeur is not None:
        exemplaires[1] = valeur
    return exemplaires[1]


def retireUn(exemplaires):
    exemplaires[1] = int(exemplaires[1])-1
    return nombre(exemplaires)


def versChaine(exemplaires):
    print("{}x{}".format(nombre(exemplaires), planchette(exemplaires)))
