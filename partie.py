from main_joueur import Main
from deck import Deck
from Pile import Pile
from cartevalide import carte_valide

#Initialisation de la partie

deck_partie = Deck()
deck_partie.remplir_entier()
deck_partie.melange()
player = Main(deck_partie)
ia = Main(deck_partie)
player.creer_main()
ia.creer_main()
reponse = ""

#Début Partie

while reponse != "oui" or reponse != "non":

	reponse = str(input("Voulez-vous commencer une partie ? | Oui/Non")).lower()

	if reponse == "oui":

		while player.main_joueur != [] or ia.main_joueur:

			carte_place.empiler(deck_partie.retirer_carte())
			print(player)
			valid = False
			while valid == False:
			
				while numero < 0 or numero > player.nb_carte():
			
					numero = input("Choisir Carte")
			
				valid = carte_valide(player.main_joueur[numero], carte_place.sommet())
				
			cc = player.choix_carte(int(numero))
			
			print(cc)
			carte_place.empiler(cc)
			#placer effet Player
			numeral = ia.jouer(ia.main_joueur)
			ccc = ia.choix_carte(int(numero))
			print(ccc)
			#Placer effet Ia
			
			if player.main_joueur == []:
			
				print("Victoire du joueur !!!!!")
			
			else:
			
				print("Victoire de l'IA (T'es mauvais :-) )")

	else :

		print("Au revoir")


carte_place = Pile()

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