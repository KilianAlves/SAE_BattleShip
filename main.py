# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame

from model.Constantes import *
from model.Jeu import jouerJeu, getListeBateaux
from model.Joueur import construireJoueur, repondreTirJoueur
from model.Manuel import choisirCaseTirManuel, placerBateauxManuel, traiterResultatTirManuel, construireActeurManuel
from view import window

def main_test():
    j = construireJoueur("Test", [const.PORTE_AVION, const.CUIRASSE, const.CROISEUR, const.TORPILLEUR])
    # j = construireJoueur("Test", [const.PORTE_AVION, const.CUIRASSE])
    window.afficher(j)
    window.placer_bateaux()
    window.set_action("Pour terminer, cliquez dans la grille de DROITE")
    window.get_clicked_cell(2)

    placerBateauxManuel(j)
    coord = choisirCaseTirManuel(j)
    print(coord)
    rep = repondreTirJoueur(j,coord)
    traiterResultatTirManuel(j,coord,rep)

    window.refresh()
    window.set_action("Pour terminer, cliquez dans la grille de DROITE")
    window.get_clicked_cell(2)


def main() -> None:

    nomJoueur1 = "AAAAAAAAAA"
    nomJoueur2 = "BBBBBBBBB"

    joueur1 = construireJoueur(nomJoueur1,getListeBateaux())
    joueur2 = construireJoueur(nomJoueur2,getListeBateaux())

    acteur1 = construireActeurManuel(joueur1)
    acteur2 = construireActeurManuel(joueur2)

    jouerJeu(acteur1,acteur2)

    return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

