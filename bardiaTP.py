# BARDIA


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
        


def vers_base_dix(IP):
    """ Retourne l'IP écrite en base dix
        Entrée : IP binaire (str)
        Sortie : chaine en base 10 (str)"""
    liste_morceaux = IP.split(".")
    assert len(liste_morceaux) == 4, "erreur dans l'IP"
    return ".".join(str(int(octet,2)) for octet in liste_morceaux)



def trouve_IP_reseau(IP,masque):
    """ retourne l'IP réseau à partir d'une IP d'une machine et du masque
        Entrée : IP est une chaine de caractères (0 ou 1) et masque est un nombre entier (int)
        Sortie : IP du réseau : chaine de caractères (0 ou 1)"""
    nouvelle_chaine = ""
    ip_masque = ("1" * masque) + ("0" * (32 - masque))
    ip_masque = ip_masque[0:8] + "." + ip_masque[8:16] + "." + ip_masque[16:24] + "." + ip_masque[24:]
    for i in range(len(IP)):
        if IP[i] == "1" and ip_masque[i] == "1":
            nouvelle_chaine += "1"
        elif IP[i] == ".":
            nouvelle_chaine += "."
        else:
            nouvelle_chaine += "0"
    
    return nouvelle_chaine
      

def trouve_IP_diffusion(IP,masque):
    """ retourne l'IP de diffusion à partir d'une IP d'une machine et du masque
        Entrée : IP est une chaine de caractères (0 ou 1) et masque est un nombre entier (int)
        Sortie : IP du réseau : chaine de caractères (0 ou 1)"""
    nouvelle_chaine = ""
    ip_masque = ("0" * masque) + ("1" * (32 - masque))
    ip_masque = ip_masque[0:8] + "." + ip_masque[8:16] + "." + ip_masque[16:24] + "." + ip_masque[24:32]
    for i in range(len(IP)):
        if IP[i] == "0" and ip_masque[i] == "0":
            nouvelle_chaine += "0"
        elif IP[i] == ".":
            nouvelle_chaine += "."
        else:
            nouvelle_chaine += "1"
    
    return nouvelle_chaine

def trouve_IP_dhcp(IP_reseau_binaire):
    liste_morceaux = IP_reseau_binaire.split(".")
    octets =[int(octet, 2) for octet in liste_morceaux]
    octets[-1] += 1
    
    if octets[-1] > 255:
        octets[-1] = 0
        octets[-2] += 1
    ip_routeur_binaire = ".".join(format(octet, '08b') for octet in octets)
    
    return ip_routeur_binaire

def trouve_IP_routeur(IP_reseau, IP_diffus):
    octets_diffus = IP_diffus.split(".")
    octets_int =[int(octet) for octet in octets_diffus]
    octets_int[-1] -= 1
    
    if octets_int[-1] < 0:
        octets_int[-1] = 255
        octets_int[-2] -= 1
    ip_routeur = ".".join(str(octet) for octet in octets_int)
    
    return ip_routeur



def nombre_places(masque):
    return ((2 ** (32 - masque)) - 4)

def plage(ip_diffus, ip_rout):
    ip_diffus = vers_base_dix(ip_diffus)
    ip_rout = vers_base_dix(ip_rout)
    lachainediff = ip_diffus.split(".")
    lachainerout = ip_rout.split(".")
    for i in range(3, -1, -1):  
        if int(lachainerout[i]) < 255:
            lachainerout[i] = str(int(lachainerout[i])+ 1)
        else:
            lachainerout[i] = "0"

    for i in range(3, -1, -1):
        if int(lachainediff[i]) > 0:
            lachainediff[i] = str(int(lachainediff[i]) - 1)
        else:
            lachainediff[i] = "255"
    premierdisp = ".".join(lachainerout)
    dernierdisp = ".".join(lachainediff)

    return(premierdisp, "à", dernierdisp)
    


user_ip = input("⮑ Entrez votre IP : ")
user_masque = int(input("⮑ Entrez votre masque : "))

user_ip_binaire = vers_base_deux(user_ip)
user_ip_reseau = trouve_IP_reseau(user_ip_binaire, user_masque)

user_ip_diff = trouve_IP_diffusion(user_ip_binaire, user_masque)
user_ip_routeur = trouve_IP_routeur(user_ip_reseau, user_ip_diff)
user_ip_dhcp = trouve_IP_dhcp(user_ip_reseau)

print("-----------")
print("* Votre IP de réseau : ", vers_base_dix(user_ip_reseau))
print("* Votre IP de diffusion : ", vers_base_dix(user_ip_diff))
print("* L'IP du routeur : ", vers_base_dix(user_ip_routeur))
print("* L'IP du serveur DHCP : ", vers_base_dix(user_ip_dhcp))
print("* Nombre de places :", nombre_places(user_masque))
print("* Plage : ", plage(user_ip_diff, user_ip_routeur))
