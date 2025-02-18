from deck import *
from main_joueur import *
from tkinter import *
from PIL import Image, ImageTk
#from pygame import mixer
from os import *
import sqlite3
from main_joueur import Main
from carte_valide import *
from carte_effet import *
from bot import *
from time import sleep
from random import randint

# Varmainiables interface

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
score = 0

#fonction pour les tours du joueur

def toursJoueur (mainJoueur,mainIA,peut_jouer, nouvelle_couleur,score):

    global numeroChoisie
    global pile_milieu
    valid = False
    valid1 = False
    tours_valide = False

    if peut_jouer is True:
        print(nouvelle_couleur)
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
            

            pile_milieu.append(carteChoisie)
            deck_partie.ajouter_carte(carteChoisie)

            if carteChoisie.effet_carte() == 0 :

                score = score + 10

            if carteChoisie.effet_carte() == 1 :

                mainJoueur,mainIA = mainIA,mainJoueur
                score = float(score) + float(score) * 1.5

            if carteChoisie.effet_carte() == 2 :
                peut_jouer = interdit_jouer()
                score = score + 10

            if carteChoisie.effet_carte() == 3:

                coef = 0
                coef = plus_2_carte_bot(mainIA,mainJoueur,deck_partie,carteChoisie,pile_milieu,coef)
                score = float(score) + float(score) * 1.25

            if carteChoisie.effet_carte() == 4:

                coef = 0
                nouvelle_couleur, coef = plus_4_carte_interface(mainIA,mainJoueur,deck_partie,carteChoisie,pile_milieu,coef)
                score = float(score) + score * 1.75

            if carteChoisie.effet_carte() == 5 : 

                nouvelle_couleur = changer_couleur_interface() 
                score = score + 25
	
    return nouvelle_couleur, peut_jouer, score

def toursIA (mainIA,mainJoueur,peut_jouer, nouvelle_couleur): 

    global deck_partie
    global pile_milieu
    valid1 = False
    tours_valide = False

    if peut_jouer is True :
        
        afficher_ia()

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

        if carteChoisie.effet_carte() == 1 :
            mainJoueur,mainIA = mainIA,mainJoueur

        if carteChoisie.effet_carte() == 2 :

            peut_jouer = interdit_jouer()
  

        if carteChoisie.effet_carte() == 3:

            coef = 0
            coef = plus_2_carte_bot(mainJoueur,mainIA,deck_partie,carteChoisie,pile_milieu,coef)
            
        if carteChoisie.effet_carte() == 4: 

            coef = 0
            nouvelle_couleur = bot_plus_4_carte_interface(mainJoueur,mainIA,deck_partie,carteChoisie,pile_milieu,coef)

        if carteChoisie.effet_carte() == 5 :

            nouvelle_couleur = bot_changer_couleur_interface()

    cacher_ia()

    return nouvelle_couleur, peut_jouer

def changer_couleur_interface():

    global index_couleur

    afficher_changer_couleur()
    nouvelleCouleur = ["", 1]
    frame_changer_couleur.wait_variable(index_couleur)
    nouvelleCouleur[0] = index_couleur.get()
    print("La nouvelle couleur est",nouvelleCouleur[0])
    cacher_changer_couleur()

    return nouvelleCouleur

def plus_4_carte_interface (main,bot,deck,carte,pile_milieu,coef):

    global numeroChoisie
    update_carteJouer()

    valide = False
    for k in range(main.nb_main()):
        if renvoie_valide_plus2(main.main_joueur[k]) == True:
            valide = True
    if valide == True:
        valid = False
        while valid == False:
            numeroChoisie.set(-1)
            while int(numeroChoisie) < 0 or int(numeroChoisie) >= main.nb_main():
                frame_cartes_joueur.wait_variable(numeroChoisie)
                numeroChoisie_value = numeroChoisie.get()
                if int(numeroChoisie_value) >= 0 and int(numeroChoisie_value) < main.nb_main():
                    valid = renvoie_valide_plus2(main.main_joueur[int(numeroChoisie_value)]) 
        carteChoisie = main.choix_carte(int(numeroChoisie_value))
        print("La carte retourné est :",carteChoisie)
        pile_milieu.append(carteChoisie)
        deck.ajouter_carte(carteChoisie)
        coef = coef + 4
        bot_plus_4_carte_interface(bot,main,deck,carte,pile_milieu,coef)

    else:
        coef = coef + 4
        for i in range (coef):

            main.ajouter_carte(deck.retirer_carte())

        nouvelle_couleur = changer_couleur_interface()

        return nouvelle_couleur, coef
    
def bot_plus_4_carte_interface (bot,main,deck,carte,pile_milieu,coef):
    valide = False
    for k in range(bot.nb_main()):
        if renvoie_valide_plus2(bot.main_joueur[k]) == True:
            valide = True
    if valide == True:
        print("Renvoie de carte")
        carteChoisie = renvoie_valide_plus(carte,bot)
        c = bot.main_joueur[carteChoisie]
        print("La carte retourné est :", c)
        pile_milieu.append(c)
        deck.ajouter_carte(c)
        coef = coef + 4
        plus_4_carte_interface(main,bot,deck,carte,pile_milieu,coef)
    else:
        coef = coef + 4
        for i in range (coef):

            bot.ajouter_carte(deck.retirer_carte())

        nouvelleCouleur = bot_changer_couleur_interface()

        return nouvelleCouleur, c

def bot_changer_couleur_interface():

    c = randint(0,3)
    nouvelleCouleur= [c, 1]

    print("La nouvelle couleur est",nouvelleCouleur[0])

    return nouvelleCouleur

def plus_2_carte (main,bot,deck,carte,pile_milieu,coef):

    global numeroChoisie
    
    # Vérification de la possibilité de jouer

    valide = False
    for k in range(main.nb_main()):
        if renvoie_valide2(main.main_joueur[k]) == True:
            valide = True

    # Choix de la carte par le joueur

    if valide == True:

        valid = False

        while valid == False:
            
            numeroChoisie.set(-1)
            while int(numeroChoisie) < 0 or int(numeroChoisie) >= main.nb_main():
                frame_cartes_joueur.wait_variable(numeroChoisie)
                numeroChoisie_value = numeroChoisie.get()
                if int(numeroChoisie_value) >= 0 and int(numeroChoisie_value) < main.nb_main():
                    valid = renvoie_valide2(main.main_joueur[int(numeroChoisie)]) 
        carteChoisie = main.choix_carte(int(numeroChoisie_value))
        print("La carte retourné est :",carteChoisie)
        pile_milieu.append(carteChoisie)
        deck.ajouter_carte(carteChoisie)
        if carteChoisie.nombre == 13:
            coef = coef + 4
            bot_plus_4_carte(bot,main,deck,carte,pile_milieu,coef)

        else:
            coef = coef + 2
            plus_2_carte_bot(bot,main,deck,carte,pile_milieu,coef)

    #  Si le joueur ne peut pas jouer

    else :

        coef = coef + 2
        for i in range (coef):

            main.ajouter_carte(deck.retirer_carte())

    return coef

# Création de la fenêtre

fenetre = Tk()
fenetre.title("Cosmunos")
fenetre.geometry("1600x800")
fenetre.attributes("-fullscreen",True)

index_carte = IntVar(value=-1)
numeroChoisie = IntVar(value=-1)
index_couleur = IntVar(value=-1)

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

def cacher_changer_couleur():

    frame_fond.place_forget()
    frame_changer_couleur.place_forget()

def afficher_changer_couleur():

    frame_fond.place(relx=0.5, rely=0.5, anchor="center", width=1600, height=800)
    frame_changer_couleur.place(anchor="center", relx=0.5, rely=0.5, y=25)
    
def cacher_joueur():

    frame_joueur.place_forget()

def afficher_joueur():

    frame_joueur.place(relx=0.5, rely=0.7, anchor="center")

def cacher_ia():

    frame_ia.place_forget()

def afficher_ia():

    frame_ia.place(relx=0.5, rely=0.3, anchor="center")

def afficher_victoire():

    frame_victoire.place(relx=0.5, rely=0.5, anchor=CENTER,width=1600,height=800)

def afficher_defaite():

    frame_defaite.place(relx=0.5, rely=0.5, anchor=CENTER,width=1600,height=800)

def cacher_victoire():
    
    frame_victoire.place_forget()

def cacher_defaite():

    frame_defaite.place_forget()

def tout_cacher():

    frame_cartes_mainIA.pack_forget()
    frame_cartes_joueur.pack_forget()
    frame_milieu.pack_forget()
    frame_fond.place_forget()
    frame_changer_couleur.place_forget()
    frame_ia.place_forget()
    frame_joueur.place_forget()

#Action bouton

def bouton_jouer_cartes(index):

    global numeroChoisie
    numeroChoisie.set(index)  
    print(f"Carte choisie : {index}")

def afficher_index_couleur(valeur) :

    index_couleur.set(valeur)
    print("Index couleur :", index_couleur.get())
    cacher_changer_couleur()

# def bouton_pioche(mains,deck):

# 	mains.ajouter_carte(deck.retirer_carte())

# Création des frames

frame_cartes_mainIA = Frame(fenetre, bg=fond)
frame_cartes_mainIA.pack(side=TOP, pady=20)
frame_cartes_mainIA.lift()

frame_cartes_joueur = Frame(fenetre, bg=fond)
frame_cartes_joueur.pack(side=BOTTOM, pady=20)

frame_milieu = Frame(fenetre, bg=fond) 
frame_milieu.pack(anchor=CENTER)

frame_fond = Frame(fenetre, bg=fond)
frame_fond.place(relx=0.5, rely=0.5, anchor="center", width=1600, height=800)

frame_changer_couleur = Frame(frame_fond, bg=fond)
frame_changer_couleur.place(anchor="center", relx=0.5, rely=0.5, y=25)

frame_ia = Frame(fenetre, bg=fond)
frame_ia.place(relx=0.5, rely=0.3, anchor="center")

frame_joueur = Frame(fenetre, bg=fond)
frame_joueur.place(relx=0.5, rely=0.7, anchor="center")

frame_victoire = Frame(fenetre, bg=fond)
frame_victoire.place(relx=0.5, rely=0.5, anchor=CENTER,width=1600,height=800)

frame_defaite = Frame(fenetre,bg=fond)
frame_victoire.place(relx=0.5, rely=0.5, anchor=CENTER,width=1600,height=800)

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
pioche.grid(row=0, column=0, pady=100)

# Créer image de fond et de changement de couleur

ratio = 0.2

fond_path = path.abspath("Interface/Changer de couleur/Interface.png")
fond_changer_couleur = Image.open(fond_path)
new_size = (int(fond_changer_couleur.width * ratio), int(fond_changer_couleur.height * ratio))
fond_changer_couleur = fond_changer_couleur.resize(new_size)
fond_changer_couleur = ImageTk.PhotoImage(fond_changer_couleur)

image_bleu = Image.open(path.abspath("Interface/Changer de couleur/Bleu.png"))

new_size = (int(image_bleu.width * ratio), int(image_bleu.height * ratio))

image_bleu = image_bleu.resize(new_size)
image_bleu = ImageTk.PhotoImage(image_bleu)

image_cyan = Image.open(path.abspath("Interface/Changer de couleur/Cyan.png"))
image_cyan = image_cyan.resize(new_size)
image_cyan = ImageTk.PhotoImage(image_cyan)

image_rose = Image.open(path.abspath("Interface/Changer de couleur/Rose.png"))
image_rose = image_rose.resize(new_size)
image_rose = ImageTk.PhotoImage(image_rose)

image_violet = Image.open(path.abspath("Interface/Changer de couleur/Violet.png"))
image_violet = image_violet.resize(new_size)
image_violet = ImageTk.PhotoImage(image_violet)

image_joueur = Image.open(path.abspath("Interface/Vous jouez.png"))
image_joueur = image_joueur.resize((int(image_joueur.width * 0.3), int(image_joueur.height * 0.3)))
image_joueur = ImageTk.PhotoImage(image_joueur)

image_ia = Image.open(path.abspath("Interface/Le bot joue.png"))
image_ia = image_ia.resize((int(image_ia.width * 0.3), int(image_ia.height * 0.3)))
image_ia = ImageTk.PhotoImage(image_ia)

ratio = 0.2

image_victoire = Image.open(path.abspath("Interface/Victoire.png"))
new_size = (int(image_victoire.width * ratio), int(image_victoire.height * ratio))
image_victoire = image_victoire.resize(new_size)
image_victoire = ImageTk.PhotoImage(image_victoire)

image_defaite = Image.open(path.abspath("Interface/Defaite.png"))
image_defaite = image_defaite.resize(new_size)
image_defaite = ImageTk.PhotoImage(image_defaite)

##Label & Bouton

label_fond = Label(frame_fond, image=fond_changer_couleur, bg=fond)
label_fond.place(relx=0.5, rely=0.5, anchor=CENTER,width=1600,height=800)

bouton_bleu = Button(frame_changer_couleur, image=image_bleu, bg="#121212", command=lambda: afficher_index_couleur(2), borderwidth=0, activebackground="#121212").grid(row=0, column=0, padx=0)
bouton_cyan = Button(frame_changer_couleur, image=image_cyan, bg="#121212", command=lambda: afficher_index_couleur(3) ,borderwidth=0, activebackground="#121212").grid(row=0, column=1, padx=0)
bouton_rose = Button(frame_changer_couleur, image=image_rose, bg="#121212", command=lambda: afficher_index_couleur(1) ,borderwidth=0, activebackground="#121212").grid(row=0, column=2, padx=0)
bouton_violet = Button(frame_changer_couleur, image=image_violet, bg="#121212", command=lambda: afficher_index_couleur(0) ,borderwidth=0, activebackground="#121212").grid(row=0, column=3, padx=0)



label_joueur = Label(frame_joueur, image=image_joueur, bg=fond)
label_joueur.pack(anchor="center")

label_ia = Label(frame_ia, image=image_ia, bg=fond)
label_ia.pack(anchor="center")

label_victoire = Label(frame_victoire,image=image_victoire,bg=fond)
label_victoire.place(relx=0.5, rely=0.5, anchor=CENTER)
label_defaite = Label(frame_defaite,image=image_defaite,bg=fond)
label_defaite.place(relx=0.5, rely=0.5, anchor=CENTER)

frame_changer_couleur.lift()
frame_cartes_joueur.lift()
frame_cartes_mainIA.lift()

# Mise à jour de l'interface

cacher_defaite()
cacher_victoire()
cacher_changer_couleur()
cacher_joueur()
cacher_ia()
update_cartesmainIA()
update_carteJouer()
update_cartesJoueur()

# Partie

index_carte = IntVar()

vict = False
confimation = True

while vict is False :


    update_carteJouer()

    print("Tour du joueur")
    
    joueurAJouer = False
    mainJoueur.trier_mains()

    afficher_joueur()

    print(mainJoueur)
    nouvelle_couleur, peut_jouer, score = toursJoueur(mainJoueur,mainIA, peut_jouer, nouvelle_couleur,score)    
    print(mainJoueur)

    mainJoueur.trier_mains()
    
    cacher_joueur()
    update_cartesJoueur()
    update_carteJouer()

    if mainJoueur.main_joueur == []:
        tout_cacher()
        afficher_victoire()
        vict = True
        confimation = False

    sleep(2)

    print(mainIA)
    
    nouvelle_couleur, peut_jouer = toursIA(mainIA,mainJoueur, peut_jouer, nouvelle_couleur)
    mainJoueur.trier_mains()

    print(mainIA)

    update_cartesmainIA()
    update_carteJouer()

    sleep(1)

    if mainIA.main_joueur == [] and confimation is True:
        tout_cacher()
        vict = True
        afficher_defaite()

fenetre.mainloop()