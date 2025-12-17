##---les fonctions---##
def trouve_IP_reseau(IP,masque):
    """ retourne l'IP réseau à partir d'une IP d'une machine et du masque
        Entrée : IP est une chaine de caractères (0 ou 1) et masque est un nombre entier (int)
        Sortie : IP du réseau : chaine de caractères (0 ou 1)"""
    binaire = '.'.join(format(int(i), '08b') for i in IP.split('.'))
    
    nouvelle_chaine = ""
    ip_masque = ("1" * masque) + ("0" * (32 - masque))
    ip_masque = ip_masque[0:8] + "." + ip_masque[8:16] + "." + ip_masque[16:24] + "." + ip_masque[24:]
    for i in range(len(binaire)):
        if binaire[i] == "1" and ip_masque[i] == "1":
            nouvelle_chaine += "1"
        elif binaire[i] == ".":
            nouvelle_chaine += "."
        else:
            nouvelle_chaine += "0"
    liste_temp = []
    for elmt in(nouvelle_chaine):
        liste_temp.append(elmt)
    ip = '.'.join(str(int(octet, 2)) for octet in nouvelle_chaine.split('.'))

    return ip
    #return nouvelle_chaine
        

def trouve_IP_diffusion(IP,masque):
    """ retourne l'IP de diffusion à partir d'une IP d'une machine et du masque
        Entrée : IP est une chaine de caractères (0 ou 1) et masque est un nombre entier (int)
        Sortie : IP du réseau : chaine de caractères (0 ou 1)"""
    binaire = '.'.join(format(int(i), '08b') for i in IP.split('.'))
    
    nouvelle_chaine = ""
    ip_masque = ("0" * masque) + ("1" * (32 - masque))
    ip_masque = ip_masque[0:8] + "." + ip_masque[8:16] + "." + ip_masque[16:24] + "." + ip_masque[24:]
    for i in range(len(binaire)):
        if binaire[i] == "0" and ip_masque[i] == "0":
            nouvelle_chaine += "0"
        elif binaire[i] == ".":
            nouvelle_chaine += "."
        else:
            nouvelle_chaine += "1"
    ip = '.'.join(str(int(octet, 2)) for octet in nouvelle_chaine.split('.'))
    return ip

def ip_routeur(IP, masque):
    binaire = '.'.join(format(int(i), '08b') for i in IP.split('.'))
    
    nouvelle_chaine = ""
    ip_masque = ("0" * masque) + ("1" * (32 - masque))
    ip_masque = ip_masque[0:8] + "." + ip_masque[8:16] + "." + ip_masque[16:24] + "." + ip_masque[24:]
    for i in range(len(binaire)):
        if binaire[i] == "0" and ip_masque[i] == "0":
            nouvelle_chaine += "0"
        elif binaire[i] == ".":
            nouvelle_chaine += "."
        else:
            nouvelle_chaine += "1"
    ip = '.'.join(str(int(octet, 2)) for octet in nouvelle_chaine.split('.'))

    temp = []
    for elmt in ip.split('.'):
        temp.append(int(elmt))
    temp[-1] -= 1
    iprouteur = ""
    compteur = 0
    for elmt in temp:
        iprouteur += str(elmt)
        if compteur < 3:
            compteur +=1
            iprouteur += "."
    return iprouteur
    
def ip_serveur_dhcp(IP,masque):
    """ retourne l'IP réseau à partir d'une IP d'une machine et du masque
        Entrée : IP est une chaine de caractères (0 ou 1) et masque est un nombre entier (int)
        Sortie : IP du réseau : chaine de caractères (0 ou 1)"""
    binaire = '.'.join(format(int(i), '08b') for i in IP.split('.'))
    
    nouvelle_chaine = ""
    ip_masque = ("1" * masque) + ("0" * (32 - masque))
    ip_masque = ip_masque[0:8] + "." + ip_masque[8:16] + "." + ip_masque[16:24] + "." + ip_masque[24:]
    for i in range(len(binaire)):
        if binaire[i] == "1" and ip_masque[i] == "1":
            nouvelle_chaine += "1"
        elif binaire[i] == ".":
            nouvelle_chaine += "."
        else:
            nouvelle_chaine += "0"
    liste_temp = []
    for elmt in(nouvelle_chaine):
        liste_temp.append(elmt)
    ip = '.'.join(str(int(octet, 2)) for octet in nouvelle_chaine.split('.'))

    temp = []
    for elmt in ip.split('.'):
        temp.append(int(elmt))
    temp[-1] += 1
    ip_dhcp = ""
    compteur = 0
    for elmt in temp:
        ip_dhcp += str(elmt)
        if compteur < 3:
            compteur +=1
            ip_dhcp += "."
    return ip_dhcp

def plage_adressable(IP, masque):
    ip_max = ip_routeur(IP, masque)
    ip_min = ip_serveur_dhcp(IP, masque)
    temp = []
    for elmt in ip_max.split('.'):
        temp.append(int(elmt))
    temp[-1] -= 1
    ip_max = ""
    compteur = 0
    for elmt in temp: #dernière ip possible après le routeur
        ip_max+= str(elmt)
        if compteur < 3:
            compteur +=1
            ip_max += "."
    
    temp = []
    for elmt in ip_min.split('.'):
        temp.append(int(elmt))
    temp[-1] += 1
    ip_min = ""
    compteur = 0
    for elmt in temp: #1ère ip possible après le dhcp
        ip_min+= str(elmt)
        if compteur < 3:
            compteur +=1
            ip_min += "."
    return ip_min, "et", ip_max



def nombre_machine(masque):
    machine = 2**(32-masque) -4
    return machine


if __name__ == '__main__' :
    # les tests 
    #monIP1 = "91.155.184.57" #91.155.184.57
    monIP1 = str(input("Entrez votre ip: \n"))
    compteur_de_points = 0
    for elmt in monIP1:
        if elmt == ".":
            compteur_de_points += 1
    if compteur_de_points != 3:
        print ("votre ip n'est pas valide")
    else:
        #masque1 = 15
        masque1 = int(input("Entrez un masque: \n"))
        if masque1 < 0 or masque1 > 32:
            print("le masque n'est pas valide")
        else:
            print("l'adresse réseau est", trouve_IP_reseau(monIP1, masque1))
            print("l'adresse de diffusion", trouve_IP_diffusion(monIP1, masque1))
            print("l'ip du routeur est" ,ip_routeur(monIP1, masque1))
            print("l'ip du serveur dhcp est" ,ip_serveur_dhcp(monIP1, masque1))
            print("la plage adressable se situe entre" ,plage_adressable(monIP1, masque1))
            print("le nombres de machines dispo sur le réseau est de", nombre_machine(masque1))    
            print("les tests sont validés")