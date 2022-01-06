# model/Manuel.py
#
from model.Case import type_case
from model.Constantes import *
from model.Coordonnees import type_coordonnees
from model.Grille import marquerCouleGrille
from model.Joueur import type_joueur
from view import window

def placerBateauxManuel(joueur:dict) -> None:

    if not type_joueur(joueur):
        raise ValueError(f"placerBateauxManuel : erreur {joueur} n'est pas un joueur")
    window.afficher(joueur)
    window.display_message(f"{joueur[const.JOUEUR_NOM]} : Placez vos bateaux")
    window.placer_bateaux()
    return None


def choisirCaseTirManuel(joueur:dict) -> tuple:

    if not type_joueur(joueur):
        raise ValueError(f"choisirCaseTirManuel : erreur {joueur} n'est pas un joueur")


    window.afficher(joueur)
    window.display_message(f"{joueur[const.JOUEUR_NOM]} : choisissez la case ou vous voulez tirer.")
    window.set_action(f"Choisissez la case de tir (bouton gauche)")
    res = window.get_clicked_cell(2)

    return res[0]


def traiterResultatTirManuel(joueur:dict,coord:tuple,rep:str) -> None:

    if not type_joueur(joueur):
        raise ValueError(f"traiterResultatTirManuel : erreur {joueur} n'est pas un joueur")
    if not type_coordonnees(coord):
        raise ValueError(f"traiterResultatTirManuel : erreur {coord} n'est pas une coordonnée")
    if None in coord:
        raise ValueError(f"traiterResultatTirManuel : erreur {coord} est Null")
    if not type_case(rep):
        raise ValueError(f"traiterResultatTirManuel : erreur {rep} n'est pas un str")

    joueur[const.JOUEUR_GRILLE_TIRS][coord[0]][coord[1]] = rep
    if rep == const.COULE:
        marquerCouleGrille(joueur[const.JOUEUR_GRILLE_TIRS],coord)
    print(rep)

    return None