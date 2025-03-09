from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
from os import path
from interface_jeu_POO import *

class Menu(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.pack(fill="both", expand=True)
        self.config(bg="#1e1e1e")

        self.frame_menu = Frame(self, bg="#1e1e1e")
        self.frame_jeu = Frame(self,bg="#1e1e1e")
        

        # Musique de fond
        main_theme_path = path.abspath("Interface/Son/Main_Theme.mp3")
        mixer.init()
        mixer.music.load(main_theme_path)
        mixer.music.play(-1)

        # Création des éléments du menu
        self.creer_widgets()

    def creer_widgets(self):

        # Logo
        self.logo_path = path.abspath("Interface/Logo.png")
        self.logo_image = Image.open(self.logo_path).resize((450, 450))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = Label(self.frame_menu, image=self.logo_image, bg="#1e1e1e")
        self.logo_label.place(relx=0.5, rely=0.25, anchor='center') 

        # Bouton Jouer
        bouton1_path = path.abspath("Interface/Bouton/Bouton Jouer.png")
        bouton1_image_normal = Image.open(bouton1_path).resize((400, 130))
        self.bouton1_image_normal = ImageTk.PhotoImage(bouton1_image_normal)

        self.bouton1_image_large = Image.open(bouton1_path).resize((480, 156))
        self.bouton1_image_large = ImageTk.PhotoImage(self.bouton1_image_large)

        self.bouton1_button = Button(self.frame_menu, image=self.bouton1_image_normal, bg="#1e1e1e", width=400, height=100, command=self.bouton_jouer, borderwidth=0, activebackground="#1e1e1e")
        self.bouton1_button.place(relx=0.5, rely=0.7, anchor='center')

        # Ajout des bind après que les boutons ont été créés
        self.bouton1_button.bind("<Enter>", self.bouton_jouer_entrer)
        self.bouton1_button.bind("<Leave>", self.bouton_jouer_sortie)

        # Bouton Quitter
        bouton3_path = path.abspath("Interface/Bouton/Bouton Quitter.png")
        bouton3_image_normal = Image.open(bouton3_path).resize((400, 130))
        self.bouton3_image_normal = ImageTk.PhotoImage(bouton3_image_normal)

        self.bouton3_image_large = Image.open(bouton3_path).resize((480, 156))
        self.bouton3_image_large = ImageTk.PhotoImage(self.bouton3_image_large)

        self.bouton3_button = Button(self.frame_menu, image=self.bouton3_image_normal, bg="#1e1e1e", width=400, height=100, command=self.bouton_quitter, borderwidth=0, activebackground="#1e1e1e")
        self.bouton3_button.place(relx=0.5, rely=0.82, anchor='center')

        self.bouton3_button.bind("<Enter>", self.bouton_quitter_entrer)
        self.bouton3_button.bind("<Leave>", self.bouton_quitter_sortie)

        self.frame_menu.place(relx=0.5, rely=0.5, anchor='center', width=1600, height=800)

    def bouton_jouer(self):
        
        self.frame_menu.pack_forget()
        self.frame_jeu.pack(fill="both", expand=True)
        self.partie_en_cours = PartieJeu(self.frame_jeu, self.frame_menu,fenetre)
        self.partie_en_cours.pack(fill="both", expand=True)
        
    def bouton_jouer_entrer(self, event):
        self.bouton1_button.config(image=self.bouton1_image_large)

    def bouton_jouer_sortie(self, event):
        self.bouton1_button.config(image=self.bouton1_image_normal)

    def bouton_quitter(self):
        """Action pour quitter l'application"""
        fenetre.destroy()

    def bouton_quitter_entrer(self, event):
        self.bouton3_button.config(image=self.bouton3_image_large)

    def bouton_quitter_sortie(self, event):
        self.bouton3_button.config(image=self.bouton3_image_normal)

# Création de la fenêtre

fenetre = Tk()
fenetre.title("Cosmunos")
fenetre.geometry("1600x800")
fenetre.attributes("-fullscreen", True)

# Fond

fond = "#1e1e1e"
fenetre.config(bg=fond)

# Création des frames
frame_jeu = Frame(fenetre, bg=fond)

# Création du menu
menu = Menu(fenetre)

fenetre.mainloop()