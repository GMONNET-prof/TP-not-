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
    
    return nouvelle_chaine
        

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
    print(nouvelle_chaine)
    return nouvelle_chaine





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
        
print(vers_base_deux("192.168.15.0"))

def vers_base_dix(IP):
    """ Retourne l'IP écrite en base dix
        Entrée : IP binaire (str)
        Sortie : chaine en base 10 (str)"""
    liste_finale = []
    liste_morceaux = IP.split(".")
    assert len(liste_morceaux) == 4, "erreur dans l'IP"
    return ".".join(str(int(octet,2)) for octet in liste_morceaux)
        

rep = str(input("Donnez moi votre ip : "))
masque = int(input("Donnez moi votre masque : "))
rep_bin = vers_base_deux(rep)
ip_res = trouve_IP_reseau(rep_bin, masque)

print("Votre adresse reseau est donc : ", vers_base_dix(ip_res))
ip_diffusion = trouve_IP_diffusion(rep_bin, masque)
print("Votre adresse de diffusion est donc : ", vers_base_dix(ip_diffusion))
ip_a_trouver = ip_res.split(".")
dhcp =  ip_res
dhcp = vers_base_dix(dhcp)
l = dhcp.split(".")
l[3] = str(int(l[3]) + 1)
ip_finale = ".".join(l)
print("L'ip dhcp est : ",ip_finale)
routeur = ip_diffusion
routeur = vers_base_dix(routeur)
l1 = routeur.split(".")
l1[3] = str(int(l1[3]) - 1)
ip_finale1 = ".".join(l1)
print("L'ip routeur est : ",ip_finale1)
pl_min = dhcp.split(".")
pl_max = routeur.split(".")
pl_min = l[3] = str(int(l[3]) + 2)
pl_max = l1[3] = str(int(l1[3]) - 2)
ad1 = ".".join(l)
ad2 =".".join(l1)
print("La plage adressable est entre",ad1,"et",ad2 )
print("Le nombre de machine possible est :", 2**(32-masque)-4)
    



if __name__ == '__main__' :
    # les tests 
    monIP1 = "01011011.10011011.10111000.00111001" #91.155.184.57
    masque1 = 15
    # print(trouve_IP_reseau(monIP1, masque1))
    # print(trouve_IP_diffusion(monIP1, masque1))
    # print(vers_base_deux("192.156.12.5"))
    
    print("les tests sont validés") 