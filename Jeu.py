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


def piocheJoueur(jeu):
    return joueurCourant(jeu)[1]

# Etape 5.2


def joue(jeu):
    majVues(jeu)
    Fenetre.quandOuverte(fenetre(jeu), activite, jeu)
    Fenetre.affiche(fenetre(jeu))


def majVues(jeu):
    """ Met a jour les element du canvas """
    Fenetre.effaceGraphiques(fenetre(jeu))
    VuePile.dessine(fenetre(jeu), pile(jeu))
    VuePioche.dessine(fenetre(jeu), Joueur.pioche(jeu["0"]), True, "blue")
    VuePioche.dessine(fenetre(jeu), Joueur.pioche(jeu["1"]), False, "red")

# Etape 5.3


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
        return "blue"
    else:
        return "red"


def activite(jeu):
    continuer = True
    desequilibre = False
    while continuer:
        color = colorPlayer(jeu)
        joueur = indiceJoueur(jeu)
        pioche = piocheJoueur(jeu)
        # si la pioche n'est pas vide et que l'empilement n'est pas en desequilibre
        if pioche and not desequilibre:
            selection = selectionnePlanchette(jeu)
            longueur = getlongueur(selection)
            marge = getMarge(selection)
            Pioche.retire(piocheJoueur(jeu), selection)
            selection = Planchette.cree(longueur, marge)
            decalage = choisisDecalage(jeu, selection)
            Pile.empileEtCalcule(jeu["pile"], selection, decalage, color)
            desequilibre = Pile.sommet(pile(jeu))["desequilibre"]
            passeJoueurSuivant(jeu)
            selection = ""
            sauvegarde(jeu)
        else:
            print("le joueur n° {} a gagné ".format(joueur))
            continuer = False
            askRejouer(jeu)
        majVues(jeu)
    sauvegarde(jeu, True)


def askRejouer(jeu):
    if Fenetre.rejouer(fenetre(jeu)) == "yes":
        Fenetre.quitte(fenetre(jeu))
        jeu = cree()
        joue(jeu)
    else:
        Fenetre.quitte(fenetre(jeu))


def selectionnePlanchette(jeu):
    txt = "Joueur n° " + str(indiceJoueur(jeu)) + \
        " saississez votre planchette"
    selection = Fenetre.saisisTexte(
        fenetre(jeu), txt)
    while selection is None or Pioche.contient(piocheJoueur(jeu), selection)is False:
        selection = Fenetre.saisisTexte(
            fenetre(jeu), txt)
    if selection is not None:
        return selection


def choisisDecalage(jeu, planchetteAPoser):
    txt = "Joueur n° " + str(indiceJoueur(jeu)) + \
        " choisit ton decalage"
    decalage = Fenetre.saisisEntier(fenetre(jeu), txt)
    while decalage is None:
        decalage = Fenetre.saisisEntier(fenetre(jeu), txt)
    if decalage is not None:
        return decalage


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
