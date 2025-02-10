from deck import *
from main_joueur import *
from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
from os import *
from time import sleep
import sqlite3

# Jeu

deck = Deck()
deck.remplir_entier()
deck.melange()
main = Main(deck)
main.creer_main()
main.trier_mains()

# Création de la fenêtre

fenetre = Tk()
fenetre.title("Cosmunos")
fenetre.geometry("1600x800")
fenetre.attributes("-fullscreen", True)

# Fond

fond = "#1e1e1e"
fenetre.config(bg=fond)

# Fonction pour mettre à jour l'affichage des cartes tourbées

def update_display():

    global main
    global image_dos_carte_rotate

    for widget in frame.winfo_children():
        widget.destroy()

    col = 0
    
    for i in range (main.nb_main()):

        Label(frame, image=image_dos_carte_rotate, padx=10, pady=5, bg=fond).grid(row=0, column=col, padx=0)
        col += 1

    fenetre.update()

def fichier_carte(carte):

    connexion = sqlite3.connect('carte/carte.db')
    c = connexion.cursor()

    c.execute("SELECT chemin FROM carte WHERE IDCouleur = ? AND IDCarte = ?", (carte.get_couleur(),carte.get_nombre()))
    chemin = c.fetchall()[0][0]

    return chemin
    
    
frame = Frame(fenetre)
frame.pack(pady=20)

image_path = path.abspath("carte/autre/Dos.png")

image_dos_carte = Image.open(image_path)
ratio = 0.1
new_size = (int(image_dos_carte.width * ratio), int(image_dos_carte.height * ratio))
image_dos_carte = image_dos_carte.resize(new_size)
image_dos_carte_rotate = image_dos_carte.rotate(180)
image_dos_carte_rotate = ImageTk.PhotoImage(image_dos_carte_rotate)

print (main.choix_carte(0))
print(fichier_carte(main.choix_carte(0)))

update_display()

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
