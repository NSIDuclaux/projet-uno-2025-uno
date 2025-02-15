from deck import *
from main_joueur import *
from tkinter import *
from PIL import Image, ImageTk
#from pygame import mixer
from os import *
import sqlite3
from main_joueur import Main
from deck import Deck
from carte_valide import *
from carte_effet import *
from bot import *
from time import sleep

# VarmainIAbles interface

image_cartes_joueur = []
image_cartes_milieu = []

# Jeu

deck_partie = Deck()
deck_partie.remplir_entier()
deck_partie.melange()
mainJoueur = Main(deck_partie)
mainIA = Main(deck_partie)
mainJoueur.creer_main()
mainIA.creer_main()
pile_milieu = []
sens_horaire = True
mainJoueurPeutJouer = True
mainIAPeutJouer = True
peut_jouer = True
nouvelle_couleur = ["", 0]
pile_milieu.append(deck_partie.retirer_carte())
mainJoueur.trier_mains()
mainIA.trier_mains()
score = [0,0]

#fonction pour les tours du joueur

def toursJoueur (mainJoueur,mainIA,peut_jouer, nouvelle_couleur,score):

    global numeroChoisie
    global pile_milieu
    valid = False
    valid1 = False
    tours_valide = False

    if peut_jouer is True:
        if nouvelle_couleur[1] == 1:
            t = nouvelle_couleur[0]

            for k in range(mainJoueur.nb_main()):
                if carte_valide2(t, mainJoueur.main_joueur[k]) == True:
                    valid1 = True

            if valid1 == True:
                while valid == False:
                    numeroChoisie.set(-1)  # Réinitialise avant de demander un choix
                    # Attends que l'utilisateur fasse un choix (via la variable)
                    frame_cartes_joueur.wait_variable(numeroChoisie)
                    numeroChoisie_value = numeroChoisie.get()

                    if int(numeroChoisie_value) >= 0 and int(numeroChoisie_value) < mainJoueur.nb_main():
                        valid = carte_valide2(t, mainJoueur.main_joueur[int(numeroChoisie_value)])

                carteChoisie = mainJoueur.choix_carte(int(numeroChoisie_value))
                tours_valide = True
                carte_placer = True
            else:
                mainJoueur.ajouter_carte(deck_partie.retirer_carte())
                print("Vous piochez")

                if carte_valide2(t, mainJoueur.main_joueur[-1]) == True:
                    carteChoisie = mainJoueur.choix_carte(-1)
                    tours_valide = True
                    print("Vous placez la carte piochée")
                    carte_placer = True

        else:
            # Gestion de la situation sans nouvelle couleur
            for k in range(mainJoueur.nb_main()):
                if carte_valide(pile_milieu[-1], mainJoueur.main_joueur[k]) == True:
                    valid1 = True

            if valid1 == True:
                while valid == False:
                    numeroChoisie.set(-1)  # Réinitialise avant de demander un choix
                    # Attends que l'utilisateur fasse un choix (via la variable)
                    frame_cartes_joueur.wait_variable(numeroChoisie)
                    numeroChoisie_value = numeroChoisie.get()

                    if int(numeroChoisie_value) >= 0 and int(numeroChoisie_value) < mainJoueur.nb_main():
                        valid = carte_valide(pile_milieu[-1], mainJoueur.main_joueur[int(numeroChoisie_value)])

                carteChoisie = mainJoueur.choix_carte(int(numeroChoisie_value))
                tours_valide = True
                carte_placer = True
            else:
                mainJoueur.ajouter_carte(deck_partie.retirer_carte())
                print("Vous piochez")
                if carte_valide(pile_milieu[-1], mainJoueur.main_joueur[-1]) == True:
                    carteChoisie = mainJoueur.choix_carte(-1)
                    print("Vous placez la carte piochée")
                    carte_placer = True

                else :  
                   carte_placer = False

            tours_valide = True
                

    peut_jouer = True
    nouvelle_couleur = ["", 0]

    if tours_valide == True:
        
        if carte_placer is True:
            print("La carte jouer est :",carteChoisie)
            pile_milieu.append(carteChoisie)
            deck_partie.ajouter_carte(carteChoisie)

            if carteChoisie.effet_carte() == 0 :
                score[0] = score[0] + 10
            if carteChoisie.effet_carte() == 1 :
                score[0] = score[0] * 1.5

            if carteChoisie.effet_carte() == 2 :
                peut_jouer = interdit_jouer()
                score[0] = score[0] + 10
            if carteChoisie.effet_carte() == 3:
                coef = 0
                score = plus_2_carte_bot(mainIA,mainJoueur,deck_partie,carteChoisie,pile_milieu,coef, score)

            if carteChoisie.effet_carte() == 4:
                coef = 0
                nouvelle_couleur, score = bot_plus_4_carte(mainIA,mainJoueur,deck_partie,carteChoisie,pile_milieu,coef, score)

            if carteChoisie.effet_carte() == 5 : 
                nouvelle_couleur = changer_couleur()
                score[0] = score[0] + 25
	
    return nouvelle_couleur, peut_jouer, score

def toursIA (mainIA,mainJoueur,peut_jouer, nouvelle_couleur,score): 

    global deck_partie
    global pile_milieu
    valid1 = False
    tours_valide = False
    if peut_jouer is True :
        if nouvelle_couleur[1] == 1:
            for k in range(mainIA.nb_main()):
                t = nouvelle_couleur[0]
                if carte_valide2(t, mainIA.main_joueur[k]) == True:
                    valid1 = True

            if valid1 == True:    
                carteChoisie = choix_complexe2(mainIA.main_joueur,mainJoueur.main_joueur, t)[0]
                mainIA.choix_carte(choix_complexe2(mainIA.main_joueur,mainJoueur.main_joueur, t)[1])
                tours_valide = True

            else:
                mainIA.ajouter_carte(deck_partie.retirer_carte())
                print("Le bot pioche")
                if carte_valide2(t, mainIA.main_joueur[-1]) == True:
                    carteChoisie = mainIA.choix_carte(-1)    
                    tours_valide = True
                    print("Le bot place la carte pioché")
        else:
            for k in range(mainIA.nb_main()):
                if carte_valide(pile_milieu[-1], mainIA.main_joueur[k]) == True:
                    valid1 = True

            if valid1 == True:    
                carteChoisie = choix_complexe(mainIA.main_joueur,mainJoueur.main_joueur, pile_milieu[-1])[0]
                mainIA.choix_carte(choix_complexe(mainIA.main_joueur,mainJoueur.main_joueur, pile_milieu[-1])[1])
                tours_valide = True

            else:
                mainIA.ajouter_carte(deck_partie.retirer_carte())
                print("Le bot pioche")
                if carte_valide(pile_milieu[-1], mainIA.main_joueur[-1]) == True:
                    carteChoisie = mainIA.choix_carte(-1)    
                    tours_valide = True
                    print("Le bot place la carte pioché")
                    
    peut_jouer = True
    nouvelle_couleur = ["", 0]

    if tours_valide == True:
        print("La carte jouer est :",carteChoisie)
        pile_milieu.append(carteChoisie)
        deck_partie.ajouter_carte(carteChoisie)

        if carteChoisie.effet_carte() == 0 :
            score[1] = score[1] + 10

        if carteChoisie.effet_carte() == 1 :
            score[1] = score[1] * 1.5

        if carteChoisie.effet_carte() == 2 :
            peut_jouer = interdit_jouer()
            score[1] = score[1] + 10

        if carteChoisie.effet_carte() == 3:
            coef = 0
            score = plus_2_carte(mainJoueur,mainIA,deck_partie,carteChoisie,pile_milieu,coef, score)

        if carteChoisie.effet_carte() == 4: 
            coef = 0
            nouvelle_couleur, score = plus_4_carte(mainJoueur,mainIA,deck_partie,carteChoisie,pile_milieu,coef, score)

        if carteChoisie.effet_carte() == 5 :
            nouvelle_couleur = bot_changer_couleur()
            score[1] = score[1] + 25

    return nouvelle_couleur, peut_jouer, score

# Création de la fenêtre

fenetre = Tk()
fenetre.title("Cosmunos")
fenetre.geometry("1600x800")
fenetre.attributes("-fullscreen",True)

index_carte = IntVar(value=-1)
numeroChoisie = IntVar(value=-1)

# Fond

fond = "#1e1e1e"
fenetre.config(bg=fond)

# Fonction pour mettre à jour l'affichage

def update_cartesmainIA():

    global mainIA
    global image_dos_carte_rotate

    for widget in frame_cartes_mainIA.winfo_children():
        widget.destroy()

    col = 0
    
    for i in range(mainIA.nb_main()):

        Label(frame_cartes_mainIA, image=image_dos_carte_rotate, padx=10, pady=5, bg=fond).grid(row=0, column=col, padx=0)
        col += 1

    fenetre.update()

def update_cartesJoueur():

    global mainJoueur
    global image_cartes_joueur
    global peut_jouer

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

        Button(
            frame_cartes_joueur, 
            image=image_carte, 
            padx=10, 
            pady=5, 
            bg=fond, 
            borderwidth=0, 
            activebackground="#1e1e1e",
            command=lambda idx=i: bouton_jouer_cartes(idx)
        ).grid(row=0, column=col, padx=0)

        col += 1

        fenetre.update()

def update_carteJouer():

    global pile_milieu
    global image_cartes_milieu

    for widget in frame_milieu.winfo_children():
        if widget.winfo_name() == "carte_milieu":
            widget.destroy()

    chemin = path.abspath(fichier_carte(pile_milieu[-1]))
    image_carte = Image.open(chemin)
    ratio = 0.1
    new_size = (int(image_carte.width * ratio), int(image_carte.height * ratio))
    image_carte = image_carte.resize(new_size)
    image_carte = ImageTk.PhotoImage(image_carte)
    image_cartes_milieu.append(image_carte)
    Label(frame_milieu, image=image_carte, padx=10, pady=5, bg=fond).grid(row=0, column=1, pady=90)

    fenetre.update()

def fichier_carte(carte):

    connexion = sqlite3.connect('carte/carte.db')
    c = connexion.cursor()

    c.execute("SELECT chemin FROM carte WHERE IDCouleur = ? AND IDCarte = ?", (carte.get_couleur(), carte.get_nombre()))
    chemin = c.fetchall()[0][0]

    return chemin


    frame_cartes_joueur.wait_variable(index_carte)
    choix = index_carte.get()
    print(f"Carte choisie : {choix}")
    return choix

#Action bouton

def bouton_jouer_cartes(index):

    global numeroChoisie
    numeroChoisie.set(index)  
    print(f"Carte choisie : {index}")

# def bouton_pioche(mains,deck):

# 	mains.ajouter_carte(deck.retirer_carte())

# Création des frames

frame_cartes_mainIA = Frame(fenetre, bg=fond)
frame_cartes_mainIA.pack(side=TOP, pady=20)

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

# Créer le bouton pioche

pioche = Button(frame_milieu, image=image_dos_carte, padx=10, pady=5, bg=fond, borderwidth=0, activebackground="#1e1e1e")
pioche.grid(row=0, column=0, pady=90)

# Mise à jour de l'interface

update_cartesmainIA()
update_carteJouer()
update_cartesJoueur()

# Partie

index_carte = IntVar()

vict = False

while vict is False :

    print("Tour du joueur")
    
    joueurAJouer = False
    mainJoueur.trier_mains()

    print(mainJoueur)
    nouvelle_couleur, peut_jouer, score = toursJoueur(mainJoueur,mainIA, peut_jouer, nouvelle_couleur,score)    

    update_cartesJoueur()
    update_carteJouer()

    sleep(1)

    print(str(pile_milieu))
    
    nouvelle_couleur, peut_jouer, score = toursIA(mainIA,mainJoueur, peut_jouer, nouvelle_couleur,score)

    update_cartesmainIA()
    update_carteJouer()

    print(str(pile_milieu))

    sleep(1)

    if mainJoueur.main_joueur == []:
        vict = True
    elif mainIA.main_joueur == []:
        vict = True

fenetre.mainloop()
