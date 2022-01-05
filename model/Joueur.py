# Joueur.py

from model.Bateau import type_bateau, construireBateau
from model.Grille import type_grille, construireGrille
from model.Constantes import *


#
# Un joueur est représenté par un dictionnaire contenant les couples (clé, valeur) suivants :
#  const.JOUEUR_NOM : Nom du joueur de type str
#  const.JOUEUR_LISTE_BATEAUX : Liste des bateaux du joueur
#  const.JOUEUR_GRILLE_TIRS : Grille des tirs sur les bateaux adverses
#  const.JOUEUR_GRILLE_ADVERSAIRE : une grille des tirs de l'adversaire pour tester la fonction de tir
#  de l'adversaire.
#


def type_joueur(joueur: dict) -> bool:
    """
    Retourne <code>True</code> si la liste semble correspondre à un joueur,
    <code>false</code> sinon.

    :param joueur: Dictionnaire représentant un joueur
    :return: <code>True</code> si le dictionnaire représente un joueur, <code>False</code> sinon.
    """
    return type(joueur) == dict and len(joueur) >= 4 and \
           len([p for p in [const.JOUEUR_NOM, const.JOUEUR_LISTE_BATEAUX, const.JOUEUR_GRILLE_TIRS] if
                p not in joueur]) == 0 and \
           type(joueur[const.JOUEUR_NOM]) == str and type(joueur[const.JOUEUR_LISTE_BATEAUX]) == list \
           and type_grille(joueur[const.JOUEUR_GRILLE_TIRS]) \
           and all(type_bateau(v) for v in joueur[const.JOUEUR_LISTE_BATEAUX])


def construireJoueur(PlayerName: str, Bateau: dict) -> dict:
    """
    construire le joueur
    """
    Bateau = list(Bateau)
    bateauxList = []

    for i in range(0,len(Bateau)):
        bateauxList.append(construireBateau(Bateau[i]))

    joueur = {const.JOUEUR_NOM : PlayerName, const.JOUEUR_LISTE_BATEAUX : bateauxList, const.JOUEUR_GRILLE_TIRS : construireGrille(), const.JOUEUR_GRILLE_ADVERSAIRE : construireGrille()}


    if not type_joueur(joueur):
        raise ValueError(f"construireJoueur : Erreur {joueur} n'est pas un joueur")

    return joueur


def getNomJoueur(joueur:dict) -> str:
    """
    recupere le nom du joueur
    """
    if not type_joueur(joueur):
        raise ValueError(f"getNomJoueur : Erreur {joueur} n'est pas un joueur")

    NomJoueur = joueur[const.JOUEUR_NOM]

    return NomJoueur

def getNombreBateauxJoueur(joueur:dict) -> int:
    """"
    recupere le nombre de bateaux du joueurs
    """
    if not type_joueur(joueur):
        raise ValueError(f"getNombreBateauxJoueur : Erreur {joueur} n'est pas un joueur")

    NbrBateauJoueur = len(joueur[const.JOUEUR_LISTE_BATEAUX])

    return NbrBateauJoueur


def getBateauxJoueur(joueur:dict) -> list:
    """
    recupere les bateaux du joueur
    """
    if not type_joueur(joueur):
        raise ValueError(f"getBateauxJoueur : Erreur {joueur} n'est pas un joueur")

    bateauxJoueur = joueur[const.JOUEUR_LISTE_BATEAUX]

    return bateauxJoueur


def getGrilleTirsJoueur(joueur:dict) -> list:
    """
    recupere la grille de tir du joueur
    """
    if not type_joueur(joueur):
        raise ValueError(f"getGrilleTirsJoueur : Erreur {joueur} n'est pas un joueur")

    GrilleTirsJoueur = joueur[const.JOUEUR_GRILLE_TIRS]

    return GrilleTirsJoueur

def getGrilleTirsAdversaire (joueur:dict) -> list:
    """
    recupere la grille de tirs de l'adversaire
    """
    if not type_joueur(joueur):
        raise ValueError(f"getGrilleTirsAdversaire  : Erreur {joueur} n'est pas un joueur")

    GrilleTirsJoueur = joueur[const.JOUEUR_GRILLE_ADVERSAIRE]

    return GrilleTirsJoueur