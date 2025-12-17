# -*- coding: utf-8 -*-

def vers_base_deux(IP):
    """ Retourne l'IP écrite en base deux
        Entrée : IP (str)
        Sortie : chaine binaire (str)"""
    liste_finale = []
    liste_morceaux = IP.split(".")
    assert len(liste_morceaux) == 4, "erreur dans l'IP"
    for nombre in liste_morceaux :
        quotient = int(nombre)
        chaine=""
        while quotient != 0:
            reste = quotient%2
            quotient = quotient//2
            chaine =str(reste)+chaine
        chaine = "0"*(8-len(chaine))+chaine
        liste_finale.append(chaine)
    return ".".join(liste_finale)
        
          
            


