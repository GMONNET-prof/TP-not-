# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 08:34:30 2025

@author: gregory.monnet
"""

def vers_base_dix(IP):
    """ Retourne l'IP écrite en base dix
        Entrée : IP binaire (str)
        Sortie : chaine en base 10 (str)"""
    liste_finale = []
    liste_morceaux = IP.split(".")
    assert len(liste_morceaux) == 4, "erreur dans l'IP"
    for nombre in liste_morceaux :
        puiss = len(nombre) - 1 
        res = 0
        for carac in nombre :
            res = res + int(carac) * 2 ** puiss
            puiss -= 1
        liste_finale.append(str(res))
    return ".".join(liste_finale)