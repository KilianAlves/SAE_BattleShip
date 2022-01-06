# Grille.py
from model.Bateau import setEtatSegmentBateau
from model.Constantes import *
from model.Case import type_case

#
# - Définition de la grille des tirs
#       - tableau 2D (const.DIM x const.DIM) contenant des cases de type type_case.
#
# Bien qu'on pourrait créer une autre grille contenant les bateaux, ceux-ci seront stockés dans une liste
# et chaque bateau contiendra sa liste de coordonnées.
#
from model.Coordonnees import type_coordonnees
from model.Segment import construireSegment


def type_grille(g: list) -> bool:
    """
    Détermine si le paramètre est une grille de cases dont le type est passé en paramètre ou non
    :param g: paramètre à tester
    :return: True s'il peut s'agir d'une grille du type voulu, False sinon.
    """
    res = True
    if type(g) != list or len(g) != const.DIM:
        res = False
    else:
        i = 0
        while res and i < len(g):
            res = type(g[i]) == list and len(g[i]) == const.DIM
            j = 0
            while res and j < len(g[i]):
                res = type_case(g[i][j])
                j += 1
            i += 1
    return res


def construireGrille() -> list:
    """
    construire la grille
    """
    grille = []
    for k in range(0,const.DIM):
        grille.append([])

    for i in range(0,const.DIM):
        for j in range(0,const.DIM):
            grille[i].append(None)

    return grille


def marquerCouleGrille(grille: list, coord: tuple) -> None:

    if not type_grille(grille):
        raise ValueError(f"marquerCouleGrille : erreur {grille} n'est pas une grille")
    if not type_coordonnees(coord):
        raise ValueError(f"marquerCouleGrille : erreur {coord} n'est pas une coordonnée")
    if None in coord:
        raise ValueError(f"marquerCouleGrille : erreur {coord}")

    lst = [coord]

    while len(lst) > 0:
        tempCord = lst[0]
        del lst[0]
        grille[tempCord[0]][tempCord[1]] = const.COULE
        lstVoisins = [(tempCord[0]-1,tempCord[1]),(tempCord[0]+1,tempCord[1]),(tempCord[0],tempCord[1]-1),(tempCord[0],tempCord[1]+1)]

        for i in lstVoisins:
            if i[0] >= 0 and i[0] < const.DIM and i[1] >= 0 and i[1] < const.DIM :
                if grille[i[0]][i[1]] == const.TOUCHE:
                    lst.append(i)

    return None