# -*- coding: utf-8 -*-

def entier_vers_binaire(chaine):
    """Transforme la chaine d'entier de base 10 en chaine de base 2
       Entrée : une chaine d'int en base 10 (str)
       Sortie : la chaine d'int en base 2 (str)"""
    chaine_int = chaine.split(".")
    chaine_binaire = ""
    for elt in chaine_int :
        assert int(elt) <= 255 and int(elt) >= 0
        nbre_binaire = ""
        for i in range(7, -1,-1):
            res = int(elt) - 2**i
            if res >= 0 :
                nbre_binaire += "1"
                elt = int(elt) - 2**i
            else :
                nbre_binaire += "0"
        chaine_binaire = chaine_binaire + nbre_binaire + "."
    return chaine_binaire[:-1]



def binaire_vers_entier(chaine):
    """Transforme la chaine d'entier de base 2 en chaine de base 10
       Entrée : une chaine d'int en base 2 (str)
       Sortie : la chaine d'int en base 10 (str)"""
    chaine_binaire = chaine.split(".")
    chaine_int = ""
    for elt in chaine_binaire :
        assert len(elt) == 8, "Erreur : la chaine doit être de longeur 8"
        res = 0
        puis = 0
        for i in range(7,-1,-1) :
            res += int(elt[i]) * 2**puis
            puis +=1
        chaine_int = chaine_int + str(res) + "."
    return chaine_int[:-1]
            
            

def IP_reseau(IP,masque):
    """Retourne l'IP réseau à partir d'une IP d'une machine et d'un masque
       Entrée : IP de longueur 32 (str de 0 et de 1) et masque (int entre 0 et 32)
       Sortie : IP réseau(str en binaire)"""
    IP_reseau = ""
    IP_masque = ""
    for j in range(int(masque)): # méthode utilisée en classe qui ne fonctionnait pas (erreur multiplication str et int)
        IP_masque += "1"
    for a in range(32-int(masque)):
        IP_masque += "0"
    IP_masque = IP_masque[0:8] + "." + IP_masque[8:16] + "." + IP_masque[16:24] + "." + IP_masque[24:]
    for i in range(len(IP)):
        if IP[i] == "1" and IP_masque[i] == "1":
            IP_reseau += "1"
        elif IP[i] == ".":
            IP_reseau += "."
        else :
            IP_reseau += "0"
    return IP_reseau



def IP_diffusion(IP,masque):
    """Retourne l'IP diffusion à partir d'une IP d'une machine et d'un masque
       Entrée : IP de longueur 32 (str de 0 et de 1) et masque (int entre 0 et 32)
       Sortie : IP réseau(str en binaire)"""
    IP_diffusion = ""
    IP_masque = ""
    for j in range(int(masque)):
        IP_masque += "0"
    for a in range(32-int(masque)):
        IP_masque += "1"
    IP_masque = IP_masque[0:8] + "." + IP_masque[8:16] + "." + IP_masque[16:24] + "." + IP_masque[24:]
    for i in range(len(IP)):
        if IP[i] == "0" and IP_masque[i] == "0":
            IP_diffusion += "0"
        elif IP[i] == ".":
            IP_diffusion += "."
        else :
            IP_diffusion += "1"
    return IP_diffusion


def IP_routeur(ad_diffusion):
    """Retourne l'adresse IP du routeur
       Entrée : l'adresse IP (str)
       Sortie : l'IP du routeur (str)"""
    ip_routeur = ""
    ip_diffusion = ad_diffusion.split(".") #trouve a dernière adresse
    ip_diffusion[-1] = "254"
    ip_routeur = ".".join(ip_diffusion)
    return ip_routeur


def IP_DHCP(ad_reseau):
    """Retourne l'adresse IP du DHCP
       Entrée : l'adresse IP (str)
       Sortie : l'IP du DHCP (str)"""
    ip_dhcp = ""
    ip_reseau = ad_reseau.split(".") #trouve la première adresse
    ip_reseau[-1] = "1"
    ip_dhcp = ".".join(ip_reseau)
    return ip_dhcp

def plage_adressable(ad_reseau, ad_diffusion):
    """Retourne la plage adressable du réseau en fonction de l'IP en entrée
       Entrée : L'IP du réseau (str)
       Sortie : la plage adressable = 1e et dernière adresse IP (str)"""
    premiere_adresse = ""
    ip_reseau = ad_reseau.split(".") #trouve la première adresse
    ip_reseau[-1] = "2"
    premiere_adresse = ".".join(ip_reseau)
    
    derniere_adresse = ""
    ip_diffusion = ad_diffusion.split(".") #trouve a dernière adresse
    ip_diffusion[-1] = "253"
    derniere_adresse = ".".join(ip_diffusion)
    return(f"première adresse : {premiere_adresse} , dernière adresse : {derniere_adresse}")
    
       
       

def trouve_nbre_machines(masque):
    """Retourne le nombre de machines maximum pouvant être sur le réseau en fonction de la plage adressable
       Entrée : la plage adressable
       Sortie : le nombre de machines (int)"""
    nb_machines =  2**(32-int(masque)) - 2
    return nb_machines
       


def test():
    chaine = input("Entrez une IP : ")
    masque = input("Entrez un masque : ")
    IP_binaire = entier_vers_binaire(chaine)
    ad_reseau = binaire_vers_entier(IP_reseau(IP_binaire, masque))
    print("IP réseau : ", ad_reseau)
    ad_dif = binaire_vers_entier(IP_diffusion(IP_binaire, masque))
    print("IP diffusion : ", ad_dif)
    print("IP DHCP : ", IP_DHCP(ad_reseau))
    print("IP routeur : ", IP_routeur(ad_dif))
    print("plage adressable => ", plage_adressable(ad_reseau, ad_dif))
    print(f"nb_machines : {trouve_nbre_machines(masque)} machines (sans le routeur et le DHCP)")
    

test()

