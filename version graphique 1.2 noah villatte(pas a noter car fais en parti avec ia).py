import tkinter as tk
from tkinter import messagebox, filedialog
import re
import csv
import os
import subprocess

# Fonctions de calcul réseau
def valide_ip(ip):
    """ Vérifie si l'IP est valide """
    pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    if re.match(pattern, ip):
        octets = ip.split(".")
        for octet in octets:
            if int(octet) < 0 or int(octet) > 255:
                return False
        return True
    return False

def is_ip_privee(ip):
    """ Vérifie si l'IP appartient à un réseau privé """
    octets = ip.split(".")
    # Réseaux privés : 10.x.x.x, 172.16.x.x - 172.31.x.x, 192.168.x.x
    return (int(octets[0]) == 10 or
            (int(octets[0]) == 172 and 16 <= int(octets[1]) <= 31) or
            (int(octets[0]) == 192 and int(octets[1]) == 168))

def trouve_IP_reseau(IP, masque):
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
    return ".".join(str(int(octet, 2)) for octet in octets)

def trouver_ip_binaire(IP):
    liste_finale = []
    liste_morceaux = IP.split(".")
    for nombre in liste_morceaux:
        quotient = int(nombre)
        chaine = ""
        while quotient != 0:
            reste = quotient % 2
            quotient = quotient // 2
            chaine = str(reste) + chaine
        chaine = "0" * (8 - len(chaine)) + chaine
        liste_finale.append(chaine)
    return ".".join(liste_finale)

def trouve_IP_diffusion(IP, masque):
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
    return ".".join(str(int(octet, 2)) for octet in octets)

def IP_routeur(IP, masque):
    ip_diffusion = trouve_IP_diffusion(IP, masque)
    octets = ip_diffusion.split(".")
    trois_octet = int(octets[3]) - 1
    octets.pop(3)
    octets.append(trois_octet)
    return ".".join(str(int(octet)) for octet in octets)

def IP_DHCP(IP, masque):
    ip_reseau = trouve_IP_reseau(IP, masque)
    octets = ip_reseau.split(".")
    trois_octet = int(octets[3]) + 1
    octets.pop(3)
    octets.append(trois_octet)
    return ".".join(str(int(octet)) for octet in octets)

def nb_de_machine_sur_reseau(masque):
    return (2 ** (32 - masque)) - 4

def plage_adressable(IP, masque):
    ip_routeur = IP_routeur(IP, masque)
    octets = ip_routeur.split(".")
    trois_octet = int(octets[3]) - 1
    octets.pop(3)
    octets.append(trois_octet)
    ip_derniere = ".".join(str(int(octet)) for octet in octets)

    ip_dhcp = IP_DHCP(IP, masque)
    octets = ip_dhcp.split(".")
    trois_octet = int(octets[3]) + 1
    octets.pop(3)
    octets.append(trois_octet)
    ip_premiere = ".".join(str(int(octet)) for octet in octets)

    return f"La plage adressable va de l'ip {ip_premiere} à l'ip {ip_derniere}"

# Vérifier la connectivité (ping)
def verifier_connectivite():
    ip = ip_entry.get()
    if not valide_ip(ip):
        messagebox.showerror("Erreur", "Veuillez entrer une IP valide pour effectuer le test.")
        return
    try:
        response = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if response.returncode == 0:
            messagebox.showinfo("Connectivité", f"Ping vers {ip} réussi !")
        else:
            messagebox.showerror("Connectivité", f"Échec du ping vers {ip}.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors du test de connectivité : {e}")

# Fonction pour afficher et exporter les résultats
def calculer():
    ip = ip_entry.get()
    masque = masque_entry.get()

    if not ip or not masque:
        messagebox.showerror("Erreur", "Veuillez entrer à la fois une IP et un masque.")
        return

    if not valide_ip(ip):
        messagebox.showerror("Erreur", "L'IP entrée n'est pas valide. Veuillez entrer une IP correcte.")
        return

    try:
        masque = int(masque)
        if masque < 0 or masque > 32:
            messagebox.showerror("Erreur", "Le masque de sous-réseau doit être entre 0 et 32.")
            return
    except ValueError:
        messagebox.showerror("Erreur", "Le masque de sous-réseau doit être un entier valide.")
        return

    # Convertir IP en binaire
    ip_binaire = trouver_ip_binaire(ip)
    ip_binaire_label.config(text=f"IP Binaire: {ip_binaire}")

    # Vérifier si l'IP est privée ou publique
    if is_ip_privee(ip):
        ip_type_label.config(text="Type d'IP : Privée")
    else:
        ip_type_label.config(text="Type d'IP : Publique")

    # Calculer les résultats
    ip_reseau = trouve_IP_reseau(ip_binaire, masque)
    ip_diffusion = trouve_IP_diffusion(ip_binaire, masque)
    ip_routeur_resultat = IP_routeur(ip_binaire, masque)
    ip_dhcp_resultat = IP_DHCP(ip_binaire, masque)
    nb_machines = nb_de_machine_sur_reseau(masque)
    plage = plage_adressable(ip_binaire, masque)

    # Affichage des résultats
    result_label.config(
        text=f"IP Réseau: {ip_reseau}\n"
             f"IP Diffusion: {ip_diffusion}\n"
             f"IP Routeur: {ip_routeur_resultat}\n"
             f"IP DHCP: {ip_dhcp_resultat}\n"
             f"Nombre de machines: {nb_machines}\n"
             f"Plage Adressable: {plage}"
    )

# Fonction d'exportation
def exporter_resultats():
    ip = ip_entry.get()
    masque = masque_entry.get()

    if not ip or not masque:
        messagebox.showerror("Erreur", "Veuillez entrer à la fois une IP et un masque.")
        return

    if not valide_ip(ip):
        messagebox.showerror("Erreur", "L'IP entrée n'est pas valide. Veuillez entrer une IP correcte.")
        return

    try:
        masque = int(masque)
        if masque < 0 or masque > 32:
            messagebox.showerror("Erreur", "Le masque de sous-réseau doit être entre 0 et 32.")
            return
    except ValueError:
        messagebox.showerror("Erreur", "Le masque de sous-réseau doit être un entier valide.")
        return

    ip_binaire = trouver_ip_binaire(ip)
    ip_reseau = trouve_IP_reseau(ip_binaire, masque)
    ip_diffusion = trouve_IP_diffusion(ip_binaire, masque)
    ip_routeur_resultat = IP_routeur(ip_binaire, masque)
    ip_dhcp_resultat = IP_DHCP(ip_binaire, masque)
    nb_machines = nb_de_machine_sur_reseau(masque)
    plage = plage_adressable(ip_binaire, masque)

    resultats = [
        ["IP", ip],
        ["Masque", masque],
        ["IP Réseau", ip_reseau],
        ["IP Diffusion", ip_diffusion],
        ["IP Routeur", ip_routeur_resultat],
        ["IP DHCP", ip_dhcp_resultat],
        ["Nombre de machines", nb_machines],
        ["Plage Adressable", plage]
    ]

    # Demander où sauvegarder le fichier
    fichier = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("CSV files", "*.csv")])
    if fichier:
        with open(fichier, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(resultats)
        messagebox.showinfo("Succès", "Les résultats ont été exportés avec succès.")

# Fonction de réinitialisation
def reinitialiser():
    ip_entry.delete(0, tk.END)
    masque_entry.delete(0, tk.END)
    result_label.config(text="")
    ip_binaire_label.config(text="IP Binaire: ")
    ip_type_label.config(text="Type d'IP : ")
    ip_entry.focus()

# Fonction pour l'aide
def afficher_aide():
    messagebox.showinfo("Aide", 
        "Entrez une adresse IP valide (ex: 192.168.1.1) et un masque de sous-réseau en bits (ex: 24).\n"
        "Le calcul affichera l'IP du réseau, l'IP de diffusion, l'IP du routeur, l'IP du serveur DHCP, "
        "le nombre de machines possibles et la plage adressable.\n"
        "Vous pouvez exporter ces résultats dans un fichier texte ou CSV.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Calculateur d'IP Réseau")
root.geometry("900x700")
root.config(bg="#f4f4f9")

# Frame pour organiser les widgets
frame = tk.Frame(root, bg="#f4f4f9")
frame.pack(pady=20)

# Titre
title_label = tk.Label(frame, text="Calculateur d'IP Réseau", font=("Arial", 18, "bold"), bg="#f4f4f9")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Champ pour l'IP
ip_label = tk.Label(frame, text="Adresse IP :", font=("Arial", 12), bg="#f4f4f9")
ip_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
ip_entry = tk.Entry(frame, font=("Arial", 12))
ip_entry.grid(row=1, column=1, padx=10, pady=10)

# Champ pour le masque
masque_label = tk.Label(frame, text="Masque de sous-réseau :", font=("Arial", 12), bg="#f4f4f9")
masque_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
masque_entry = tk.Entry(frame, font=("Arial", 12))
masque_entry.grid(row=2, column=1, padx=10, pady=10)

# Affichage du type d'IP
ip_type_label = tk.Label(frame, text="Type d'IP : ", font=("Arial", 12), bg="#f4f4f9")
ip_type_label.grid(row=3, column=0, columnspan=2, pady=10)

# Boutons
calcul_button = tk.Button(frame, text="Calculer", font=("Arial", 12), command=calculer, bg="#4CAF50", fg="white", relief="raised", width=15)
calcul_button.grid(row=4, column=0, columnspan=2, pady=20)

export_button = tk.Button(frame, text="Exporter", font=("Arial", 12), command=exporter_resultats, bg="#FF9800", fg="white", relief="raised", width=15)
export_button.grid(row=5, column=0, columnspan=2, pady=10)

reinitialiser_button = tk.Button(frame, text="Réinitialiser", font=("Arial", 12), command=reinitialiser, bg="#f44336", fg="white", relief="raised", width=15)
reinitialiser_button.grid(row=6, column=0, columnspan=2, pady=10)

# Vérification de la connectivité
ping_button = tk.Button(frame, text="Vérifier la Connectivité", font=("Arial", 12), command=verifier_connectivite, bg="#2196F3", fg="white", relief="raised", width=20)
ping_button.grid(row=7, column=0, columnspan=2, pady=20)

# Affichage des résultats
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f4f4f9", justify="left")
result_label.pack(pady=20)

# Affichage IP binaire
ip_binaire_label = tk.Label(root, text="IP Binaire: ", font=("Arial", 12), bg="#f4f4f9")
ip_binaire_label.pack(pady=10)

# Bouton d'aide
aide_button = tk.Button(root, text="Aide", font=("Arial", 12), command=afficher_aide, bg="#2196F3", fg="white", relief="raised")
aide_button.pack(pady=10)

# Lancer l'application
root.mainloop()


