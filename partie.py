from main_joueur import Main
from deck import Deck
from Pile import Pile

D_partie = Deck()
D_partie.remplir_entier()
D_partie.melange()
Player = Main(D_partie)
Ia = Main(D_partie)
Player.main()
Ia.main()
reponse = ""

while reponse == "":
  reponse = input("Start")

carte_place = Pile()

while Player.main_joueur != [] or Ia.main_joueur:
  print(Player)
  while numero < 0 or numero > Player.nb_carte():
    numero = input("Choisir Carte")
  carte_place.empiler(Player.choixcarte(int(numero)))
  