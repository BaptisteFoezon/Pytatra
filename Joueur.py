import Pioche


def cree(numero):
    return (numero, Pioche.cree())


def numero(joueur):
    return joueur[0]


def nom(joueur):
    return "joueur n°{}".format(numero(joueur))


def pioche(joueur):
    return joueur[1]
