# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def convertion(IP):
    """convertie l'ip en binaire
       Entre: IP en base 10
       Sortie: IP en binaire
    """
    nb = IP.split(".")
    IP_en_binaire = ""
    for elem in nb:
        morceau = str(bin(int(elem))) + "."
        morceau = morceau[2:]
        morceau = "0"* (9-len(morceau)) + morceau
        IP_en_binaire += morceau
    IP_en_binaire = IP_en_binaire[:-1]
    return IP_en_binaire



def reconvertion(chaine):
     nb = chaine.split(".")
     IP_en_10 = ""
     for elem in nb:
        #elem est un 8 bits
        res = 0
        puissance = 7
        for bit in elem :
            res += int(bit)*2**puissance
            puissance-=1
        IP_en_10 += str(res)+"."
     IP_en_10 = IP_en_10[:-1]
     return IP_en_10   
    
    
    
    
def trouve_IP_reseau(IP_en_binaire,masque):
    """ retourne l'IP réseau à partir d'une IP d'une machine et du masque
        Entrée : IP est une chaine de caractères (0 ou 1) et masque est un nombre entier (int)
        Sortie : IP du réseau : chaine de caractères (0 ou 1)"""
    nouvelle_chaine = ""
    ip_masque = ("1" * masque) + ("0" * (32 - masque))
    ip_masque = ip_masque[0:8] + "." + ip_masque[8:16] + "." + ip_masque[16:24] + "." + ip_masque[24:]
    for i in range(len(IP_en_binaire)):
        if IP_en_binaire[i] == "1" and ip_masque[i] == "1":
            nouvelle_chaine += "1"
        elif IP_en_binaire[i] == ".":
            nouvelle_chaine += "."
        else:
            nouvelle_chaine += "0"
    
    return nouvelle_chaine
        

def trouve_IP_diffusion(IP_en_binaire,masque):
    """ retourne l'IP de diffusion à partir d'une IP d'une machine et du masque
        Entrée : IP est une chaine de caractères (0 ou 1) et masque est un nombre entier (int)
        Sortie : IP du réseau : chaine de caractères (0 ou 1)"""
    nouvelle_chaine = ""
    ip_masque = ("0" * masque) + ("1" * (32 - masque))
    ip_masque = ip_masque[0:8] + "." + ip_masque[8:16] + "." + ip_masque[16:24] + "." + ip_masque[24:]
    for i in range(len(IP_en_binaire)):
        if IP_en_binaire[i] == "0" and ip_masque[i] == "0":
            nouvelle_chaine += "0"
        elif IP_en_binaire[i] == ".":
            nouvelle_chaine += "."
        else:
            nouvelle_chaine += "1"
    
    return nouvelle_chaine




def IP_routeur(IP_diffusion):
    """ Retourne l'IP du routeur a partir de l'ip de diffusion
        Entrée : IP binaire (str)
        Sortie : chaine en base 10 (str)"""
    liste_finale = []
    liste_morceaux = IP_diffusion.split(".")
    assert len(liste_morceaux) == 4, "erreur dans l'IP"
    for nombre in liste_morceaux :
        puiss = len(nombre) - 1 
        res = 0
        for carac in nombre :
            res = res + int(carac) * 2 ** puiss
            puiss -= 1
        liste_finale.append(str(res))
    dernier_nombre = int(liste_finale[-1])
    dernier_nombre -= 1
    liste_finale[-1] = str(dernier_nombre)
    return ".".join(liste_finale)
    

def IP_dhcp(IP_reseau):
    """ Retourne l'IP du DHCP a partir de l'ip du reseau
        Entrée : IP binaire (str)
        Sortie : chaine en base 10 (str)"""
    liste_finale = []
    liste_morceaux = IP_reseau.split(".")
    assert len(liste_morceaux) == 4, "erreur dans l'IP"
    for nombre in liste_morceaux :
        puiss = len(nombre) - 1 
        res = 0
        for carac in nombre :
            res = res + int(carac) * 2 ** puiss
            puiss -= 1
        liste_finale.append(str(res))
    dernier_nombre = int(liste_finale[-1])
    dernier_nombre += 1
    liste_finale[-1] = str(dernier_nombre)
    return ".".join(liste_finale)


def nb_machine_reseau(masque):
    """retourne le nombre de machine disponible sur le resau
       Entree: masque est un nombre entier (int)
       Sortie:
    """
    nb_machine = 2**32-masque
    return(nb_machine)

    
def plage_adressable(IP_en_binaire,masque):
    """ retourne la plage d'adresses utilisables du réseau
        Entrée : IP en binaire (chaine) et masque (int)
        Sortie : IP_debut, IP_fin en binaire
    """
    debut = IP_dhcp(trouve_IP_reseau(monIP1, masque1))
    fin = IP_routeur(trouve_IP_diffusion(monIP1, masque1))
    return debut, fin  

if __name__ == '__main__' :
    # les tests 
    #monIP1 = "91.155.184.57" #91.155.184.57
    monIP1 = str(input("Entrez votre ip svp: "))
    compteur_de_points = 0
    for elmt in monIP1:
        if elmt == ".":
            compteur_de_points += 1
    if compteur_de_points != 3:
        print ("votre ip n'est pas valide")
    else:
        masque1 = int(input("Entrez votre masque: "))
        if masque1 < 0 or masque1 > 32:
            print("le masque n'est pas valide")
        else:
            monIP1 = "01011011.10011011.10111000.00111001" #91.155.184.57
            IP10 = "193.156.12.5"
            print(convertion(IP10))
            IP_res = trouve_IP_reseau(monIP1, masque1)
            print("l'IP du reseau est :",IP_res)
            IP_diff = trouve_IP_diffusion(monIP1, masque1)
            #print(IP_diff)
            print("l'IP du routeur est :",IP_routeur(IP_diff))
            print("l'IP du DHCP est :",IP_dhcp(IP_res))
            print(plage_adressable(monIP1,masque1))
            
            print("les tests sont validés") 