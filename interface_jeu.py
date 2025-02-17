from deck import *
from main_joueur import *
from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
from os import *
from time import sleep
import sqlite3

# Jeu

image_cartes_joueur = []
deck = Deck()
deck.remplir_entier()
deck.melange()
mainIA = Main(deck)
mainIA.creer_main()
mainIA.trier_mains()
mainJoueur = Main(deck)
mainJoueur.creer_main()
mainJoueur.trier_mains()

# Création de la fenêtre

fenetre = Tk()
fenetre.title("Cosmunos")
fenetre.geometry("1600x800")
fenetre.attributes("-fullscreen", True)

# Fond

fond = "#1e1e1e"
fenetre.config(bg=fond)

# Fonction pour mettre à jour l'affichage des cartes tourbées

def update_cartesIA():

    global mainIA
    global image_dos_carte_rotate

    for widget in frame_cartes_ia.winfo_children():
        widget.destroy()

    col = 0
    
    for i in range(mainIA.nb_main()):

        Label(frame_cartes_ia, image=image_dos_carte_rotate, padx=10, pady=5, bg=fond).grid(row=0, column=col, padx=0)
        col += 1

    fenetre.update()

def update_cartesJoueur():

    global mainJoueur
    global image_cartes_joueur

    for widget in frame_cartes_joueur.winfo_children():
        widget.destroy()

    col = 0
    
    for i in range(mainJoueur.nb_main()):

        chemin = path.abspath(fichier_carte(mainJoueur.selection_carte(i)))
        image_carte = Image.open(chemin)
        ratio = 0.1
        new_size = (int(image_carte.width * ratio), int(image_carte.height * ratio))
        image_carte = image_carte.resize(new_size)
        image_carte = ImageTk.PhotoImage(image_carte)
        image_cartes_joueur.append(image_carte)

        Button(frame_cartes_joueur, image=image_carte, padx=10, pady=5, bg=fond, borderwidth=0, activebackground="#1e1e1e").grid(row=0, column=col, padx=0)
        col += 1

    fenetre.update()

def fichier_carte(carte):

    connexion = sqlite3.connect('carte/carte.db')
    c = connexion.cursor()

    c.execute("SELECT chemin FROM carte WHERE IDCouleur = ? AND IDCarte = ?", (carte.get_couleur(), carte.get_nombre()))
    chemin = c.fetchall()[0][0]

    return chemin
    
# Création des frames
frame_cartes_ia = Frame(fenetre, bg=fond)
frame_cartes_ia.pack(side=TOP, pady=20)

frame_cartes_joueur = Frame(fenetre, bg=fond)
frame_cartes_joueur.pack(side=BOTTOM, pady=20)

frame_milieu = Frame(fenetre, bg=fond) 
frame_milieu.pack(anchor=CENTER)

# Charger l'image de la carte dos
image_path = path.abspath("carte/autre/Dos.png")
image_dos_carte = Image.open(image_path)
ratio = 0.1
new_size = (int(image_dos_carte.width * ratio), int(image_dos_carte.height * ratio))
image_dos_carte = image_dos_carte.resize(new_size)
image_dos_carte_rotate = image_dos_carte.rotate(180)
image_dos_carte_rotate = ImageTk.PhotoImage(image_dos_carte_rotate)
image_dos_carte = ImageTk.PhotoImage(image_dos_carte)

# Créer le bouton pioche avec l'image de la carte dos
pioche = Button(frame_milieu, image=image_dos_carte, padx=10, pady=5, bg=fond, borderwidth=0, activebackground="#1e1e1e")

pioche.pack(anchor=CENTER, pady=90, padx=10)

# Mettre à jour l'affichage des cartes
update_cartesIA()
update_cartesJoueur()

# Essaie

# for k in range(3):
#     sleep(1)
#     main.ajouter_carte(deck.retirer_carte()) 
#     update_display()
#     sleep(1) 

# for i in range(3):
#     main.choix_carte(i)
#     update_display()
#     sleep(1)

fenetre.mainloop()
