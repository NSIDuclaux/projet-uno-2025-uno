from main_joueur import Main
from deck import Deck
from Pile import Pile
from cartevalide import carte_valide
from bot import jouer_carte
D_partie = Deck()
D_partie.remplir_entier()
D_partie.melange()
Player = Main(D_partie)
Ia = Main(D_partie)
Player.creer_main()
Ia.creer_main()

p = input("Start")

carte_place = Pile()
carte_place.empiler(D_partie.retirer_carte())
while Player.main_joueur != [] or Ia.main_joueur:
  print(carte_place.sommet())
  print(Player)
  valid = False
  while valid == False:
    numero = -1
    while numero < 0 or numero > Player.nb_carte():
        numero = input("Choisir Carte")
    valid = carte_valide(Player.main_joueur[numero], carte_place.sommet())
  carte_place.empiler(Player.choix_carte(int(numero)))
  print(carte_place.sommet())
  carte_place.empiler(carte_place.sommet())
  #placer effet Player
  numeral = jouer_carte(Ia.main_joueur, carte_place.sommet())
  carte_place.empiler(Ia.choix_carte(int(numero)))
  print(carte_place.sommet())
  #Placer effet Ia
if Player.main_joueur == []:
  print("Victoire du joueur !!!!!")
else:
  print("Victoire de l'IA (T'es mauvais :-) )")