from deck import *
from main_joueur import *
from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
from os import *
import sqlite3
from main_joueur import Main
from deck import Deck
from carte_valide import *
from carte_effet import *
from bot import *
from time import sleep

# Variables interface

image_cartes_joueur = []
image_cartes_milieu = []

# Jeu

deck_partie = Deck()
deck_partie.remplir_entier()
deck_partie.melange()
player = Main(deck_partie)
ia = Main(deck_partie)
player.creer_main()
ia.creer_main()
reponse = ""
pile_milieu = []
sens_horaire = True
playerPeutJouer = True
iaPeutJouer = True
peut_jouer = True
nouvelle_couleur = ["", 0]
pile_milieu.append(deck_partie.retirer_carte())
player.trier_mains()
ia.trier_mains()

#fonction pour les tours du joueur

def toursjoueur (player,ia,peut_jouer, nouvelle_couleur, sens_horaire):

	global deck_partie
	global pile_milieu
	valid = False
	valid1 = False
	arghhh = False

	if peut_jouer is True :
		if nouvelle_couleur[1] == 1:
			t = nouvelle_couleur[0]
			for k in range(player.nb_main()):
				if carte_valide2(t, player.main_joueur[k]) == True:
					valid1 = True

			if valid1 == True:
				while valid == False:
					numeroChoisie = -1
      
					while int(numeroChoisie) < 0 or int(numeroChoisie) >= player.nb_main():
						numeroChoisie = input("Choissez une carte")
						
						if int(numeroChoisie) >= 0 and int(numeroChoisie) < player.nb_main():
							valid = carte_valide2(t,player.main_joueur[int(numeroChoisie)])

				carteChoisie = player.choix_carte(int(numeroChoisie))
				arghhh = True

			else:
				player.ajouter_carte(deck_partie.retirer_carte())
				print("Vous piochez")

				if carte_valide2(t, player.main_joueur[-1]) == True:
					carteChoisie = player.choix_carte(-1)	
					arghhh = True
					print("Vous placez la carte pioché")

		else:
			for k in range(player.nb_main()):
				if carte_valide(pile_milieu[-1], player.main_joueur[k]) == True:
					valid1 = True

			if valid1 == True:	
				while valid == False:
				
					numeroChoisie = -1
      
					while int(numeroChoisie) < 0 or int(numeroChoisie) >= player.nb_main():
						numeroChoisie = input("Choissez une carte")	
						if int(numeroChoisie) >= 0 and int(numeroChoisie) < player.nb_main():
							valid = carte_valide(pile_milieu[-1], player.main_joueur[int(numeroChoisie)])

				carteChoisie = player.choix_carte(int(numeroChoisie))
				arghhh = True

			else:
				player.ajouter_carte(deck_partie.retirer_carte())
				print("Vous piochez")
				if carte_valide(pile_milieu[-1], player.main_joueur[-1]) == True:
					carteChoisie = player.choix_carte(-1)	
					arghhh = True
					print("Vous placez la carte pioché")

	peut_jouer = True
	nouvelle_couleur = ["", 0]
		
	if arghhh == True:
		print("La carte jouer est :",carteChoisie)
		pile_milieu.append(carteChoisie)
		deck_partie.ajouter_carte(carteChoisie)

		if carteChoisie.effet_carte() == 1 :
			sens_horaire = inverse(sens_horaire)

		if carteChoisie.effet_carte() == 2 :
			peut_jouer = interdit_jouer()

		if carteChoisie.effet_carte() == 3:
			coef = 0
			c = plus_2_carte_bot(ia,deck_partie,carteChoisie,pile_milieu,coef)
			if c == int:
				plus_2_carte(player,deck_partie,carteChoisie,pile_milieu,c)

		if carteChoisie.effet_carte() == 4:
			nouvelle_couleur = plus_4_carte(ia,deck_partie)

		if carteChoisie.effet_carte() == 5 : 
			nouvelle_couleur = changer_couleur()
	
	return nouvelle_couleur, peut_jouer, sens_horaire
	

def toursia (ia,player,peut_jouer, nouvelle_couleur, sens_horaire): 

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

def update_carteJouer():

    global pile_milieu
    global image_cartes_milieu

    for widget in frame_milieu.winfo_children():
        if widget.winfo_name() == "carte_milieu":
            widget.destroy()

    chemin = path.abspath(fichier_carte(pile_milieu[0]))
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
pioche.grid(row=0, column=0, pady=90)

# Mettre à jour l'affichage des cartes
update_cartesIA()
update_cartesJoueur()
update_carteJouer()

# Partie

vict = False

while reponse != "oui" or reponse != "non":

	reponse = str(input("Voulez-vous commencer une partie ? | Oui/Non")).lower()

	if reponse == "oui":
		while vict == False:
			
			print("joueur :", player)
            
			print("La carte du milieu est :" , pile_milieu[-1])
                  

			if sens_horaire is True:

				nouvelle_couleur, peut_jouer, sens_horaire = toursjoueur(player,ia, peut_jouer, nouvelle_couleur, sens_horaire)
				nouvelle_couleur, peut_jouer, sens_horaire = toursia(ia,player, peut_jouer, nouvelle_couleur, sens_horaire)

			else :

				nouvelle_couleur, peut_jouer, sens_horaire = toursia(ia,player,peut_jouer, nouvelle_couleur, sens_horaire)
				nouvelle_couleur, peut_jouer, sens_horaire = toursjoueur(player,ia,peut_jouer, nouvelle_couleur, sens_horaire)
			
			if player.main_joueur == []:
				vict = True
				print("Victoire du joueur !!!!!")
				break

			elif ia.main_joueur == []:
				vict = True
				print("Victoire de l'IA (T'es mauvais :-) )")
				break
                  
           
		
	if reponse == "non" :

		break



fenetre.mainloop()
