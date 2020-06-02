import Planchette
import Empilement


def cree():
    return []


def estVide(pile):
    return pile == []


def sommet(pile):
    if estVide(pile):
        return None
    else:
        return pile[len(pile)-1]


def empile(pile, planchette, decalage):
    if not estVide(pile):
        centre = Empilement.centreGeometrique(sommet(pile)) + decalage
    else:
        centre = 0
        masse = Planchette.longueur(planchette)
    empilement = Empilement.cree(planchette, centre)
    pile.append(empilement)


def versChaine(pile):
    print('-'*20)
    for empilement in pile:
        num = Planchette.numero(empilement["planchette"])
        mass = empilement["masse"]
        centre = empilement["abscisse"]
        grav = empilement["centre_grav"]
        dese = ""
        if empilement["desequilibre"]:
            dese = "!"
        print("n° {} m= {} c={} g={} {}".format(num, mass, centre, grav, dese))
    print('^'*20)


def empileEtCalcule(pile, planchette, decalage):
    empile(pile, planchette, decalage)
    calculeCentresGravite(pile)
    calculeEquilibre(pile)


def calculeCentresGravite(pile):
    taille = len(pile)
    for i in range(taille-1, 0, -1):
        dessus = pile[i]
        dessous = pile[i-1]
        # calcul des masses
        longueurDessous = Planchette.longueur(Empilement.planchette(dessous))
        masseDessus = Empilement.masse(dessus)
        masseDessous = longueurDessous + masseDessus
        Empilement.masse(dessous, masseDessous)
        # calcul des centres de gravité
        centreGeometriqueDessous = Empilement.centreGeometrique(dessous)
        centreGraviteDessus = Empilement.centreGravite(dessus)
        centreGraviteDessous = (longueurDessous * centreGeometriqueDessous)
        centreGraviteDessous += (masseDessus * centreGraviteDessus)
        centreGraviteDessous /= masseDessous
        Empilement.centreGravite(dessous, centreGraviteDessous)


def calculeEquilibre(pile):
    taille = len(pile)
    for i in range(taille-1, 0, -1):
        dessus = pile[i]
        dessous = pile[i-1]
        longueurDessous = Planchette.longueur(Empilement.planchette(dessous))
        centreGraviteDessus = Empilement.centreGravite(dessus)
        centreGeometriqueDessous = Empilement.centreGeometrique(dessous)
        if abs(centreGraviteDessus - centreGeometriqueDessous) > longueurDessous/2:
            Empilement.desequilibre(dessus, True)
