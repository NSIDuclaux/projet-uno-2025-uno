from deck import Deck
from Trie import *

class Main :

    def __init__ (self, deck):

        self.deck = deck
        self.main_joueur = []

    def creer_main (self):

        for i in range (7):

            self.main_joueur.append(self.deck.retirer_carte())

        return self.main_joueur
    
    def choix_carte(self, num_carte):

        return self.main_joueur.pop(num_carte)
    
    def selection_carte(self,index):

        return self.main_joueur[index]

    def nb_main(self):
        return len(self.main_joueur)
    
    def ajouter_carte(self,carte):

        self.main_joueur.append(carte)

    def trier_mains(self):

        cartes_violet = []
        cartes_rose = []
        cartes_bleu = []
        cartes_cyan = []
        cartes_noir = []

        for carte in self.main_joueur:

            if carte.get_couleur() == 0:

                cartes_violet.append(carte)

            elif carte.get_couleur() == 1:

                cartes_rose.append(carte)

            elif carte.get_couleur() == 2:

                cartes_bleu.append(carte)
            
            elif carte.get_couleur() == 3:

                cartes_cyan.append(carte)

            elif carte.get_couleur() == 4:

                cartes_noir.append(carte)

        tableau_cartes = [cartes_violet,cartes_rose,cartes_bleu,cartes_cyan,cartes_noir]
        tableau_cartes_trie = []

        for tab in tableau_cartes:
            
            tableau_cartes_trie.append(tri_selection(tab))

        nouvelle_main = []

        for i in range (5):

            for carte in tableau_cartes_trie[i]:

                nouvelle_main.append(carte)

        self.main_joueur = nouvelle_main

    def __str__(self):
        
        self.affichage = []
        compteur = -1
        
        for carte in self.main_joueur:
            
            compteur += 1
            self.affichage.append(str(compteur) + " | " + str(carte))

        return str(self.affichage)

# deck = Deck()
# deck.remplir_entier()
# deck.melange()

# mains = Main(deck)
# mains.creer_main()
# print(mains)
# mains.trier_mains()
# print(mains)
