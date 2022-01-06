# model/Jeu.py

#
#  Module mettant en place les joueurs
#
from random import randint

from model.Joueur import type_joueur, estPerdantJoueur, repondreTirJoueur
from model.Constantes import *
from model.Manuel import placerBateauxManuel, choisirCaseTirManuel, traiterResultatTirManuel
from view import window


# Pour jouer, un joueur doit être capable de :
# - placer ses bateaux
# - choisir une case pour tirer
# - traiter le résultat d'un tir
# Pour cela, on crée un acteur : dictionnaire
#       const.ACTEUR : Joueur (voir construireJoueur)
#       const.ACTEUR_PLACER_BATEAUX : fonction permettant de placer les bateaux
#       const.ACTEUR_CHOISIR_CASE : fonction permettant de choisir la case où le tir aura lieu
#       const.ACTEUR_TRAITER_RESULTAT : fonction permettant de traiter le résultat d'un précédent tir

def type_acteur(agent: dict) -> bool:
    """
    Détermine si le tuple passé en paramètre peut être un agent ou non
    :param agent: Agent à tester
    :return: True si c'est un agent, False sinon
    """
    return type(agent) == dict and \
        all(k in agent for k in [const.ACTEUR,
                                 const.ACTEUR_PLACER_BATEAUX,
                                 const.ACTEUR_CHOISIR_CASE,
                                 const.ACTEUR_TRAITER_RESULTAT]) and \
        type_joueur(agent[const.ACTEUR]) and \
        callable(agent[const.ACTEUR_PLACER_BATEAUX]) and callable(agent[const.ACTEUR_CHOISIR_CASE]) and \
        callable(agent[const.ACTEUR_TRAITER_RESULTAT])


def jouerJeu(joueur1: dict, joueur2: dict) -> None:

    placerBateauxManuel(joueur1[const.ACTEUR])
    placerBateauxManuel(joueur2[const.ACTEUR])

    JoueurRandom = randint(1,2)

    while (estPerdantJoueur(joueur1[const.ACTEUR]) == False) and (estPerdantJoueur(joueur2[const.ACTEUR]) == False):


        window.afficher()

        if JoueurRandom == 1:
            JoueurRandom = 2
            window.display_message(f"C’est au tour de {joueur1[const.ACTEUR][const.JOUEUR_NOM]}")
            coord = joueur1[const.ACTEUR_CHOISIR_CASE](joueur1[const.ACTEUR])
            rep = repondreTirJoueur(joueur2[const.ACTEUR],coord)
            joueur1[const.ACTEUR_TRAITER_RESULTAT](joueur1[const.ACTEUR],coord,rep)
            window.refresh()
            window.display_message(f"Tir en {coord} : {rep}")
        else:
            JoueurRandom = 1
            window.display_message(f"C’est au tour de {joueur2[const.ACTEUR][const.JOUEUR_NOM]}")
            coord = joueur2[const.ACTEUR_CHOISIR_CASE](joueur2[const.ACTEUR])
            rep = repondreTirJoueur(joueur1[const.ACTEUR], coord)
            joueur2[const.ACTEUR_TRAITER_RESULTAT](joueur2[const.ACTEUR], coord, rep)
            window.refresh()
            window.display_message(f"Tir en {coord} : {rep}")


    if estPerdantJoueur(joueur1[const.ACTEUR]):
        window.display_message(f"Le gagnant est {joueur2[const.ACTEUR][const.JOUEUR_NOM]}")
        print(f"le gagnant est : {joueur2[const.ACTEUR][const.JOUEUR_NOM]}")
    else:
        window.display_message(f"Le gagnant est {joueur1[const.ACTEUR][const.JOUEUR_NOM]}")
        print(f"le gagnant est : {joueur1[const.ACTEUR][const.JOUEUR_NOM]}")

    return None


def getListeBateaux() -> list:

    lstBateaux = [const.PORTE_AVION,const.CUIRASSE,const.CROISEUR,const.CROISEUR,const.TORPILLEUR]

    return lstBateaux