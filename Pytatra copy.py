from tkinter import *
import Jeuselectionsouris
import Fenetre
import json


def newGame():
    jeu = Jeuselectionsouris.cree()
    Jeuselectionsouris.joue(jeu)


def loadGame():
    with open("data.json", "r") as read_file:
        data = json.load(read_file)
        if data == "":
            texte = "pas de partie a chargé"
            jeu = Jeuselectionsouris.cree()
        else:
            jeu = data
            jeu["fenetre"] = Fenetre.cree(1000, 600)
    Jeuselectionsouris.joue(jeu)


welcomePage = Fenetre.cree(300, 100)
canvas = Fenetre.toile(welcomePage)
text = Label(canvas, text="PYTATRA")
text.pack()
boutons1 = Button(canvas, text="Nouvelle partie",
                  command=lambda: [Fenetre.tk(welcomePage).destroy(), newGame()])
boutons1.pack()
boutons2 = Button(canvas, text="Charger partie", command=lambda: [
                  Fenetre.tk(welcomePage).destroy(), loadGame()])
boutons2.pack()
Fenetre.affiche(welcomePage)
