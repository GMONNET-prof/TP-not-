# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def convertion(IP):
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

def IP_routeur(IP_en_binaire,masque):
    ...
    

def nb_machine_reseau(masque):
   nb_machine = 2**32-masque
   return(nb_machine)
    
    

if __name__ == '__main__' :
    # les tests 
    monIP1 = "01011011.10011011.10111000.00111001" #91.155.184.57
    masque1 = 15
    IP10 = "193.156.12.5"
    print(convertion(IP10))
    # print(trouve_IP_reseau(monIP1, masque1))
    # print(trouve_IP_diffusion(monIP1, masque1))
    
    # print("les tests sont validés") 