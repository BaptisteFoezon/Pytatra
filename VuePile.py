# coding: utf-8
from tkinter import *
import Planchette
import Empilement
import Fenetre
import VuePlanchette


def dessine(fenetre, pile):
    y0 = Planchette.Epaisseur
    for empilement in pile:
        x0 = Empilement.centreGeometrique(
            empilement) - Empilement.planchette(empilement)[0]/2
        planchette = Empilement.planchette(empilement)
        x = VuePlanchette.pixels(x0) + Fenetre.largeur(fenetre)/2
        y = Fenetre.hauteur(fenetre) - VuePlanchette.pixels(y0) - 40
        VuePlanchette.dessine(fenetre,  planchette, x, y,
                              Empilement.color(empilement))
        x1 = VuePlanchette.pixels(Empilement.centreGravite(
            empilement)) + Fenetre.largeur(fenetre)/2
        y1 = y + VuePlanchette.pixels(Planchette.Epaisseur / 2)
<<<<<<< HEAD
        dessinecroix(fenetre, empilement, y1, x1)
        y0 += Planchette.Epaisseur
=======
        # dessinecroix(fenetre, empilement, x1, y1, y0)
        y0 += Planchette.Epaisseur

>>>>>>> eecc816abb9aafa5f75be6fd9538c9105139ee57

def dessinecroix(fenetre, empilement, x1, y1, y0):
    color = colorDesequilibre(empilement)
    Fenetre.toile(fenetre).create_line(
        x1-5, y1-5, x1+5, y1+5, width=3, fill=color)
    Fenetre.toile(fenetre).create_line(
        x1+5, y1-5, x1-5, y1+5, width=3, fill=color)

<<<<<<< HEAD
def dessinecroix(fenetre, empilement, y1, x1):
=======

def colorDesequilibre(empilement):
>>>>>>> eecc816abb9aafa5f75be6fd9538c9105139ee57
    if Empilement.desequilibre(empilement):
        color = "red"
    else:
        color = "green"
<<<<<<< HEAD
    Fenetre.toile(fenetre).create_line(
        x1-5, y1-5, x1+5, y1+5, width=3, fill=color)
    Fenetre.toile(fenetre).create_line(
        x1+5, y1-5, x1-5, y1+5, width=3, fill=color)
=======
    return color
>>>>>>> eecc816abb9aafa5f75be6fd9538c9105139ee57
