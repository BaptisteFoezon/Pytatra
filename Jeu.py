import Dialogue
import Empilement
import Exemplaires
import Fenetre
import Joueur
import Pile
import Pioche
import Planchette
import VuePioche
import VuePile
import json

# Etape 5.1


def cree():
    return {"fenetre": Fenetre.cree(1000, 600),
            "pile": Pile.cree(),
            "0": Joueur.cree(0),
            "1": Joueur.cree(1),
            "courant": 0,
            "selection": ''}


def getSelection(jeu):
    return jeu["selection"]


def setSelection(jeu, selection):
    jeu["selection"] = selection


def fenetre(jeu):
    return jeu["fenetre"]


def pile(jeu):
    return jeu["pile"]


def joueurs(jeu):
    return (jeu["0"], jeu["1"])


def indiceJoueur(jeu):
    return jeu["courant"]


def joueurCourant(jeu):
    return jeu[str(indiceJoueur(jeu))]


def passeJoueurSuivant(jeu):
    jeu["courant"] = int(not jeu["courant"])


def piocheJoueur(jeu):
    return joueurCourant(jeu)[1]
# Etape 5.2


def getlongueur(selection):
    """ retourne la longeur de la planchette selectionner """
    return int(selection[0]) + int(selection[1])+int(selection[2])


def getMarge(selection):
    """ retourne la marge de la planchette selectionner """
    return int(selection[0])


def colorPlayer(jeu):
    """
    retourne la couleur du joueur actuel
    """
    if indiceJoueur(jeu) == 0:
        return "red"
    else:
        return "blue"


def joue(jeu):
    Fenetre.quandOuverte(fenetre(jeu), majVues, jeu)
    Fenetre.quandClick(fenetre(jeu), click, jeu)
    Fenetre.quandDeplacement(fenetre(jeu), deplacement, jeu)
    Fenetre.quandBoutonRelache(fenetre(jeu), relachement, jeu)
    Fenetre.affiche(fenetre(jeu))


def verification(jeu):
    if Pile.desequilibre(pile(jeu)) or not piocheJoueur(jeu):
        print("Fin du jeux")
        askRejouer(jeu)


def askRejouer(jeu):
    if Fenetre.rejouer(fenetre(jeu)) == "yes":
        Fenetre.quitte(fenetre(jeu))
        jeu = cree()
        joue(jeu)
    else:
        Fenetre.quitte(fenetre(jeu))


def majVues(jeu):
    Fenetre.effaceGraphiques(fenetre(jeu))
    VuePile.dessine(fenetre(jeu), pile(jeu))
    VuePioche.dessine(fenetre(jeu), Joueur.pioche(jeu["1"]), True, "blue")
    VuePioche.dessine(fenetre(jeu), Joueur.pioche(jeu["0"]), False, "red")


# Etape 5.3
def click(fenetre, event, jeu):
    x, y = event.x, event.y
    objet = fenetre[2].find_closest(x, y)
    tag = fenetre[2].gettags(objet)
    setSelection(jeu, objet)


def deplacement(fenetre, event, jeu):
    x, y = event.x, event.y
    objet = getSelection(jeu)
    x1, y1, x2, y2 = fenetre[2].coords(objet[0])
    xcenter = (x1 + x2)//2
    ycenter = (y1 + y2)//2
    fenetre[2].move(objet[0], x-xcenter, y-ycenter)


def relachement(fenetre, event, jeu):
    print("pose")
    color = colorPlayer(jeu)
    x, y = event.x, event.y
    objet = fenetre[2].find_closest(x, y)
    x1, y1, x2, y2 = fenetre[2].coords(objet[0])
    xcenter = (x1 + x2)//2
    tag = fenetre[2].gettags(objet)[0]
    selection = tagToPlanch(tag)
    largeurFenetre = 1000/10
    if Pile.sommet(pile(jeu)) is None:
        decalage = xcenter/10 - largeurFenetre/2
    else:
        abssommet = Pile.sommet(pile(jeu))['abscisse']
        print(abssommet)
        decalage = (xcenter/10-largeurFenetre/2) - abssommet
    Pile.empileEtCalcule(jeu["pile"], selection, decalage, color)
    Pioche.retire(piocheJoueur(jeu), tag)
    majVues(jeu)
    sauvegarde(jeu)
    verification(jeu)
    passeJoueurSuivant(jeu)


def tagToPlanch(tag):
    longueur = int(tag[0])+int(tag[1]) + int(tag[2])
    marge = int(tag[0])
    return Planchette.cree(longueur, marge)


def sauvegarde(jeu, fin=False):
    """on sauvegarde l'etat de la partie apres chaque tout de jeux"""
    if not fin:
        jeu_copie = {}
        for key in jeu:
            jeu_copie[key] = jeu[key]
        jeu_copie["fenetre"] = ""
        with open('data.json', 'w') as f:
            json.dump(jeu_copie, f)
    if fin:
        with open('data.json', 'w') as f:
            json.dump("", f)
