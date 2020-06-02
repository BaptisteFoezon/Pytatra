from tkinter import *

# Etape 2

Titre = 'Pytatra'

def cree(largeur, hauteur):
	tk = Tk()
	tk.title(Titre)
	toile = Canvas(tk, width=largeur, height=hauteur, background="white")
	toile.pack()
	return (toile, largeur, hauteur, tk)

def toile(fenetre):
	return fenetre[0]

def largeur(fenetre):
	return fenetre[1]

def hauteur(fenetre):
	return fenetre[2]

def tk(fenetre):
	return fenetre[3]

def affiche(fenetre):
	tk(fenetre).mainloop()

# Etape 5

TagGraphiques = 'graphique'

def effaceGraphiques(fenetre):
	toile(fenetre).addtag_all(TagGraphiques)
	toile(fenetre).delete(TagGraphiques)

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

