# Bateau.py

#
# - Définit un bateau sous forme de dictionnaire de la façon suivante :
#   const.BATEAU_NOM : Nom du bateau (voir les constantes dans Constantes.py - clés du dictionnaire const.BATEAUX_CASES)
#   const.BATEAU_SEGMENTS - Liste de listes [coordonnées, état] des segments du bateau.
#       Si le bateau n'est pas positionné, les coordonnées valent None et les états valent const.RATE
#   La taille du bateau n'est pas stockée car elle correspond à la taille de la liste des listes [coordonnées, état]
#

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



def construireBateau(name:str) -> dict:
    """
    regarde si le nom est valide et crées des segments
    """
    if name not in const.BATEAUX_CASES:
        raise ValueError("construireBateau : la valeur n'est pas un str valide")

    chiffre = const.BATEAUX_CASES[name]

    segment = []
    for j in range(0,chiffre):
        segment.append(construireSegment())


    dico = {const.BATEAU_NOM:name,const.BATEAU_SEGMENTS:segment}

    return dico

def getNomBateau(Bateau:dict) -> str:

    if not type_bateau(Bateau):
        raise ValueError("getNomBateau : ne peut pas trouver de nom car ce n'est pas un bateau")

    BateauNom = Bateau[const.BATEAU_NOM]

    return BateauNom

def getTailleBateau(Bateau:dict) -> int:

    if not type_bateau(Bateau):
        raise ValueError("getTailleBateau : ne peut pas trouver de nom car ce n'est pas un bateau")

    BateauTaille = len(Bateau[const.BATEAU_SEGMENTS])

    return BateauTaille

def getSegmentsBateau(Bateau:dict) -> list:

    if not type_bateau(Bateau):
        raise ValueError("getSegmentsBateau : ne peut pas trouver de nom car ce n'est pas un bateau")

    BateauSeg = Bateau[const.BATEAU_SEGMENTS]

    return BateauSeg

def getSegmentBateau(Bateau:dict , numSegCo:object) -> object:

    if not type_bateau(Bateau):
        raise ValueError("getSegmentBateau : ne peut pas trouver de nom car ce n'est pas un bateau")

    if type(numSegCo) == int:
        # Il s’agit du numéro du segment

        if (numSegCo > len(Bateau[const.BATEAU_SEGMENTS])-1) or (numSegCo < 0):
            raise ValueError("getSegmentBateau : erreur car le numero de segment est trop grand ou trop petit")

        segment = Bateau[const.BATEAU_SEGMENTS][numSegCo]

    elif type(numSegCo) == tuple:
        # Il s’agit de coordonnées
        segment = None
        v = 0 #v est une valeur
        for v in getSegmentsBateau(Bateau):
            if getCoordonneesSegment(v) == numSegCo:
                segment = v
        if segment is None:
            raise ValueError("le segment est Null")
    else:
        raise ValueError(f"Le type du second paramètre {type(numSegCo)} ne correspond pas…")

    return segment


def setSegmentBateau(Bateau:dict,SegmentNum:int,Segment:dict) -> None:

    if not type_bateau(Bateau):
        raise ValueError("setSegmentBateau : ne peut pas trouver de nom car ce n'est pas un bateau")
    if not type_segment(Segment):
        raise ValueError("setSegmentBateau : ne peut pas trouver de nom car ce n'est pas un segment")
    if (getTailleBateau(Bateau) <=  SegmentNum) or (SegmentNum < 0):
        raise ValueError("setSegmentBateau : erreur le segment est trop grand ou trop petit")


    Bateau[const.BATEAU_SEGMENTS][SegmentNum] = Segment
    return None

def getCoordonneesBateau(Bateau:dict) -> list:

    if not type_bateau(Bateau):
        raise ValueError("setSegmentBateau : ne peut pas trouver de nom car ce n'est pas un bateau")
    coordBateau = []
    for i in range(0,getTailleBateau(Bateau)):
        coordBateau.append(getCoordonneesSegment(getSegmentBateau(Bateau,i)))

    return coordBateau