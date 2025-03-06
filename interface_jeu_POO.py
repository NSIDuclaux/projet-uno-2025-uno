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

def fichier_carte(carte):

    connexion = sqlite3.connect('carte/carte.db')
    c = connexion.cursor()

    c.execute("SELECT chemin FROM carte WHERE IDCouleur = ? AND IDCarte = ?", (carte.get_couleur(), carte.get_nombre()))
    chemin = c.fetchall()[0][0]

    return chemin

class PartieJeu:

    def __init__(self):

        # Initialisation de la fenêtre (à retirer après les teste)

        self.fenetre = Tk()
        self.fenetre.title("Cosmunos")
        self.fenetre.geometry("1600x800")
        self.fenetre.attributes("-fullscreen", True)
        self.fond = "#1e1e1e"
        self.fenetre.config(bg=self.fond)

        # Création de la pioche
        
        self.deck_partie = Deck()
        self.deck_partie.remplir_entier()
        self.deck_partie.melange()

        # Création des 2 mains

        self.mainJoueur = Main(self.deck_partie)
        self.mainIA = Main(self.deck_partie)
        self.mainJoueur.creer_main()
        self.mainIA.creer_main()

        # Création de la pile du milieu

        self.pile_milieu = [Carte(randint(0,3), randint(0,9))]
        self.peut_jouer = True
        self.nouvelle_couleur = ["", 0]

        # Variable requise pour la partie interface

        self.index_carte = IntVar()
        self.index_couleur = IntVar()
        self.numeroChoisie = IntVar()
        self.score = 0

        self.vict = False
        self.confirmation = True

        self.image_cartes_joueur = []
        self.image_cartes_milieu = []

        # Démarrage de la Partie
        
        self.init_interface()
        self.partie()

    # Fonction Interface

    def init_interface(self):

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

        self.frame_changer_couleur = Frame(self.fenetre, bg=self.fond)
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
        
        self.image_dos_carte = self.charger_image("carte/autre/Dos.png",0.1)
        self.image_dos_carte_rotate = self.charger_image("carte/autre/Dos.png",0.1,180)

        self.fond_changer_couleur = self.charger_image("Interface/Changer de couleur/Interface.png",0.2)
        self.image_bleu = self.charger_image("Interface/Changer de couleur/Bleu.png",0.2)
        self.image_cyan = self.charger_image("Interface/Changer de couleur/Cyan.png",0.2)
        self.image_rose = self.charger_image("Interface/Changer de couleur/Rose.png",0.2)
        self.image_violet = self.charger_image("Interface/Changer de couleur/Violet.png",0.2)

        self.image_joueur = self.charger_image("Interface/Vous jouez.png",0.3)
        self.image_ia = self.charger_image("Interface/Le bot joue.png",0.3)

        self.image_victoire = self.charger_image("Interface/Victoire.png",0.2)
        self.image_defaite = self.charger_image("Interface/Defaite.png",0.2)

        # Element de l'interface

        self.pioche = Label(self.frame_milieu, image=self.image_dos_carte, padx=10, pady=5, bg=self.fond, borderwidth=0)
        self.pioche.grid(row=0, column=0, pady=100)
        
        self.label_fond = Label(self.frame_fond, image=self.fond_changer_couleur, bg=self.fond)
        self.label_fond.place(relx=0.5, rely=0.5, anchor=CENTER,width=1600,height=800)

        self.bouton_bleu = Button(self.frame_changer_couleur, image=self.image_bleu, bg="#121212", command=lambda: self.afficher_index_couleur(2), borderwidth=0, activebackground="#121212").grid(row=0, column=0, padx=0)
        self.bouton_cyan = Button(self.frame_changer_couleur, image=self.image_cyan, bg="#121212", command=lambda: self.afficher_index_couleur(3) ,borderwidth=0, activebackground="#121212").grid(row=0, column=1, padx=0)
        self.bouton_rose = Button(self.frame_changer_couleur, image=self.image_rose, bg="#121212", command=lambda: self.afficher_index_couleur(1) ,borderwidth=0, activebackground="#121212").grid(row=0, column=2, padx=0)
        self.bouton_violet = Button(self.frame_changer_couleur, image=self.image_violet, bg="#121212", command=lambda: self.afficher_index_couleur(0) ,borderwidth=0, activebackground="#121212").grid(row=0, column=3, padx=0)

        self.label_bleu = Label(self.frame_couleur_bleu, image=self.image_bleu, bg=self.fond)
        self.label_cyan = Label(self.frame_couleur_cyan, image=self.image_cyan, bg=self.fond)
        self.label_rose = Label(self.frame_couleur_rose, image=self.image_rose, bg=self.fond)
        self.label_violet = Label(self.frame_couleur_violet, image=self.image_violet, bg=self.fond)

        self.label_joueur = Label(self.frame_joueur, image=self.image_joueur, bg=self.fond)
        self.label_joueur.pack(anchor="center")

        self.label_ia = Label(self.frame_ia, image=self.image_ia, bg=self.fond)
        self.label_ia.pack(anchor="center")

        self.label_victoire = Label(self.frame_victoire,image=self.image_victoire,bg=self.fond)
        self.label_victoire.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.label_defaite = Label(self.frame_defaite,image=self.image_defaite,bg=self.fond)
        self.label_defaite.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.cacher_defaite()
        self.cacher_victoire()
        self.cacher_changer_couleur()
        self.cacher_joueur()
        self.cacher_ia()
        self.update_cartesmainIA()
        self.update_carteJouer()
        self.update_cartesJoueur()

    def charger_image(self,chemin,ratio=1,rotation=0):

        image_path = path.abspath(chemin)
        image = Image.open(image_path)
        image = image.resize((int(image.width * ratio), int(image.height * ratio)))
        image = image.rotate(rotation)
        image = ImageTk.PhotoImage(image)
        
        return image

    def update_cartesmainIA(self):

        self.mainIA.trier_mains()

        for widget in self.frame_cartes_mainIA.winfo_children():

            widget.destroy

        col = 0

        for i in range (self.mainIA.nb_main()):

            Label(self.frame_cartes_mainIA, image=self.image_dos_carte_rotate, padx=10, pady=5, bg=self.fond).grid(row=0, column=col, padx=0)
            col += 1

        self.fenetre.update()

    def update_cartesJoueur(self):

        self.mainJoueur.trier_mains()

        for widget in self.frame_cartes_joueur.winfo_children():

            widget.destroy()

        col = 0

        for i in range (self.mainJoueur.nb_main()):

            chemin = path.abspath(fichier_carte(self.mainJoueur.selection_carte(i)))
            self.image_carte = self.charger_image(chemin,0.1)
            self.image_cartes_joueur.append(self.image_carte)

            Button(
                self.frame_cartes_joueur, 
                image=self.image_carte, 
                padx=10, 
                pady=5, 
                bg=self.fond, 
                borderwidth=0, 
                activebackground="#1e1e1e",
                command=lambda idx=i: self.bouton_jouer_cartes(idx)
            ).grid(row=0, column=col, padx=0)

            col += 1

        self.fenetre.update()

    def update_carteJouer(self):

        for widget in self.frame_milieu.winfo_children():

            if widget.winfo_name() == "carte_milieu":
                widget.destroy()

        chemin = chemin = path.abspath(fichier_carte(self.pile_milieu[-1]))
        self.image_carte = self.charger_image(chemin,ratio=0.1)
        self.image_cartes_milieu.append(self.image_carte)

        Label(self.frame_milieu, image=self.image_carte, padx=10, pady=5, bg=self.fond).grid(row=0, column=1, pady=90)

        self.fenetre.update()

    def cacher_changer_couleur(self):

        self.frame_fond.place_forget()
        self.frame_changer_couleur.place_forget()

    def afficher_changer_couleur(self):

        self.frame_fond.place(relx=0.5, rely=0.5, anchor="center", width=1600, height=800)
        self.frame_changer_couleur.place(anchor="center", relx=0.5, rely=0.5, y=25)

    def cacher_joueur(self):

        self.frame_joueur.place_forget()

    def afficher_joueur(self):

        self.frame_joueur.place(relx=0.5, rely=0.7, anchor="center")

    def cacher_ia(self):

        self.frame_ia.place_forget()

    def afficher_ia(self):

        self.frame_ia.place(relx=0.5, rely=0.3, anchor="center")

    def afficher_victoire(self):

        self.frame_victoire.place(relx=0.5, rely=0.5, anchor=CENTER, width=1600, height=800)
        self.afficher_score(self.score)

    def afficher_defaite(self):

        self.frame_defaite.place(relx=0.5, rely=0.5, anchor=CENTER, width=1600, height=800)
        self.afficher_score(self.score)

    def cacher_victoire(self):
    
        self.frame_victoire.place_forget()
        self.frame_score.place_forget()

    def cacher_defaite(self):

        self.frame_defaite.place_forget()
        self.frame_score.place_forget()

    def afficher_score(self,score):
    
        self.frame_score.place(relx=0.5, rely=0.6, anchor=CENTER)  # Placé au-dessus des autres frames
        self.label_score = Label(self.frame_score, text="Votre Score : " + str(int(score)), font=("Questrian", 16, "bold"), fg="#8E086E", justify="center", bg="#121212")
        self.label_score.pack()

    def tout_cacher(self):

        self.frame_cartes_mainIA.pack_forget()
        self.frame_cartes_joueur.pack_forget()
        self.frame_milieu.pack_forget()
        self.frame_fond.place_forget()
        self.frame_changer_couleur.place_forget()
        self.frame_ia.place_forget()
        self.frame_joueur.place_forget()

    def cacher_nouvelle_couleur(self):

        self.frame_couleur_violet.place_forget()
        self.frame_couleur_rose.place_forget()
        self.frame_couleur_bleu.place_forget()
        self.frame_couleur_cyan.place_forget()

    # Action Bouton

    def bouton_jouer_cartes(self,index):

        self.numeroChoisie.set(index)

    def afficher_index_couleur(self,valeur) :
    
        self.index_couleur.set(valeur)
        self.cacher_changer_couleur()

    def afficher_nouvelle_couleur(self):

        pass

    # Fonction Partie

    def changer_couleur_interface(self):

        self.afficher_changer_couleur()

        self.nouvelle_couleur = ["", 1]
        self.frame_changer_couleur.wait_variable(self.index_couleur)

        self.nouvelle_couleur[0] = self.index_couleur.get()

        if self.nouvelle_couleur[0] == 0:

            self.nouvelle_couleur = ["violet", 1]

        if self.nouvelle_couleur[0] == 1:

            self.nouvelle_couleur = ["rose",1]

        if self.nouvelle_couleur[0] == 2:

            self.nouvelle_couleur = ["bleu",1]

        if self.nouvelle_couleur[0] == 3:

            self.nouvelle_couleur = ["cyan",1]

        self.cacher_changer_couleur()

    def plus_4_carte_interface(self,coef,carte):

        valide = False

        for k in range(self.mainJoueur.nb_main()):
            if renvoie_valide2(self.mainJoueur.main_joueur[k]) == True:
                valide = True
        if valide == True:
            valid = False
            while valid == False:

                self.numeroChoisie.set(-1)

                while int(self.numeroChoisie.get()) < 0 or int(self.numeroChoisie.get()) >= self.mainJoueur.nb_main():

                    
                    self.frame_cartes_joueur.wait_variable(self.numeroChoisie)
                    numeroChoisie_value = self.numeroChoisie.get()

                    if int(numeroChoisie_value) >= 0 and int(numeroChoisie_value) < self.mainJoueur.nb_main():
                        valid = renvoie_valide_plus2(self.mainJoueur.main_joueur[int(numeroChoisie_value)]) 
            carteChoisie = self.mainJoueur.choix_carte(int(numeroChoisie_value))
            print("La carte retourné est :",carteChoisie)
            self.pile_milieu.append(carteChoisie)
            self.deck_partie.ajouter_carte(carteChoisie)
            coef = coef + 4
            return self.bot_plus_4_carte_interface(coef,carte)
        else:
            coef = coef + 4
            for i in range (coef):

                self.mainJoueur.ajouter_carte(self.deck_partie.retirer_carte())

            self.nouvelle_couleur = self.bot_changer_couleur_interface()
            self.update_cartesJoueur()

            self.peut_jouer = False

            return coef

    def bot_plus_4_carte_interface (self,coef,carte):

        valide = False
        for k in range(self.mainIA.nb_main()):
            if renvoie_valide2(self.mainIA.main_joueur[k]) == True:
                valide = True
        if valide == True:
            print("Renvoie de carte")
            carteChoisie = renvoie_valide_plus(carte,self.mainIA)
            c = self.mainIA.main_joueur[carteChoisie]
            print("La carte retourné est :", c)
            self.pile_milieu.append(c)
            self.deck_partie.ajouter_carte(c)
            coef = coef + 4
            return self.plus_4_carte_interface(coef,carte)
        else:
            coef = coef + 4
            for i in range (coef):

                self.mainIA.ajouter_carte(self.deck_partie.retirer_carte())

            self.nouvelle_couleur = self.changer_couleur_interface()
            self.update_cartesmainIA()

            self.peut_jouer = False

            return coef
          
    def bot_changer_couleur_interface(self):

        x = randint(0,3)
        couleur = ["violet","rose","bleu","cyan"]
        

        self.nouvelle_couleur= [couleur[x], 1]

        print("La nouvelle couleur est",self.nouvelle_couleur)

        self.afficher_nouvelle_couleur()

    def plus_2_carte_interface (self,coef,carte):
        
        # Vérification de la possibilité de jouer

        valide = False
        for k in range(self.mainJoueur.nb_main()):
            if renvoie_valide2(self.mainJoueur.main_joueur[k]) == True:
                valide = True

        # Choix de la carte par le joueur

        if valide == True:

            valid = False

            while valid == False:
                
                self.numeroChoisie.set(-1)
            
                while int(self.numeroChoisie.get()) < 0 or int(self.numeroChoisie.get()) >= self.mainJoueur.nb_main():
                    self.frame_cartes_joueur.wait_variable(self.numeroChoisie)
                    numeroChoisie_value = self.numeroChoisie.get()
                    numeroChoisie_value = int(numeroChoisie_value)
                    if int(numeroChoisie_value) >= 0 and int(numeroChoisie_value) < self.mainJoueur.nb_main():
                        valid = renvoie_valide2(self.mainJoueur.main_joueur[int(self.numeroChoisie.get())]) 
            carteChoisie = self.mainJoueur.choix_carte(int(numeroChoisie_value))
            print("La carte retourné est :",carteChoisie)
            self.pile_milieu.append(carteChoisie)
            self.deck_partie.ajouter_carte(carteChoisie)
            if carteChoisie.nombre == 13:
                coef = coef + 4
                return self.bot_plus_4_carte_interface(coef,carte)

            else:
                coef = coef + 2
                return plus_2_carte_bot(self.mainIA,self.mainJoueur,self.deck_partie,carte,self.pile_milieu,coef)

        #  Si le joueur ne peut pas jouer

        else :

            coef = coef + 2
            for i in range (coef):

                self.mainJoueur.ajouter_carte(self.deck_partie.retirer_carte())

            self.peut_jouer = False

            return coef
    
    def plus_2_carte_bot_interface (self,coef,carte):

        global peut_jouer

        valide = False
        for k in range(self.mainIA.nb_main()):
            if renvoie_valide2(self.mainIA.main_joueur[k]) == True:
                valide = True
        if valide == True:
            print("Renvoie de carte")
            carteChoisie = renvoie_valide(carte,self.mainIA)
            c = self.mainIA.main_joueur[carteChoisie]
            print("La carte retourné est :", c)
            self.pile_milieu.append(c)
            self.deck_partie.ajouter_carte(c)
            if c.nombre == 13:
                coef = coef + 4
                return self.plus_4_carte_interface(carte,coef)
            else:
                coef = coef + 2
                return self.plus_2_carte_interface(coef,carte)
            
        else:
            coef = coef + 2
            for i in range (coef):

                self.mainIA.ajouter_carte(self.deck_partie.retirer_carte())
            print("Le joueur suivant reçoit "+ str(coef) +" carte")

            self.update_carteJouer()

            peut_jouer = False

            return coef
    
    def attente():
        pass

    # Fonction pour les tours

    def toursJoueur (self):

        valid = False
        valid1 = False
        tours_valide = False

        if self.peut_jouer is True:

            if self.nouvelle_couleur[1] == 1:
                t = self.nouvelle_couleur[0]

                for k in range(self.mainJoueur.nb_main()):
                    if carte_valide2(t, self.mainJoueur.main_joueur[k]) == True:
                        valid1 = True

                if valid1 == True:
                    while valid == False:
                        self.numeroChoisie.set(-1)  # Réinitialise avant de demander un choix
                        # Attends que l'utilisateur fasse un choix (via la variable)
                        self.frame_cartes_joueur.wait_variable(self.numeroChoisie)
                        numeroChoisie_value = self.numeroChoisie.get()

                        if int(numeroChoisie_value) >= 0 and int(numeroChoisie_value) < self.mainJoueur.nb_main():
                            valid = carte_valide2(t, self.mainJoueur.main_joueur[int(numeroChoisie_value)])

                    carteChoisie = self.mainJoueur.choix_carte(int(numeroChoisie_value))
                    tours_valide = True
                    carte_placer = True
                else:
                    self.mainJoueur.ajouter_carte(self.deck_partie.retirer_carte())
                    print("Vous piochez")

                    if carte_valide2(t, self.mainJoueur.main_joueur[-1]) == True:
                        carteChoisie = self.mainJoueur.choix_carte(-1)
                        tours_valide = True
                        print("Vous placez la carte piochée")
                        carte_placer = True

                self.cacher_nouvelle_couleur()

            else:
                # Gestion de la situation sans nouvelle couleur
                for k in range(self.mainJoueur.nb_main()):
                    if carte_valide(self.pile_milieu[-1], self.mainJoueur.main_joueur[k]) == True:
                        valid1 = True

                if valid1 == True:
                    while valid == False:
                        self.numeroChoisie.set(-1)  # Réinitialise avant de demander un choix
                        # Attends que l'utilisateur fasse un choix (via la variable)
                        self.frame_cartes_joueur.wait_variable(self.numeroChoisie)
                        numeroChoisie_value = self.numeroChoisie.get()

                        if int(numeroChoisie_value) >= 0 and int(numeroChoisie_value) < self.mainJoueur.nb_main():
                            valid = carte_valide(self.pile_milieu[-1], self.mainJoueur.main_joueur[int(numeroChoisie_value)])

                    carteChoisie = self.mainJoueur.choix_carte(int(numeroChoisie_value))
                    tours_valide = True
                    carte_placer = True
                else:
                    self.mainJoueur.ajouter_carte(self.deck_partie.retirer_carte())
                    print("Vous piochez")
                    if carte_valide(self.pile_milieu[-1], self.mainJoueur.main_joueur[-1]) == True:
                        carteChoisie = self.mainJoueur.choix_carte(-1)
                        print("Vous placez la carte piochée")
                        carte_placer = True

                    else :  
                        carte_placer = False

                tours_valide = True
                

        self.peut_jouer = True
        self.nouvelle_couleur = ["", 0]

        if tours_valide == True:
            
            if carte_placer is True:
                
                self.pile_milieu.append(carteChoisie)
                self.deck_partie.ajouter_carte(carteChoisie)

                if carteChoisie.effet_carte() == 0 :

                    self.score = self.score + 10

                if carteChoisie.effet_carte() == 1 :

                    inverse(self.mainJoueur, self.mainIA)
                    self.update_cartesJoueur()
                    self.update_cartesmainIA()
                    self.score = float(self.score) + float(self.score) * 1.5

                if carteChoisie.effet_carte() == 2 :
                    self.peut_jouer = interdit_jouer()
                    self.score = self.score + 10

                if carteChoisie.effet_carte() == 3:

                    coef = 0
                    coef = self.plus_2_carte_bot_interface(coef,carteChoisie)
                    self.score = float(self.score) + float(self.score) * 1.25

                if carteChoisie.effet_carte() == 4:

                    coef = 0
                    coef = self.bot_plus_4_carte_interface(coef,carteChoisie)
                    self.score = float(self.score) + self.score * 1.75

                if carteChoisie.effet_carte() == 5 : 

                    self.changer_couleur_interface() 
                    self.score = self.score + 25

    def toursIA(self):

        valid1 = False
        tours_valide = False
        
        if self.peut_jouer:

            self.afficher_ia()
            
            if self.nouvelle_couleur[1] == 1:

                for k in range(self.mainIA.nb_main()):
                    t = self.nouvelle_couleur[0]

                
                    if carte_valide2(t, self.mainIA.main_joueur[k]) == True:
                        valid1 = True
                
                if valid1:
                    carteChoisie = choix_complexe2(self.mainIA.main_joueur,self.mainJoueur.main_joueur, t)[0]
                    self.mainIA.choix_carte(choix_complexe2(self.mainIA.main_joueur,self.mainJoueur.main_joueur, t)[1])
                    tours_valide = True

                else:
                    self.mainIA.ajouter_carte(self.deck_partie.retirer_carte())
                    print("Le bot pioche")
                    if carte_valide2(t, self.mainIA.main_joueur[-1]):
                        carteChoisie = self.mainIA.choix_carte(-1)
                        tours_valide = True
                        print("Le bot place la carte piochée")
                
                self.cacher_nouvelle_couleur()
            
            else:
                for k in range(self.mainIA.nb_main()):
                    if carte_valide(self.pile_milieu[-1], self.mainIA.main_joueur[k]) == True:
                        valid1 = True
                
                if valid1:
                    carteChoisie = choix_complexe(self.mainIA.main_joueur,self.mainJoueur.main_joueur, self.pile_milieu[-1])[0]
                    self.mainIA.choix_carte(choix_complexe(self.mainIA.main_joueur,self.mainJoueur.main_joueur, self.pile_milieu[-1])[1])
                    tours_valide = True

                else:
                    self.mainIA.ajouter_carte(self.deck_partie.retirer_carte())
                    print("Le bot pioche")
                    if carte_valide(self.pile_milieu[-1], self.mainIA.main_joueur[-1]):
                        carteChoisie = self.mainIA.choix_carte(-1)
                        tours_valide = True
                        print("Le bot place la carte piochée")
        
        self.peut_jouer = True
        self.nouvelle_couleur = ["", 0]
        
        if tours_valide:
            print("La carte jouée est :", carteChoisie)
            self.pile_milieu.append(carteChoisie)
            self.deck_partie.ajouter_carte(carteChoisie)
            
            effet = carteChoisie.effet_carte()
            print(effet)

            if effet == 1:

                inverse(self.mainJoueur, self.mainIA)
                self.update_cartesJoueur()
                self.update_cartesmainIA()

            elif effet == 2:

                self.peut_jouer = interdit_jouer()

            elif effet == 3:

                coef = 0
                coef = self.plus_2_carte_bot_interface(coef,carteChoisie)

            elif effet == 4:
                
                coef = 0
                coef = self.plus_4_carte_interface(coef,carteChoisie)
            
            elif effet == 5:
                
                self.bot_changer_couleur_interface()
        
        self.cacher_ia()
    
    def partie(self):

        while not self.vict:

            print(self.peut_jouer)
            self.update_carteJouer()
            print("Tour du joueur")
            
            self.mainJoueur.trier_mains()
            self.mainIA.trier_mains()
            self.afficher_joueur()
            print(self.mainJoueur)
            
            self.toursJoueur()
            print(self.mainJoueur)

            if self.peut_jouer:  # Vérifie que le joueur a bien joué avant de laisser l'IA jouer
                self.fenetre.after(1000, self.attente)
            
            self.mainJoueur.trier_mains()
            self.mainIA.trier_mains()
            
            self.cacher_joueur()
            self.update_cartesJoueur()
            self.update_carteJouer()
            
            if not self.mainJoueur.main_joueur:
                self.tout_cacher()
                self.afficher_victoire()
                self.vict = True
                self.confirmation = False
            
            self.update_carteJouer()
            self.fenetre.after(1000, self.attente)
            
            print("L'IA joue")
            print(self.mainIA)
            self.toursIA()
            self.mainJoueur.trier_mains()
            
            print(self.mainIA)
            self.update_cartesmainIA()
            self.update_carteJouer()
            
            if not self.mainIA.main_joueur and self.confirmation:
                self.tout_cacher()
                self.vict = True
                self.afficher_defaite()
            
            self.update_cartesmainIA()
            self.update_carteJouer()
        
        self.fenetre.mainloop()

partie = PartieJeu()