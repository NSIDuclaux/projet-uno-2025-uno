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



        

