##---les fonctions---##
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
   
    octets = nouvelle_chaine.split(".")
    ip_reseau_decimal = ".".join(str(int(octet, 2)) for octet in octets)
    
    return ip_reseau_decimal
    
    
    
def trouver_ip_binaire(IP):
    
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
        
    
    
 
        

def trouve_IP_diffusion(IP,masque):
    """ retourne l'IP de diffusion à partir d'une IP d'une machine et du masque
        Entrée : IP est une chaine de caractères (0 ou 1) et masque est un nombre entier (int)
        Sortie : IP du réseau : chaine de caractères (0 ou 1)"""
    nouvelle_chaine = ""
    ip_masque = ("0" * masque) + ("1" * (32 - masque))
    ip_masque = ip_masque[0:8] + "." + ip_masque[8:16] + "." + ip_masque[16:24] + "." + ip_masque[24:]
    for i in range(len(IP)):
        if IP[i] == "0" and ip_masque[i] == "0":
            nouvelle_chaine += "0"
        elif IP[i] == ".":
            nouvelle_chaine += "."
        else:
            nouvelle_chaine += "1"
    
    
        
    octets = nouvelle_chaine.split(".")
    ip_diffusion_decimal = ".".join(str(int(octet, 2)) for octet in octets)
    
    return ip_diffusion_decimal


def IP_routeur(IP, masque):
    ip_diffusion=trouve_IP_diffusion(IP, masque)
    octets=ip_diffusion.split(".")
   
    trois_octet=int(octets[3])
    trois_octet-=1
    
    octets.pop(3)
    octets.append(trois_octet)
    ip_routeur=".".join(str(int(octet))for octet in octets)
    return  ip_routeur

def IP_DHCP(IP, masque):
    ip_reseau=trouve_IP_reseau(IP, masque)
    octets=ip_reseau.split(".")
   
    trois_octet=int(octets[3])
    trois_octet+=1
    
    octets.pop(3)
    octets.append(trois_octet)
    ip_DHCP=".".join(str(int(octet))for octet in octets)
    return ip_DHCP


def nb_de_machine_sur_reseau(masque):
    return (2**(32-masque))-4

def plage_adressable(IP, masque):
    ip_routeur=IP_routeur(IP, masque)
    octets=ip_routeur.split(".")
   
    trois_octet=int(octets[3])
    trois_octet-=1
    
    octets.pop(3)
    octets.append(trois_octet)
    ip_derniere =".".join(str(int(octet))for octet in octets)
    
    ip_dhcp=IP_DHCP(IP, masque)
    octets=ip_dhcp.split(".")
   
    trois_octet=int(octets[3])
    trois_octet+=1
    
    octets.pop(3)
    octets.append(trois_octet)
    ip_premiere=".".join(str(int(octet))for octet in octets)
    
    return f"La plage adressable va de l'ip {ip_premiere} à l'ip {ip_derniere}"







if __name__ == '__main__' :
    # les tests 
    x= str(input("Quel est l'ip? "))
    monIP1 = trouver_ip_binaire(x) #91.155.184.57
    masque1 = int(input("Quel est le masque du reseau? "))
    print(f"L'ip du reseau est: {trouve_IP_reseau(monIP1, masque1)}")
    print(f"L'ip de diffusion est: {trouve_IP_diffusion(monIP1, masque1)}")
    print(f"L'ip du routeur est: {IP_routeur(monIP1, masque1)}")
    print(f"L'ip du serveur dhcp est: {IP_DHCP(monIP1, masque1)}")
    print(f"Le reseau peux acceuillir {nb_de_machine_sur_reseau(masque1)} machines")
    print(plage_adressable(monIP1, masque1))
    print("les tests sont validés") 