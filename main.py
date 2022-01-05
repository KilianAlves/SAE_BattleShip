# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame

from model.Constantes import *
from model.Joueur import construireJoueur
from model.Manuel import choisirCaseTirManuel, placerBateauxManuel
from view import window

def main_test():
    j = construireJoueur("Test", [const.PORTE_AVION, const.CUIRASSE, const.CROISEUR, const.TORPILLEUR])
    # j = construireJoueur("Test", [const.PORTE_AVION, const.CUIRASSE])
    window.afficher(j)
    window.placer_bateaux()
    window.set_action("Pour terminer, cliquez dans la grille de DROITE")
    window.get_clicked_cell(2)

    placerBateauxManuel(j)
    print(choisirCaseTirManuel(j))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

