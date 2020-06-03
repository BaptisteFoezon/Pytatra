# coding: utf-8
from tkinter import *

import Fenetre
import Planchette

Facteur = 10  # 1 cm = 10 pixels


def pixels(cm):
    return cm*10


def dessine(fenetre, planchette, x0, y0, color="blue"):
    """

    """

    eppaisseur = pixels(Planchette.Epaisseur)
    marge = pixels(Planchette.marge(planchette))
    longueur = pixels(Planchette.longueur(planchette))-2*marge

    Fenetre.toile(fenetre).create_rectangle(
        x0, y0, x0+marge, y0+eppaisseur, fill="grey")
    Fenetre.toile(fenetre).create_rectangle(x0+marge, y0, x0 +
                                            marge+longueur, y0+eppaisseur, fill=color, tag=Planchette.numero(planchette))
    Fenetre.toile(fenetre).create_rectangle(x0+marge+longueur, y0,
                                            x0+marge+longueur+marge, y0+eppaisseur, fill="grey")
