from main_joueur import Main
from deck import Deck

D_partie = Deck()
D_partie.remplir_entier()
D_partie.melange()
Player = Main(D_partie)
Player.main()
Ia = Main

