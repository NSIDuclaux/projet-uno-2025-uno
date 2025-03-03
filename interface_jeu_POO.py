from deck import *
from main_joueur import *
from tkinter import *
from PIL import Image, ImageTk
from os import *
import sqlite3
from main_joueur import Main
from carte_valide import *
from carte_effet import *
from bot import *
from random import randint

class PartieJeu:

    def __init__(self):

        # Création de la pioche
        
        self.deckPartie = Deck()
        self.deckPartie.remplir_entier()
        self.deckPartie.melange()

        # Création des 2 mains

        self.mainJoueur = Main(self.deckPartie)
        self.mainIA = Main(self.deckPartie)
        self.mainJoueur.creer_main()
        self.mainIA.creer_main()

        # Création de la pile du milieu

        self.pileMilieu = [Carte(randint(0,3), randint(0,9))]
        self.peutJouer = True
        self.nouvelle_couleur = ["", 0]

        # Démarrage de la Partie

        self.init_interface()
        self.lancer_partie()

    def init_interface(self):

        # Initialisation de la fenêtre (à retirer après les teste)

        self.fenetre = Tk()
        self.fenetre.title("Cosmunos")
        self.fenetre.geometry("1600x800")
        self.fenetre.attributes("-fullscreen", True)
        self.fond = "#1e1e1e"
        self.fenetre.config(bg=self.fond)

        # Initialisation des frames

        self.frame_cartes_mainIA = Frame(self.fenetre, bg=self.fond)
        self.frame_cartes_mainIA.pack(side=TOP, pady=20)
        self.frame_cartes_mainIA.lift()

        self.frame_cartes_joueur = Frame(self.fenetre, bg=self.fond)
        self.frame_cartes_joueur.pack(side=BOTTOM, pady=20)

        self.frame_milieu = Frame(self.fenetre, bg=self.fond) 
        self.frame_milieu.pack(anchor=CENTER)

        self.frame_fond = Frame(self.fenetre, bg=self.fond)
        self.frame_fond.place(relx=0.5, rely=0.5, anchor="center", width=1600, height=800)

        self.frame_changer_couleur = Frame(frame_fond, bg=self.fond)
        self.frame_changer_couleur.place(anchor="center", relx=0.5, rely=0.5, y=25)

        self.frame_ia = Frame(self.fenetre, bg=self.fond)
        self.frame_ia.place(relx=0.5, rely=0.3, anchor="center")

        self.frame_joueur = Frame(self.fenetre, bg=self.fond)
        self.frame_joueur.place(relx=0.5, rely=0.7, anchor="center")

        self.frame_victoire = Frame(self.fenetre, bg=self.fond)
        self.frame_victoire.place(relx=0.5, rely=0.5, anchor=CENTER,width=1600,height=800)

        self.frame_defaite = Frame(self.fenetre,bg=self.fond)
        self.frame_defaite.place(relx=0.5, rely=0.5, anchor=CENTER,width=1600,height=800)

        self.frame_couleur_cyan = Frame(self.fenetre, bg=self.fond)
        self.frame_couleur_bleu = Frame(self.fenetre, bg=self.fond)
        self.frame_couleur_violet = Frame(self.fenetre, bg=self.fond)
        self.frame_couleur_rose = Frame(self.fenetre, bg=self.fond)

        self.frame_score = Frame(self.fenetre,bg=self.fond)
        self.frame_victoire.place(relx=0.5, rely=0.5, anchor=CENTER,width=1600,height=800)

        self.frame_changer_couleur.lift()
        self.frame_cartes_joueur.lift()
        self.frame_cartes_mainIA.lift()

        # Charger les images requises
        
        self.image_dos_carte.charger_image("carte/autre/Dos.png",0.1)
        self.image_dos_carte_rotate.charger_image("carte/autre/Dos.png",0.1,180)

        self.fond_charger_couleur.charger_image("Interface/Changer de couleur/Interface.png",0.2)
        self.image_bleu.charger_image("Interface/Changer de couleur/Bleu.png",0.2)
        self.image_cyan.charger_image("Interface/Changer de couleur/Cyan.png",0.2)
        self.image_rose.charger_image("Interface/Changer de couleur/Rose.png",0.2)
        self.image_violet.charger_image("Interface/Changer de couleur/Violet.png",0.2)

        self.image_joueur.charger_image("Interface/Vous jouez.png",0.3)
        self.image_ia.charger_image("Interface/Le bot joue.png",0.3)

        self.image_victoire.charger_image("Interface/Victoire.png",0.2)
        self.image_defaite.charger_image("Interface/Defaite.png",0.2)

        # Element de l'interface

        self.pioche = Label(self.frame_milieu, image=self.image_dos_carte, padx=10, pady=5, bg=self.fond, borderwidth=0)
        self.pioche.grid(row=0, column=0, pady=100)
        
        self.label_fond = Label(self.frame_fond, image=self.fond_changer_couleur, bg=self.fond)
        self.label_fond.place(relx=0.5, rely=0.5, anchor=CENTER,width=1600,height=800)

        self.bouton_bleu = Button(self.frame_changer_couleur, image=self.image_bleu, bg=self.fond, command=lambda: afficher_index_couleur(2), borderwidth=0, activebackground="#121212").grid(row=0, column=0, padx=0)
        self.bouton_cyan = Button(self.frame_changer_couleur, image=self.image_cyan, bg=self.fond, command=lambda: afficher_index_couleur(3) ,borderwidth=0, activebackground="#121212").grid(row=0, column=1, padx=0)
        self.bouton_rose = Button(self.frame_changer_couleur, image=self.image_rose, bg=self.fond, command=lambda: afficher_index_couleur(1) ,borderwidth=0, activebackground="#121212").grid(row=0, column=2, padx=0)
        self.bouton_violet = Button(self.frame_changer_couleur, image=self.image_violet, bg=self.fond, command=lambda: afficher_index_couleur(0) ,borderwidth=0, activebackground="#121212").grid(row=0, column=3, padx=0)

        self.label_bleu = Label(self.frame_couleur_bleu, image=self.image_bleu, bg=self.fond)
        self.label_cyan = Label(self.frame_couleur_cyan, image=self.image_cyan, bg=self.fond)
        self.label_rose = Label(self.frame_couleur_rose, image=self.image_rose, bg=self.fond)
        self.label_violet = Label(self.frame_couleur_violet, image=self.image_violet, bg=self.fond)

        self.label_joueur = Label(self.frame_joueur, image=self.image_joueur, bg=self.fond)
        self.label_joueur.pack(anchor="center")

        self.label_ia = Label(self.frame_ia, image=self.image_ia, bg=self.fond)
        self.label_ia.pack(anchor="center")

    def charger_image(self,chemin,ratio=1,rotation=0):

        image_path = path.abspath(chemin)
        image = Image.open(image_path)
        image = image.resize((int(image.width * ratio), int(image.height * ratio)))
        image = image.rotate(rotation)
        image = ImageTk.PhotoImage(image)
        
        return image

        

