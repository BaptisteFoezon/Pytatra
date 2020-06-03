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


def saisisTexte(fenetre, message, titre=""):
    return askstring(titre, message)


def saisisEntier(fenetre, message, titre=""):
    return askinteger(titre, message)


def rejouer(fenetre):
    return askquestion("Pytatra", "voulez rejouer")


def quandOuverte(fenetre, fonction, argument):
    def fonctionInterne(e):
        # pour éviter les invocations ultérieures
        tk(fenetre).unbind('<Map>')
        # invocation de la fonction principale
        fonction(argument)
    # liaison de l'évènement d'ouverture
    tk(fenetre).bind('<Map>', fonctionInterne)


def quitte(fenetre):
    tk(fenetre).destroy()


def saisisFlottant(fenetre, message):
    return askfloat("", message)


"""def menu(fenetre):
    menuBar = Menu(tk(fenetre))
    tk(fenetre).config(menu=menuBar)
    menufichier = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Fichier", menu=menufichier)"""
