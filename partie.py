from main_joueur import Main
from deck import Deck
from Pile import Pile

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
  print(Player)
  while numero < 0 or numero > Player.nb_carte():
    numero = input("Choisir Carte")
  cc = Player.choix_carte(int(numero))
  print(cc)
  carte_place.empiler(cc)
  numeral = ProgIa.jouer(Ia.main_joueur)
  ccc = Ia.choix_carte(int(numero))
  print(ccc)
if Player.main_joueur == []:
  print("Victoire du joueur !!!!!")
else:
  print("Victoire de l'IA (T'es mauvais :-) )")