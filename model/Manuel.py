# model/Manuel.py
#
from model.Constantes import *
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
        raise ValueError("choisirCaseTirManuel : ")


    window.afficher(joueur)
    window.display_message(f"{joueur[const.JOUEUR_NOM]} : choisissez la case ou vous voulez tirer.")
    window.set_action(f"Choisissez la case de tir (bouton gauche)")
    res = window.get_clicked_cell(2)

    return res