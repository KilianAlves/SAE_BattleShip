# model/Manuel.py
#
from model.Joueur import type_joueur
from view import window

def placerBateauxManuel(joueur:dict) -> None:

    if not type_joueur(joueur):
        raise ValueError(f"placerBateauxManuel : erreur {joueur} n'est pas un joueur")
    window.afficher(joueur)
    window.display_message(f"{joueur[const.JOUEUR_NOM]} : Placez vos bateaux")
    window.placer_bateaux()
    return None