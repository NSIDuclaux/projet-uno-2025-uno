from main_joueur import Main
from deck import Deck
from carte_valide import *
from carte_effet import *
from bot import *

def toursjoueur (player,ia,peut_jouer, nouvelle_couleur):

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
			inverse(sens_horaire)

		if carteChoisie.effet_carte() == 2 :
			peut_jouer = interdit_jouer()

		if carteChoisie.effet_carte() == 3:
			plus_2_carte(ia,deck_partie)

		if carteChoisie.effet_carte() == 4:
			nouvelle_couleur = plus_4_carte(ia,deck_partie)

		if carteChoisie.effet_carte() == 5 : 
			nouvelle_couleur = changer_couleur()
	
	return nouvelle_couleur, peut_jouer
	

def toursia (ia,player,peut_jouer, nouvelle_couleur): 

	global deck_partie
	global pile_milieu
	valid1 = False
	arghhh = False
	if peut_jouer is True :
		if nouvelle_couleur[1] == 1:
			for k in range(ia.nb_main()):
				t = nouvelle_couleur[0]
				if carte_valide2(t, ia.main_joueur[k]) == True:
					valid1 = True

			if valid1 == True:	
				carteChoisie = choix_complexe2(ia.main_joueur,player.main_joueur, t)[0]
				ia.choix_carte(choix_complexe2(ia.main_joueur,player.main_joueur, t)[1])
				arghhh = True

			else:
				ia.ajouter_carte(deck_partie.retirer_carte())
				print("Le bot pioche")
				if carte_valide2(t, ia.main_joueur[-1]) == True:
					carteChoisie = ia.choix_carte(-1)	
					arghhh = True
					print("Le bot place la carte pioché")
		else:
			for k in range(ia.nb_main()):
				if carte_valide(pile_milieu[-1], ia.main_joueur[k]) == True:
					valid1 = True

			if valid1 == True:	
				carteChoisie = choix_complexe(ia.main_joueur,player.main_joueur, pile_milieu[-1])[0]
				ia.choix_carte(choix_complexe(ia.main_joueur,player.main_joueur, pile_milieu[-1])[1])
				arghhh = True

			else:
				ia.ajouter_carte(deck_partie.retirer_carte())
				print("Le bot pioche")
				if carte_valide(pile_milieu[-1], ia.main_joueur[-1]) == True:
					carteChoisie = ia.choix_carte(-1)	
					arghhh = True
					print("Le bot place la carte pioché")

	peut_jouer = True
	nouvelle_couleur = ["",0]

	if arghhh == True:
		print("La carte jouer est :",carteChoisie)
		pile_milieu.append(carteChoisie)
		deck_partie.ajouter_carte(carteChoisie)

		if carteChoisie.effet_carte() == 0 :
			0

		if carteChoisie.effet_carte() == 1 :
			inverse(sens_horaire)

		if carteChoisie.effet_carte() == 2 :
			peut_jouer = interdit_jouer()

		if carteChoisie.effet_carte() == 3:
			plus_2_carte(player,deck_partie)

		if carteChoisie.effet_carte() == 4: 
			nouvelle_couleur = bot_plus_4_carte(player, deck_partie)

		if carteChoisie.effet_carte() == 5 :
			nouvelle_couleur = bot_changer_couleur()	
	return nouvelle_couleur, peut_jouer


#Initialisation de la partie

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
#Début Partie
vict = False
while reponse != "oui" or reponse != "non":

	reponse = str(input("Voulez-vous commencer une partie ? | Oui/Non")).lower()

	if reponse == "oui":
		while vict == False:
			#print("bot :", ia)
			print("joueur :", player)
            
			print("La carte du milieu est :" , pile_milieu[-1])

			if sens_horaire is True:

				nouvelle_couleur, peut_jouer = toursjoueur(player,ia, peut_jouer, nouvelle_couleur)
				nouvelle_couleur, peut_jouer = toursia(ia,player, peut_jouer, nouvelle_couleur)

			else :

				nouvelle_couleur, peut_jouer = toursia(ia,player,peut_jouer, nouvelle_couleur)
				nouvelle_couleur, peut_jouer = toursjoueur(player,ia,peut_jouer, nouvelle_couleur)
			
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