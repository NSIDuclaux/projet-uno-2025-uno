from main_joueur import Main
from deck import Deck
from Pile import Pile
from carte_valide import carte_valide
from carte_effet import *

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

#Fonction partie

def tours (joueur1,joueur2,peut_jouer): #joueur1 -> Joue #joueur2 -> ne joue pas

	global deck_partie
	global pile_milieu
	valid = False

	if peut_jouer is True :

		while valid == False:
					
			numeroChoisie = 0

			while numeroChoisie < 0 or numeroChoisie > player.nb_main():
				
				numeroChoisie = int(input("Choissez une carte"))	
				valid = carte_valide(player.main_joueur[numeroChoisie],pile_milieu[0])
					
			carteChoisie = player.choix_carte(int(numeroChoisie))
			print("La carte jouer est :",carteChoisie)
			pile_milieu.append(carteChoisie)
			deck_partie.ajouter_carte(carteChoisie)

			if carteChoisie.effet() == 1 :

				resultat = inverse(sens_horaire)

			if carteChoisie.effet() == 2 :

				resultat = interdit_jouer ()

			if carteChoisie.effet() == 3:

				plus_2_carte(ia,deck_partie)

			if carteChoisie.effet() == 4:

				resultat = plus_4_carte(ia,deck_partie)

			if carteChoisie.effet() == 5 :

				resultat = changer_couleur(ia,deck_partie)
			
			return resultat


#Début Partie

while reponse != "oui" or reponse != "non":

	reponse = str(input("Voulez-vous commencer une partie ? | Oui/Non")).lower()

	if reponse == "oui":

		while player.main_joueur  or ia.main_joueur:

			pile_milieu.append(deck_partie.retirer_carte())
			print(player)
			print("La carte du milieu est :" , pile_milieu[0])

			if sens_horaire is True:

				tours(player,ia,playerPeutJouer)
				tours(ia,player,iaPeutJouer)

			else :

				tours(ia,player,iaPeutJouer)
				tours(player,ia,playerPeutJouer)
		
			if player.main_joueur == []:
			
				print("Victoire du joueur !!!!!")
			
			else:
			
				print("Victoire de l'IA (T'es mauvais :-) )")

	if reponse == "non" :

		break

#aaa