# coding: utf-8
from tkinter import *
import Jeu
import Fenetre
import json
import webbrowser


def callback(event):
    webbrowser.open_new(r"https://github.com/BaptisteFoezon/Pytatra")


def newGame():
    jeu = Jeu.cree()
    Jeu.joue(jeu)


def loadGame():
    with open("data.json", "r") as read_file:
        data = json.load(read_file)
        if data == "":
            texte = "pas de partie a chargé"
            jeu = Jeu.cree()
        else:
            jeu = data
            jeu["fenetre"] = Fenetre.cree(1000, 600)
    Jeu.joue(jeu)


def welcome():
    print("#"*10 + "\n Pytatra \n" + "#"*10)

    welcomePage = Fenetre.cree(350, 150)
    canvas = Fenetre.toile(welcomePage)
    text = Label(canvas, text="PYTATRA")
    text.pack()
    boutons1 = Button(canvas, text="Nouvelle partie",
                      command=lambda: [Fenetre.tk(welcomePage).destroy(), newGame()])
    boutons1.pack()
    boutons2 = Button(canvas, text="Charger partie", command=lambda: [
        Fenetre.tk(welcomePage).destroy(), loadGame()])
    boutons2.pack()
    text = Label(canvas, text="Lien vers le project GitHub")
    text.pack()
    link = Label(
        canvas, text="https://github.com/BaptisteFoezon/Pytatra", fg="blue")
    link.pack()
    link.bind("<Button-1>", callback)
    Fenetre.affiche(welcomePage)


if __name__ == "__main__":
    welcome()