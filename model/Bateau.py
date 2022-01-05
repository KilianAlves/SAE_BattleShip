# Bateau.py

#
# - Définit un bateau sous forme de dictionnaire de la façon suivante :
#   const.BATEAU_NOM : Nom du bateau (voir les constantes dans Constantes.py - clés du dictionnaire const.BATEAUX_CASES)
#   const.BATEAU_SEGMENTS - Liste de listes [coordonnées, état] des segments du bateau.
#       Si le bateau n'est pas positionné, les coordonnées valent None et les états valent const.RATE
#   La taille du bateau n'est pas stockée car elle correspond à la taille de la liste des listes [coordonnées, état]
#
from model.Coordonnees import type_coordonnees, sontVoisins
from model.Segment import type_segment, getCoordonneesSegment
from model.Segment import construireSegment
from model.Constantes import *


def type_bateau(bateau: dict) -> bool:
    """
    Détermine si la liste représente un bateau

    :param bateau: Liste représentant un bateau
    :return: <code>True</code> si la liste contient bien un bateau, <code>False</code> sinon.
    """
    return type(bateau) == dict and \
           all([v in bateau for v in [const.BATEAU_NOM, const.BATEAU_SEGMENTS]]) and \
           type(bateau[const.BATEAU_NOM]) == str and \
           bateau[const.BATEAU_NOM] in const.BATEAUX_CASES and type(bateau[const.BATEAU_SEGMENTS]) == list and \
           len(bateau[const.BATEAU_SEGMENTS]) == const.BATEAUX_CASES[bateau[const.BATEAU_NOM]] and \
           all([type_segment(s) for s in bateau[const.BATEAU_SEGMENTS]])


def construireBateau(name: str) -> dict:
    """
    regarde si le nom est valide et crées des segments
    """
    if name not in const.BATEAUX_CASES:
        raise ValueError(f"construireBateau : la valeur {name} n'est pas un str valide")

    chiffre = const.BATEAUX_CASES[name]

    segment = []
    for j in range(0, chiffre):
        segment.append(construireSegment())

    dico = {const.BATEAU_NOM: name, const.BATEAU_SEGMENTS: segment}

    return dico


def getNomBateau(Bateau: dict) -> str:
    """
     recupere le nom du bateau
    """
    if not type_bateau(Bateau):
        raise ValueError(f"getNomBateau : ne peut pas trouver de nom car {Bateau} n'est pas un bateau")

    BateauNom = Bateau[const.BATEAU_NOM]

    return BateauNom


def getTailleBateau(Bateau: dict) -> int:
    """
    recupere la taille du bateau
    """
    if not type_bateau(Bateau):
        raise ValueError(f"getTailleBateau : ne peut pas trouver de nom car {Bateau} n'est pas un bateau")

    BateauTaille = len(Bateau[const.BATEAU_SEGMENTS])

    return BateauTaille


def getSegmentsBateau(Bateau: dict) -> list:
    """
    prend les segments du bateau
    """
    if not type_bateau(Bateau):
        raise ValueError(f"getSegmentsBateau : ne peut pas trouver de nom car {Bateau} n'est pas un bateau")

    BateauSeg = Bateau[const.BATEAU_SEGMENTS]

    return BateauSeg


def getSegmentBateau(Bateau: dict, numSegCo: object) -> object:
    """
    retourne le segment du bateau
    """
    if not type_bateau(Bateau):
        raise ValueError(f"getSegmentBateau : ne peut pas trouver de nom car {Bateau} n'est pas un bateau")

    if type(numSegCo) == int:
        # Il s’agit du numéro du segment

        if (numSegCo > len(Bateau[const.BATEAU_SEGMENTS]) - 1) or (numSegCo < 0):
            raise ValueError(f"getSegmentBateau : erreur car le numero de segment est trop grand ou trop petit ({numSegCo})")

        segment = Bateau[const.BATEAU_SEGMENTS][numSegCo]

    elif type(numSegCo) == tuple:
        # Il s’agit de coordonnées
        segment = None
        v = 0  # v est une valeur
        for v in getSegmentsBateau(Bateau):
            if getCoordonneesSegment(v) == numSegCo:
                segment = v
        if segment is None:
            raise ValueError("le segment est Null")
    else:
        raise ValueError(f"Le type du second paramètre {type(numSegCo)} ne correspond pas…")

    return segment


def setSegmentBateau(Bateau: dict, SegmentNum: int, Segment: dict) -> None:
    """
    remplace le segment du bateau par une autre segment
    """
    if not type_bateau(Bateau):
        raise ValueError(f"setSegmentBateau : ne peut pas trouver de nom car {Bateau} n'est pas un bateau")
    if not type_segment(Segment):
        raise ValueError(f"setSegmentBateau : ne peut pas trouver de nom car {Bateau} n'est pas un segment")
    if (getTailleBateau(Bateau) <= SegmentNum) or (SegmentNum < 0):
        raise ValueError(f"setSegmentBateau : erreur le segment est trop grand ou trop petit ({SegmentNum})")

    Bateau[const.BATEAU_SEGMENTS][SegmentNum] = Segment
    return None


def getCoordonneesBateau(Bateau: dict) -> list:
    """
     récupere les coordonnée du bateau
    """
    if not type_bateau(Bateau):
        raise ValueError(f"setSegmentBateau : erreur car {Bateau} n'est pas un bateau")
    coordBateau = []
    for i in range(0, getTailleBateau(Bateau)):
        coordBateau.append(getCoordonneesSegment(getSegmentBateau(Bateau, i)))

    return coordBateau


def peutPlacerBateau(bateau: dict, first_case: tuple, horizontal: bool) -> bool:
    """
    regarde si on peut placer le bateau a c'est coordonnée dans un sens donnée
    """
    if not type_bateau(bateau):
        raise ValueError(f"peutPlacerBateau : erreur car {bateau} n'est pas un bateau")
    if not type_coordonnees(first_case) and not None:
        raise ValueError(f"peutPlacerBateau : ne peut pas trouver de coordonnées car {first_case} n'est pas une coordonnée")
    if not type(horizontal) == bool:
        raise ValueError(f"peutPlacerBateau : erreur {horizontal} n'est pas un bool")

    res = False

    # coord : (y,x)
    if horizontal == True:
        if (first_case[1] + getTailleBateau(bateau) - 1) < const.DIM:
            res = True
    else:
        if (first_case[0] + getTailleBateau(bateau) - 1) < const.DIM:
            res = True

    return res


def estPlaceBateau(bateau: dict) -> bool:
    """
    regarde si le bateau a de la place??
    """
    res = True

    if not type_bateau(bateau):
        raise ValueError(f"estPlaceBateau : erreur car ce n'est pas un {bateau}")

    lst = getCoordonneesBateau(bateau)

    if None in lst:
        res = False

    return res


def sontVoisinsBateau(bateau1:dict,bateau2:dict) -> bool:
    """
    regarde si deux bateau sont voisins
    """
    if not type_bateau(bateau1):
        raise ValueError(f"sontVoisinsBateau : erreur car {bateau1} n'est pas un bateau")
    if not type_bateau(bateau2):
        raise ValueError(f"sontVoisinsBateau : erreur car {bateau2} n'est pas un bateau")
    if not estPlaceBateau(bateau1):
        raise ValueError(f"sontVoisinsBateau : {bateau1} n'est pas placé")
    if not estPlaceBateau(bateau2):
        raise ValueError(f"sontVoisinsBateau : {bateau2} n'est pas placé")

    res = False
    bateauCoord1 = getCoordonneesBateau(bateau1)
    bateauCoord2 = getCoordonneesBateau(bateau2)

    for i in range(0,getTailleBateau(bateau1)):
        for j in range(0,getTailleBateau(bateau2)):
            print("i",i," j",j)
            if sontVoisins(bateauCoord1[i],bateauCoord2[j]):
                res = True

    return res



