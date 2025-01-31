from main_joueur import Main
from deck import Deck
from carte_valide import *
from carte_effet import *
from bot import *
#Fonction

def toursjoueur (player,ia,peut_jouer, nouvelle_couleur): #joueur1 -> Joue #joueur2 -> ne joue pas

	global deck_partie
	global pile_milieu
	valid = False
	valid1 = False
	arghhh = False
	if peut_jouer is True :
		if nouvelle_couleur[1] == 1:
			for k in range(player.nb_main()):
				if carte_valide2(nouvelle_couleur[0], player.main_joueur[k]) == True:
					valid1 = True

			if valid1 == True:	
				while valid == False:
				
					numeroChoisie = -1
      
					while int(numeroChoisie) < 0 or int(numeroChoisie) >= player.nb_main():
				
						numeroChoisie = input("Choissez une carte")	
						valid = carte_valide2(nouvelle_couleur[0],player.main_joueur[int(numeroChoisie)])
				carteChoisie = player.choix_carte(int(numeroChoisie))
				arghhh = True
			else:
				player.ajouter_carte(deck_partie.retirer_carte())
				if carte_valide(nouvelle_couleur[0], player.main_joueur[-1]) == True:
					carteChoisie = player.choix_carte(-1)	
					arghhh = True
		else:
			for k in range(player.nb_main()):
				if carte_valide(pile_milieu[-1], player.main_joueur[k]) == True:
					valid1 = True

			if valid1 == True:	
				while valid == False:
				
					numeroChoisie = -1
      
					while int(numeroChoisie) < 0 or int(numeroChoisie) >= player.nb_main():
				
						numeroChoisie = input("Choissez une carte")	
						valid = carte_valide(pile_milieu[-1], player.main_joueur[int(numeroChoisie)])
				carteChoisie = player.choix_carte(int(numeroChoisie))
				arghhh = True
			else:
				player.ajouter_carte(deck_partie.retirer_carte())
				if carte_valide(pile_milieu[-1], player.main_joueur[-1]) == True:
					carteChoisie = player.choix_carte(-1)	
					arghhh = True
		
		nouvelle_couleur = ["", 0]
		#resultat = 0	
		if arghhh == True:
			print("La carte jouer est :",carteChoisie)
			pile_milieu.append(carteChoisie)
			deck_partie.ajouter_carte(carteChoisie)

			if carteChoisie.effet_carte() == 0 :
				
				#resultat = 
				0

			if carteChoisie.effet_carte() == 1 :

				#resultat = 
				inverse(sens_horaire)

			if carteChoisie.effet_carte() == 2 :

				#resultat = 
				interdit_jouer ()

			if carteChoisie.effet_carte() == 3:

				#resultat = 
				plus_2_carte(ia,deck_partie)

			if carteChoisie.effet_carte() == 4:

				#resultat = 
				nouvelle_couleur = plus_4_carte(ia,deck_partie)

			if carteChoisie.effet_carte() == 5 :

				#resultat = 
				nouvelle_couleur = changer_couleur()
	peut_jouer = True
	return nouvelle_couleur
	

def toursia (ia,player,peut_jouer, nouvelle_couleur): #joueur1 -> Joue #joueur2 -> ne joue pas

	global deck_partie
	global pile_milieu
	valid1 = False
	arghhh = False
	if peut_jouer is True :
		if nouvelle_couleur[1] == 1:
			for k in range(ia.nb_main()):
				if carte_valide2(nouvelle_couleur[0], ia.main_joueur[k]) == True:
					valid1 = True

			if valid1 == True:	
				carteChoisie = choix_complexe2(ia.main_joueur,player.main_joueur, nouvelle_couleur)[0]
				ia.choix_carte(choix_complexe2(ia.main_joueur,player.main_joueur, nouvelle_couleur)[1])
				arghhh = True
			else:
				ia.ajouter_carte(deck_partie.retirer_carte())
				if carte_valide2(nouvelle_couleur, ia.main_joueur[-1]) == True:
					carteChoisie = ia.choix_carte(-1)	
					arghhh = True
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
				if carte_valide(pile_milieu[-1], ia.main_joueur[-1]) == True:
					carteChoisie = ia.choix_carte(-1)	
					arghhh = True
		#resultat = 0	
		nouvelle_couleur = ["",0]
		if arghhh == True:
			print("La carte jouer est :",carteChoisie)
			pile_milieu.append(carteChoisie)
			deck_partie.ajouter_carte(carteChoisie)

			if carteChoisie.effet_carte() == 0 :
				
				#resultat = 
				0

			if carteChoisie.effet_carte() == 1 :

				#resultat = 
				inverse(sens_horaire)

			if carteChoisie.effet_carte() == 2 :

				#resultat = 
				interdit_jouer ()

			if carteChoisie.effet_carte() == 3:

				plus_2_carte(player,deck_partie)

			if carteChoisie.effet_carte() == 4:

				#resultat = 
				nouvelle_couleur = bot_plus_4_carte(player, deck_partie)

			if carteChoisie.effet_carte() == 5 :

				#resultat = 
				nouvelle_couleur = bot_changer_couleur()
	peut_jouer = True	
	return nouvelle_couleur


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
nouvelle_couleur = ["", 0]
pile_milieu.append(deck_partie.retirer_carte())
#Début Partie
vict = False
while reponse != "oui" or reponse != "non":

	reponse = str(input("Voulez-vous commencer une partie ? | Oui/Non")).lower()

	if reponse == "oui":

		while vict == False:
			print("bot :", ia)
			print("joueur :", player)
            
			print("La carte du milieu est :" , pile_milieu[-1])

			if sens_horaire is True:

				nouvelle_couleur = toursjoueur(player,ia, playerPeutJouer, nouvelle_couleur)
				nouvelle_couleur = toursia(ia,player, iaPeutJouer, nouvelle_couleur)

			else :

				nouvelle_couleur = toursjoueur(ia,player,iaPeutJouer, nouvelle_couleur)
				nouvelle_couleur = toursia(player,ia,playerPeutJouer, nouvelle_couleur)
			
			if player.main_joueur == []:
				vict = True
				print("Victoire du joueur !!!!!")
			    
			elif ia.main_joueur == []:
				vict = True
				print("Victoire de l'IA (T'es mauvais :-) )")
                
	if reponse == "non" :

		break

## ANCIEN CODE
#
# while Player.main_joueur != [] or Ia.main_joueur:
#   	carte_place.empiler(D_partie.retirer_carte())
#   	print(Player)
#   	valid = False
#   	while valid == False:
#     	while numero < 0 or numero > Player.nb_carte():
#     	    numero = input("Choisir Carte")
#     	valid = carte_valide(Player.main_joueur[numero], carte_place.sommet())
# 	cc = Player.choix_carte(int(numero))
# 	print(cc)
# 	carte_place.empiler(cc)
# 	#placer effet Player
# 	numeral = ProgIa.jouer(Ia.main_joueur)
# 	ccc = Ia.choix_carte(int(numero))
# 	print(ccc)
# 	#Placer effet Ia
# 	if Player.main_joueur == []:
# 	print("Victoire du joueur !!!!!")
# 	else:
# 	print("Victoire de l'IA (T'es mauvais :-) )")