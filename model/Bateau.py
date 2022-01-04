# Bateau.py

#
# - Définit un bateau sous forme de dictionnaire de la façon suivante :
#   const.BATEAU_NOM : Nom du bateau (voir les constantes dans Constantes.py - clés du dictionnaire const.BATEAUX_CASES)
#   const.BATEAU_SEGMENTS - Liste de listes [coordonnées, état] des segments du bateau.
#       Si le bateau n'est pas positionné, les coordonnées valent None et les états valent const.RATE
#   La taille du bateau n'est pas stockée car elle correspond à la taille de la liste des listes [coordonnées, état]
#

from model.Segment import type_segment
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
        raise ValueError("getNomBateau : ne peut pas trouver de nom car ce n'est pas un batteau")
    else:
        BateauNom = Bateau[const.BATEAU_NOM]

    return BateauNom

