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

# Etape 5.3


def activite(jeu):
    global selection
    desequilibre = False
    while True:
        joueur = indiceJoueur(jeu)
        print(Pile.sommet(pile(jeu)))
        pioche = jeu[str(joueur)][1]
        if pioche and not desequilibre:
            print("c'est au joueur n° {} de jouer ".format(joueur))
            selection = selectionnePlanchette(jeu)
            if Pioche.contient(pioche, selection) is False:
                while Pioche.contient(pioche, selection) is False:
                    selection = selectionnePlanchette(jeu)
            longueur = int(selection[0]) + \
                int(selection[1])+int(selection[2])
            marge = int(selection[0])
            selection = Planchette.cree(longueur, marge)
            Pioche.retire(pioche, selection)
            decalage = choisisDecalage(jeu, selection)
            Pile.empileEtCalcule(jeu["pile"], selection, decalage)
            desequilibre = Pile.sommet(pile(jeu))["desequilibre"]
            passeJoueurSuivant(jeu)
            selection = ""
            sauvegarde(jeu)
        else:
            print("le joueur n° {} a perdu ".format(joueur))
            break
        majVues(jeu)
    print("fin du jeux le joueur n°{} a gagné".format(indiceJoueur(jeu)))
    sauvegarde(jeu, True)


def selectionnePlanchette(jeu):
    selection = Fenetre.saisisTexte(
        fenetre(jeu), "saississez votre planchette")
    while selection is None:
        selection = Fenetre.saisisTexte(
            fenetre(jeu), "saississez votre planchette")
    if selection is not None:
        return selection


def choisisDecalage(jeu, planchetteAPoser):
    decalage = Fenetre.saisisEntier(fenetre(jeu), "decalage")
    while decalage is None:
        decalage = Fenetre.saisisEntier(fenetre(jeu), "decalage")
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
