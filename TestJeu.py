import Jeu
import Joueur

j = Jeu.cree()

print('fenetre=' + str(Jeu.fenetre(j)))
print('pile=' + str(Jeu.pile(j)))
print('joueurs=' + str(Jeu.joueurs(j)))
print('indiceJoueur=' + str(Jeu.indiceJoueur(j)))

print('joueurCourant=' + Joueur.nom(Jeu.joueurCourant(j)))

for i in range(2):
	Jeu.passeJoueurSuivant(j)
	print('indiceJoueur=' + str(Jeu.indiceJoueur(j)))
	print('joueurCourant=' + Joueur.nom(Jeu.joueurCourant(j)))
