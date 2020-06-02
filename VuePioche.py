from tkinter import *

import Exemplaires
import Planchette
import Pioche
import Fenetre
import VuePlanchette


def dessine(fenetre, pioche, gauche):
    marge = 70
    y = Fenetre.hauteur(fenetre) - 40 - Planchette.Epaisseur
    for planchette in reversed(pioche):
        txt = "{}x{} ".format(pioche[planchette], planchette)
        planchette = list(map(int, planchette))
        planchette = Planchette.cree(sum(planchette), planchette[0])
        if gauche:
            VuePlanchette.dessine(fenetre, planchette,
                                  marge, y)
            Fenetre.toile(fenetre).create_text(
                marge/2, y, text=txt)
        else:
            lg = VuePlanchette.pixels(Planchette.longueur(planchette))
            x = Fenetre.largeur(fenetre) - marge - lg
            VuePlanchette.dessine(fenetre, planchette, x,
                                  y)
            Fenetre.toile(fenetre).create_text(
                (Fenetre.largeur(fenetre))-marge/2, y, text=txt)
        y -= 20
