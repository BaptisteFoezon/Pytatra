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

selection = ""


def cree():
    return {"fenetre": Fenetre.cree(1000, 600),
            "pile": Pile.cree(),
            "0": Joueur.cree(0),
            "1": Joueur.cree(1),
            "courant": 0}


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

# Etape 5.2


def joue(jeu):
    majVues(jeu)
    Fenetre.quandOuverte(fenetre(jeu), activite, jeu)
    Fenetre.affiche(fenetre(jeu))


def majVues(jeu):
    Fenetre.effaceGraphiques(fenetre(jeu))
    VuePile.dessine(fenetre(jeu), pile(jeu))
    VuePioche.dessine(fenetre(jeu), Joueur.pioche(jeu["0"]), True)
    VuePioche.dessine(fenetre(jeu), Joueur.pioche(jeu["1"]), False)


# Etape 5.1


def cree():
    return {"fenetre": Fenetre.cree(1000, 600),
            "pile": Pile.cree(),
            "0": Joueur.cree(0),
            "1": Joueur.cree(1),
            "courant": 0}


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


def piocheJoueurCourant(jeu):
    return Joueur.pioche(jeu[str(indiceJoueur(jeu))])
# Etape 5.2


def joue(jeu):
    Fenetre.quandOuverte(fenetre(jeu), majVues, jeu)
    Fenetre.quandDeplacement(fenetre(jeu), deplacement, jeu)
    Fenetre.quandBoutonRelache(fenetre(jeu), relachement, jeu)
    Fenetre.affiche(fenetre(jeu))


def majVues(jeu):
    Fenetre.effaceGraphiques(fenetre(jeu))
    VuePile.dessine(fenetre(jeu), pile(jeu))
    VuePioche.dessine(fenetre(jeu), Joueur.pioche(jeu["0"]), True)
    VuePioche.dessine(fenetre(jeu), Joueur.pioche(jeu["1"]), False)

# Etape 5.3


def deplacement(fenetre, event):
    print("deplacement ...")
    x, y = event.x, event.y
    objet = fenetre[2].find_closest(x, y)
    print(objet[0])
    x1, y1, x2, y2 = fenetre[2].coords(objet[0])
    xcenter = (x1 + x2)//2
    ycenter = (y1 + y2)//2
    fenetre[2].move(objet[0], x-xcenter, y-ycenter)


def relachement(fenetre, event, jeu):
    print("pose")
    x, y = event.x, event.y
    objet = fenetre[2].find_closest(x, y)
    tag = fenetre[2].gettags(objet)[0]
    longueur = int(tag[0])+int(tag[1]) + int(tag[2])
    marge = int(tag[0])
    pioche = piocheJoueurCourant(jeu)
    selection = Planchette.cree(longueur, marge)
    Pioche.retire(pioche, selection)
    decalage = 2
    Pile.empileEtCalcule(jeu["pile"], selection, decalage)
    Pioche.retire(pioche, tag)
    passeJoueurSuivant(jeu)
    print("joueur suivant")
    majVues(jeu)
    sauvegarde(jeu)


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
