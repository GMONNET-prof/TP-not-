##---les fonctions---##
def base2tobase10(binary):
    base2 = []
    base10 = 0
    
    for i in str(binary):
        base2.append(i)
        
    base2.reverse()
    
    for i in range(0,len(base2)):
        base10 += int(base2[i])*(2**i)
    return base10



def base10tobase2(decimal):
    base2 = []
    
    while decimal // 2 != 0:
        base2.append(decimal % 2)
        decimal = decimal // 2
    if decimal == 1:
        base2.append(decimal % 2)
    base2.reverse()
    return base2



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
    
    return nouvelle_chaine


def convertisseur_base_10(IP):
    IP_base_10 = ""
    
    premiere_part = IP[:8]
    deuxieme_part = IP[9:17]
    troisieme_part = IP[18:26]
    derniere_part = IP[27:]
    
    conv_premiere_part = base2tobase10(premiere_part)
    conv_deuxieme_part = base2tobase10(deuxieme_part)
    conv_troisieme_part = base2tobase10(troisieme_part)
    conv_derniere_part = base2tobase10(derniere_part)
    
    IP_base_10 = str(conv_premiere_part) + "." + str(conv_deuxieme_part) + "." + str(conv_troisieme_part) + "." + str(conv_derniere_part)
        
    return IP_base_10


def IP_routeur(IP, masque):
    IP_dif = trouve_IP_diffusion(IP, masque)                            #trouve ip diffusion en binaire
    #print("l'ip de diffusion :", IP_dif)
    huit_derniere = IP_dif[27:]
    #print(huit_derniere)
    huit_derniere_base_10 = base2tobase10(huit_derniere)
    #print("huit_derniere_base_10", huit_derniere_base_10)
    huit_derniere_base_10 -= 1                                          #enleve 1 pour trouver la derniere ip disponible
    huit_derniere_base_2 = base10tobase2(huit_derniere_base_10)         #convertion en binaire
    #print(huit_derniere_base_2)
    IP_rout = IP_dif[:27]
    #print("l'ip routeur sans les 8 derniere :", IP_rout)
    for element in huit_derniere_base_2:
        IP_rout += str(element)
    Ip_rout_base_10 = convertisseur_base_10(IP_rout)
    return Ip_rout_base_10


def IP_DHCP(IP, masque):
    IP_res = trouve_IP_reseau(IP, masque)                            #trouve ip reseau en binaire
    huit_derniere = IP_res[27:]
    #print(huit_derniere)
    huit_derniere_base_10 = base2tobase10(huit_derniere)
    #print("huit_derniere_base_10", huit_derniere_base_10)
    huit_derniere_base_10 += 1                                          #ajoute 1 pour trouver la premiere ip disponible
    huit_derniere_base_2 = base10tobase2(huit_derniere_base_10)         #convertion en binaire
    #print(huit_derniere_base_2)
    IP_rout = IP_res[:27]
    #print("l'ip routeur sans les 8 derniere :", IP_rout)
    for element in huit_derniere_base_2:
        IP_rout += str(element)
    Ip_rout_base_10 = convertisseur_base_10(IP_rout)
    return Ip_rout_base_10


if __name__ == '__main__' :
    # les tests 
    monIP1 = "01011011.10011011.10111000.00111001" #91.155.184.57
    masque1 = 15
    print("adresse reseau", trouve_IP_reseau(monIP1, masque1))
    print("adresse de diffusion", trouve_IP_diffusion(monIP1, masque1))
    print("convertion", convertisseur_base_10(monIP1))
    print("IP routeur :", IP_routeur(monIP1, masque1))
    print("IP_DHCP :", IP_DHCP(monIP1, masque1))

    
    print("les tests sont validés") 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    