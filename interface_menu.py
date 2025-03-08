from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
from os import path
from interface_jeu_POO import *  # Assurez-vous que votre classe PartieJeu est importée ici.

class Menu(Frame):
    def __init__(self, parent, frame_jeu):
        super().__init__(parent)
        self.frame_jeu = frame_jeu
        self.config(bg="#1e1e1e", width=1600, height=800)
        self.pack(fill="both", expand=True)

        # Musique de fond
        main_theme_path = path.abspath("Interface/Son/Main_Theme.mp3")
        mixer.init()
        mixer.music.load(main_theme_path)
        mixer.music.play(-1)

        # Création des éléments du menu
        self.creer_widgets()

    def creer_widgets(self):
        """Crée les éléments du menu (logo, boutons, etc.)"""

        # Logo
        logo_path = path.abspath("Interface/Logo.png")
        logo_image = Image.open(logo_path).resize((450, 450))
        self.logo_image = ImageTk.PhotoImage(logo_image)
        logo_label = Label(self, image=self.logo_image, bg="#1e1e1e")
        logo_label.place(relx=0.5, rely=0.25, anchor='center')

        # Bouton Jouer
        bouton1_path = path.abspath("Interface/Bouton/Bouton Jouer.png")
        bouton1_image_normal = Image.open(bouton1_path).resize((400, 130))
        self.bouton1_image_normal = ImageTk.PhotoImage(bouton1_image_normal)

        bouton1_image_large = Image.open(bouton1_path).resize((480, 156))
        self.bouton1_image_large = ImageTk.PhotoImage(bouton1_image_large)

        bouton1_button = Button(self, image=self.bouton1_image_normal, bg="#1e1e1e", width=400, height=100, command=self.bouton_jouer, borderwidth=0, activebackground="#1e1e1e")
        bouton1_button.place(relx=0.5, rely=0.7, anchor='center')

        bouton1_button.bind("<Enter>", self.bouton_jouer_entrer)
        bouton1_button.bind("<Leave>", self.bouton_jouer_sortie)

        # Bouton Quitter
        bouton3_path = path.abspath("Interface/Bouton/Bouton Quitter.png")
        bouton3_image_normal = Image.open(bouton3_path).resize((400, 130))
        self.bouton3_image_normal = ImageTk.PhotoImage(bouton3_image_normal)

        bouton3_image_large = Image.open(bouton3_path).resize((480, 156))
        self.bouton3_image_large = ImageTk.PhotoImage(bouton3_image_large)

        bouton3_button = Button(self, image=self.bouton3_image_normal, bg="#1e1e1e", width=400, height=100, command=self.bouton_quitter, borderwidth=0, activebackground="#1e1e1e")
        bouton3_button.place(relx=0.5, rely=0.82, anchor='center')

        bouton3_button.bind("<Enter>", self.bouton_quitter_entrer)
        bouton3_button.bind("<Leave>", self.bouton_quitter_sortie)

    def bouton_jouer(self):
        """Action pour démarrer la partie"""
        if not hasattr(self, 'partie_en_cours'):
            print("Je passe ici")
            self.partie_en_cours = PartieJeu(self.frame_jeu, self)  # Passer self (Menu) pour garder l'état
            self.partie_en_cours.pack(fill="both", expand=True)
            self.pack_forget()  # Masquer le menu une fois la partie lancée

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
menu = Menu(fenetre, frame_jeu)

fenetre.mainloop()
