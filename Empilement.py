import Planchette


def cree(planchette, centre):
    return {
        "planchette": planchette,
        "masse": Planchette.longueur(planchette),
        "abscisse": centre,
        "centre_grav": centre,
        "desequilibre": False,
    }


def planchette(empilement):
    return empilement["planchette"]


def centreGeometrique(empilement):
    return empilement["abscisse"]


def masse(empilement, valeur=None):
    if valeur is not None:
        empilement["masse"] = valeur
    return empilement["masse"]


def centreGravite(empilement, valeur=None):
    if valeur is not None:
        empilement["centre_grav"] = valeur
    return empilement["centre_grav"]


def desequilibre(empilement, valeur=None):
    if valeur is not None:
        empilement["desequilibre"] = valeur
    return empilement["desequilibre"]


def versChaine(empilement):
    num = empilement["planchette"]
    mass = masse(empilement)
    centre = centreGeometrique(empilement)
    grav = centreGravite(empilement)
    if desequilibre(empilement) == True:
        dese = "!"
    else:
        dese = ""
    return "n° {} m= {} c={} g={} {}".format(num, mass, centre, grav, dese)
