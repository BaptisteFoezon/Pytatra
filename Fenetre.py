from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *

# Etape 2

Titre = 'Pytatra!'


def cree(largeur, hauteur):
    root = Tk()
    root.title(Titre)
    root.geometry(str(largeur)+"x"+str(hauteur))
    fenetre = (largeur, hauteur)
    toile = Canvas(root,
                   width=largeur,
                   height=hauteur)
    return root, fenetre, toile


def toile(fenetre):
    return fenetre[2]


def largeur(fenetre):
    return fenetre[1][0]


def hauteur(fenetre):
    return fenetre[1][1]


def tk(fenetre):
    return fenetre[0]


def affiche(fenetre):
    toile(fenetre).pack()
    tk(fenetre).mainloop()


# Etape 5


TagGraphiques = 'graphique'


def effaceGraphiques(fenetre):
    toile(fenetre).delete("all")


def afficheMessage(fenetre, message):
    toile(fenetre).showinfo(" ", message)


def saisisTexte(fenetre, message):
    return askstring("", message, parent=tk(fenetre))


def saisisEntier(fenetre, message):
    return askinteger("", message)


def quandOuverte(fenetre, fonction, argument):
    def fonctionInterne(e):
        # pour éviter les invocations ultérieures
        tk(fenetre).unbind('<Map>')
        # invocation de la fonction principale
        fonction(argument)
    # liaison de l'évènement d'ouverture
    tk(fenetre).bind('<Map>', fonctionInterne)


def quitte(fenetre):
    tk(fenetre).quit()


def saisisFlottant(fenetre, message):
    return askfloat("", message)


def quandBoutonAppuye(fenetre, fonction, jeu):
    toile(fenetre).bind("<Button-1>",
                        (lambda event: fonction(fenetre, event)))


def quandDeplacement(fenetre, fonction, jeu):
    toile(fenetre).bind("<B1-Motion>",
                        (lambda event: fonction(fenetre, event)))


def quandBoutonRelache(fenetre, fonction, jeu):
    toile(fenetre).bind("<ButtonRelease-1>",
                        (lambda event: fonction(fenetre, event, jeu)))


"""def clicDeplacement(fenetre, fonction, tag):
    toile(fenetre).bind("<B1-Motion>", (lambda event: fonction(fenetre, event)))"""
