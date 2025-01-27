from main_joueur import Main
from deck import Deck
from Pile import Pile
from carte_valide import carte_valide

D_partie = Deck()
D_partie.remplir_entier()
D_partie.melange()
Player = Main(D_partie)
Ia = Main(D_partie)
Player.creer_main()
Ia.creer_main()
reponse = ""

while reponse == "":
  reponse = input("Start")

carte_place = Pile()

while Player.main_joueur != [] or Ia.main_joueur:
  carte_place.empiler(D_partie.retirer_carte())
  print(carte_place.sommet())
  print(Player)
  valid = False
  while valid == False:
    while numero < 0 or numero > Player.nb_carte():
        numero = input("Choisir Carte")
    valid = carte_valide(Player.main_joueur[numero], carte_place.sommet())
  carte_place.empiler(Player.main_joueur[numero])
  
  carte_place.empiler(cc)
  #placer effet Player
  numeral = ProgIa.jouer(Ia.main_joueur)
  ccc = Ia.choix_carte(int(numero))
  print(ccc)
  #Placer effet Ia
if Player.main_joueur == []:
  print("Victoire du joueur !!!!!")
else:
  print("Victoire de l'IA (T'es mauvais :-) )")