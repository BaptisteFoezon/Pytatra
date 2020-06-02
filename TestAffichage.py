import Fenetre
import Planchette
import VuePlanchette

p = Planchette.cree(12, 4)
ep = VuePlanchette.pixels(Planchette.Epaisseur)
r = range(ep, 10*ep, ep)

for test in range(1, 4):
    # test 1 : les 10 planchettes sont affichées
    f = Fenetre.cree(1000, 600)
    for xy in r:
        # test 2 : seule la dernière planchette est affichée
        if (test == 2):
            Fenetre.effaceGraphiques(f)
        VuePlanchette.dessine(f, p, xy, xy)
    # test 3 : aucune planchette n'est affichée
    if (test == 3):
        Fenetre.effaceGraphiques(f)
    Fenetre.affiche(f)
