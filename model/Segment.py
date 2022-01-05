# model/Segment.py

from model.Coordonnees import type_coordonnees
from model.Etat import type_etat_segment
from model.Constantes import *

#
# définit un segment de bateau :
# Un segment de bateau est un dictionnaire contenant les couples (clé, valeur) suivants :
#   - const.SEGMENT_COORDONNEES : Les coordonnées du segment sur la grille
#   - ccnst.SEGMENT_ETAT : L'état du segment (const.RATE ou const.TOUCHE)
#


def type_segment(objet: dict) -> bool:
    """
    Détermine si l'objet passé en paramètre peut être interprété ou non
    comme un segment de bateau.

    :param objet: Objet à analyser
    :return: True si l'objet peut correspondre à un segment
    False sinon.
    """
    return type(objet) == dict and \
           all([k in objet for k in [const.SEGMENT_COORDONNEES, const.SEGMENT_ETAT]]) \
           and type_coordonnees(objet[const.SEGMENT_COORDONNEES]) \
           and type_etat_segment(objet[const.SEGMENT_ETAT])



def construireSegment(coord: tuple = None) -> dict:
    """
    Construire un segment
    """
    if type_coordonnees(coord) == True:
        dico = {const.SEGMENT_COORDONNEES:coord,const.SEGMENT_ETAT:const.INTACT}
    else:
        raise ValueError(f"construireSegment : le paramètre {coord} ne correspond pas à des coordonnées")
    return dico


def getCoordonneesSegment(segment:dict) -> tuple:
    """
    recupere les coordonnée du segment
    """
    if not type_segment(segment):
        raise ValueError(f"getCoordonneesSegment : le paramètre {segment} n’est pas de type Segment.")


    coord = segment[const.SEGMENT_COORDONNEES]

    return coord


def getEtatSegment(segment:dict) -> str:
    """
    recupere l'etat du segment
    """
    if not type_segment(segment):
        raise ValueError(f"getEtatSegment : le paramètre {segment} n’est pas de type Segment.")


    return segment[const.SEGMENT_ETAT]


def setCoordonneesSegment(segment:dict,coord:tuple) -> None:
    """
    remplace les coordonnée du segment par coord
    """
    if type_segment(segment):
        if type_coordonnees(coord):
            segment[const.SEGMENT_COORDONNEES] = coord
        else:
            raise ValueError(f"setCoordonneesSegment : le paramètre {coord} ne correspond pas à des coordonnées")
    else:
        raise ValueError(f"setCoordonneesSegment : le paramètre {segment} n’est pas de type Segment.")

    return None


def setEtatSegment(segment:dict,etat:str) -> None:
    """
    remplace l'etat du segment
    """
    if type_segment(segment):
        if type_etat_segment(etat):
            segment[const.SEGMENT_ETAT] = etat
        else:
            raise ValueError(f"setEtatSegment : le paramètre {etat} ne correspond pas à un etat")
    else:
        raise ValueError(f"setEtatSegment : le paramètre {segment} n’est pas de type Segment.")

    return None