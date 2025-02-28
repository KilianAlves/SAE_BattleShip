# Coordonnees.py

#
# - Définit les coordonnées d'une case
#
#  Une coordonnée est un tuple de deux entiers compris entre 0 (inclus) et const.DIM (exclus)
#  Elle peut aussi être None si elle est non définie
#

from model.Constantes import *


def type_coordonnees(c: tuple) -> bool:
    """
    Détermine si le tuple correspond à des coordonnées
    Les coordonnées sont sous la forme (ligne, colonne).
    Malheureusement, il n'est pas possible de tester si une inversion est faite entre ligne et colonne...

    :param c: coordonnées
    :return: True s'il s'agit bien de coordonnées, False sinon
    """
    return c is None or (type(c) == tuple and len(c) == 2 and 0 <= c[0] < const.DIM and 0 <= c[1] < const.DIM)


def sontVoisins(coordX:tuple,coordY:tuple) -> bool:
    """
    regarde si les deux coordonnée sont voisines
    """
    if not type_coordonnees(coordX):
        raise ValueError(f"sontVoisins : {coordX} n'est pas une coordonnée")
    if not type_coordonnees(coordY):
        raise ValueError(f"sontVoisins : {coordY} n'est pas une coordonnée")
    if coordX == None:
        raise ValueError(f"sontVoisins : {coordX} est null.")
    if coordY == None:
        raise ValueError(f"sontVoisins : {coordY} est null.")

    res = False
    if abs(coordX[0] - coordY[0]) <= 1 and abs(coordX[1] - coordY[1]) <= 1 and coordX != coordY:
        res = True
    return res

