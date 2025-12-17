##---les fonctions---##


def codage_binaire(IP):
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
    
    return vers_base_dix(nouvelle_chaine)
        

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
    
    return vers_base_dix(nouvelle_chaine)



def trouve_IP_routeur(IP,masque):
    """trouve l'ip du routeur(la derniere ip)
    Entrée:IP du réseau(str)
    Sortie:Ip du routeur(str)"""
    nouvelle_chaine=""
    ip_masque = ("0" * masque) + ("1" * (32 - masque))
    ip_masque = ip_masque[0:8] + "." + ip_masque[8:16] + "." + ip_masque[16:24] + "." + ip_masque[24:]
    for i in range(len(IP)-1):
        if IP[i] == "0" and ip_masque[i] == "0":
            nouvelle_chaine += "0"
        elif IP[i] == ".":
            nouvelle_chaine += "."
        else:
            nouvelle_chaine += "1"
    nouvelle_chaine+="0"
    return vers_base_dix(nouvelle_chaine)
    
def trouve_IP_dhcp(IP,masque):
    """ retourne l'IP de diffusion à partir d'une IP d'une machine et du masque
        Entrée : IP est une chaine de caractères (0 ou 1) et masque est un nombre entier (int)
        Sortie : IP du réseau : chaine de caractères (0 ou 1)"""
    nouvelle_chaine = ""
    ip_masque = ("1" * masque) + ("0" * (32 - masque))
    ip_masque = ip_masque[0:8] + "." + ip_masque[8:16] + "." + ip_masque[16:24] + "." + ip_masque[24:]
    for i in range(len(IP)-1):
        if IP[i] == "1" and ip_masque[i] == "1":
            nouvelle_chaine += "1"
        elif IP[i] == ".":
            nouvelle_chaine += "."
        else:
            nouvelle_chaine += "0"
    nouvelle_chaine+="1"
    return vers_base_dix(nouvelle_chaine)

def nombre_machine(masque):
    """ retourne le nombre de machines possible sur le réseau
        Entrée : le masque(int)
        Sortie : le nombre de machines dispo(int"""
    return 2**(32-masque)-4

def plage_dispo(IP1,IP_dhcp,masque):
    """ retourne la prochaine IP applicabe et la derniere aplicable
        Entrée : L IP précedente(str) et lIP dhcp(str) et le masque(int)
        Sortie : la prochaine IP applicabe(str et la derniere aplicable(str)"""
    ip_masque = ("1" * masque) + ("0" * (32 - masque))
    ip_masque = ip_masque[0:8] + "." + ip_masque[8:16] + "." + ip_masque[16:24] + "." + ip_masque[24:]
    proch_IP=IP1
    proch_IP=proch_IP.split(".")
    if int(proch_IP[3])<255:
        proch_IP[3]=str(1+int(proch_IP[3]))
    else:
        proch_IP[2]=str(1+int(proch_IP[2]))
    proch_IP=".".join(proch_IP)
    
    ip_masque = ("1" * masque) + ("0" * (32 - masque))
    ip_masque = ip_masque[0:8] + "." + ip_masque[8:16] + "." + ip_masque[16:24] + "." + ip_masque[24:]
    der_IP=IP_dhcp
    der_IP=der_IP.split(".")
    if int(der_IP[3])==0:
        der_IP[2]=str(int(der_IP[2])-1)
    else:
        der_IP[3]=str(int(der_IP[3])-1)
    der_IP=".".join(der_IP)
    return proch_IP, " à ",der_IP
    
    
if __name__ == '__main__' :
    # les tests 
    
    monIP1 = "01011011.10011011.10111000.00111001" #91.155.184.57
    masque1 = 15
    print("l'ip du reseau est:    ",trouve_IP_reseau(monIP1, masque1))
    print("l'ip de diffusion est: ",trouve_IP_diffusion(monIP1, masque1))
    print("l'ip du routeur est:   ",trouve_IP_routeur(monIP1, masque1))
    print("l'ip du dhcp est:      ",trouve_IP_dhcp(monIP1, masque1))
    print("le nombre de machine dispo est: ",nombre_machine(masque1)," machines")
    print("la plague disponible est de",plage_dispo("91.154.0.1","91.155.255.254",masque1))
    
    print("les tests sont validés") 