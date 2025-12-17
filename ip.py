from random import *

def ipDixABinaire(ip):
    sortie = []
    ip = ip.split(".")
    for octet in ip:
        octet = bin(int(octet))[2:]
        sortie.append("0"*(8-len(octet)) + octet)
    return ".".join(sortie)

def ipBinaireADix(ip_binaire):
    ip_binaire = ip_binaire.split(".")
    return ".".join("0"*(8-len(octet)) + str(int(octet,2)) for octet in ip_binaire)


###################################################################################################
###################################################################################################
###################################################################################################

def ip_reseau(ip,masque):
    ip_binaire = ipDixABinaire(ip)

    masque = "1"*masque + "0"*(32-masque)
    masque = f'{masque[:8]}.{masque[8:16]}.{masque[16:24]}.{masque[24:]}'

    sortie = ""

    for i in range(len(masque)):
        if ip_binaire[i] == "1" and masque[i] == "1":
            sortie += "1"
        elif ip_binaire[i] == "." and masque[i] == ".":
            sortie += "."
        else:
            sortie += "0"
    
    return ipBinaireADix(sortie)

def ip_diffusion(ip,masque):
    ip_binaire = ipDixABinaire(ip)

    masque = "0"*masque + "1"*(32-masque)
    masque = f'{masque[:8]}.{masque[8:16]}.{masque[16:24]}.{masque[24:]}'

    sortie = ""

    for i in range(len(masque)):
        if ip_binaire[i] == "0" and masque[i] == "0":
            sortie += "0"
        elif ip_binaire[i] == "." and masque[i] == ".":
            sortie += "."
        else:
            sortie += "1"
    
    return ipBinaireADix(sortie)

def ip_routeur(ip,masque):
    diffusion = ip_diffusion(ip,masque)
    diffusion = diffusion.split(".")

    diffusion[-1] = str(int(diffusion[-1]) - 1)

    return ".".join(diffusion)

def ip_dhcp(ip,masque):
    reseau = ip_reseau(ip,masque)
    reseau = reseau.split(".")

    reseau[-1] = str(int(reseau[-1]) + 1)

    return ".".join(reseau)

def plage_adressable(ip,masque):
    if masque >= 30:
        return "Masque trop petit pour y ajouter un routeur ou un dhcp"
    return 2**(32-masque)-4
    debut = ip_reseau(ip,masque)
    debut = debut.split(".")
    debut[-1] = str(int(debut[-1]) + 2)
    debut = ".".join(debut)
    
    fin = ip_diffusion(ip,masque)
    fin = fin.split(".")
    fin[-1] = str(int(fin[-1]) - 2)
    fin = ".".join(fin)
    
    return f'La plage addressable va de {debut} à {fin}'

def nombre_machines(ip,masque):
    return 2**(32-masque)-4

ACTIONS = {
    "reseau": ip_reseau,
    "diffusion": ip_diffusion,
    "routeur": ip_routeur,
    "dhcp": ip_dhcp,
    "plage": plage_adressable,
    "machines": nombre_machines,
}

def Choix(ip,masque,action):
    if masque >= 30:
        return "Masque trop petit pour y ajouter un routeur ou un dhcp"
    try:
        return ACTIONS[action](ip,masque)
    except KeyError:
        print("Action Invalide")

# ip = f"{randint(0,255)}.{randint(0,255)}.{randint(0,255)}.{randint(0,255)}"
# masque = randint(0,32)

ip = "192.168.1.99"
masque = 28

print(f"L'ip choisie est {ip}/{masque}")
print("L'ip réseau est " + Choix(ip,masque,"reseau"))
print("L'ip de diffusion est " + Choix(ip,masque,"diffusion"))
print("L'ip du routeur est " + Choix(ip,masque,"routeur"))
print("L'ip dhcp est " + Choix(ip,masque,"dhcp"))
print(Choix(ip,masque,"plage"))
print(str(Choix(ip,masque,"machines")) + " machines assignables sur le réseau\n")
