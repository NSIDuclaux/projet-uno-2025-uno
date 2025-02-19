from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
from os import *
from interface_jeu import *  # Import du fichier contenant le jeu

def lancer_jeu():
    from interface_jeu import fenetre as jeu_fenetre
    jeu_fenetre.mainloop()


# Fonctions de navigation entre les frames
def affiché_frame_menu():
    frame_jeu.pack_forget()
    frame_menu.pack(fill="both", expand=True)

def affiché_frame_jeu():
    frame_menu.pack_forget()
    frame_jeu.pack(fill="both", expand=True)
    lancer_jeu()  # Lance le jeu lorsque le joueur clique sur "Jouer"

def affiché_frame_parametre():
    frame_menu.pack_forget()
    frame_parametre.pack(fill="both", expand=True)

# Fonctions des boutons
def bouton_jouer():
    affiché_frame_jeu()

def bouton_parametre():
    affiché_frame_parametre()

def bouton_quitter():
    fenetre.destroy()

# Musique de fond
main_theme_path = path.abspath("Interface/Son/Main_Theme.mp3")
mixer.init()
mixer.music.load(main_theme_path)
mixer.music.play(-1)

# Création de la fenêtre
fenetre = Tk()
fenetre.title("Cosmunos")
fenetre.geometry("1600x800")
fenetre.attributes("-fullscreen", True)

fond = "#1e1e1e"
fenetre.config(bg=fond)

# Frames
frame_menu = Frame(fenetre, bg=fond)
frame_jeu = Frame(fenetre, bg=fond)
frame_parametre = Frame(fenetre, bg=fond)

# Interface du menu
logo_path = path.abspath("Interface/Logo.png")
logo_image = Image.open(logo_path).resize((450, 450))
logo_image = ImageTk.PhotoImage(logo_image)
logo_label = Label(frame_menu, image=logo_image, bg=fond)
logo_label.place(relx=0.5, rely=0.25, anchor='center')

# Boutons du menu
bouton1_image_normal = ImageTk.PhotoImage(Image.open(path.abspath("Interface/Bouton/Bouton Jouer.png")).resize((400, 130)))
bouton1_button = Button(frame_menu, image=bouton1_image_normal, bg=fond, command=bouton_jouer, borderwidth=0)
bouton1_button.place(relx=0.5, rely=0.6, anchor='center')

bouton2_image_normal = ImageTk.PhotoImage(Image.open(path.abspath("Interface/Bouton/Bouton Paramètre.png")).resize((400, 130)))
bouton2_button = Button(frame_menu, image=bouton2_image_normal, bg=fond, command=bouton_parametre, borderwidth=0)
bouton2_button.place(relx=0.5, rely=0.72, anchor='center')

bouton3_image_normal = ImageTk.PhotoImage(Image.open(path.abspath("Interface/Bouton/Bouton Quitter.png")).resize((400, 130)))
bouton3_button = Button(frame_menu, image=bouton3_image_normal, bg=fond, command=bouton_quitter, borderwidth=0)
bouton3_button.place(relx=0.5, rely=0.84, anchor='center')

# Affichage initial du menu
frame_menu.pack(fill="both", expand=True)
fenetre.mainloop()
