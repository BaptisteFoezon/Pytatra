import Fenetre

from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *

# Boite dialogues : https://runestone.academy/runestone/books/published/thinkcspy/GUIandEventDrivenProgramming/02_standard_dialog_boxes.html

def afficheMessage(message):
	showinfo(Fenetre.Titre, message)

def saisisEntier(message):
	return saisisNombre(message, True)

def saisisFlottant(message):
	return saisisNombre(message, False)

def saisisNombre(message, entier):
	saisie = None
	while (saisie == None):
		if (entier):
			saisie = askinteger(Fenetre.Titre, message)
		else:
			saisie = askfloat(Fenetre.Titre, message)
		if (saisie == None):
			reponse = askyesno(Fenetre.Titre, "Voulez-vous terminer le jeu ?")
			if (reponse):
				return None
	return saisie
