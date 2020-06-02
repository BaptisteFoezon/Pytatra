# Etape 2

Epaisseur = 1


def cree(longueur, marge):
    planchette = (longueur, marge)  # use tuple cst
    return planchette


def longueur(planchette):
    return planchette[0]


def marge(planchette):
    return planchette[1]


def numero(planchette):
    return str(planchette[1])+str(int(planchette[0])-2*int(planchette[1]))+str(planchette[1])
