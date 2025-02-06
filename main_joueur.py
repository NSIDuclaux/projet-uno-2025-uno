from deck import Deck
# from Trie import *

class Main :

    def __init__ (self, deck):

        self.deck = deck
        self.main_joueur = []

    def creer_main (self):

        for i in range (7):

            self.main_joueur.append(self.deck.retirer_carte())

        return self.main_joueur
    
    def choix_carte(self, num_carte):
        #self.num_carte = num_carte
        return self.main_joueur.pop(num_carte)

    def nb_main(self):
        return len(self.main_joueur)
    
    def ajouter_carte(self,carte):

        self.main_joueur.append(carte)

    def trier_mains(self):

        cartes_violet = []
        cartes_rose = []
        cartes_bleu = []
        cartes_cyan = []

        for carte in self.main_joueur:
            
            print(carte.get_couleur())

            if carte.get_couleur() == "violet":

                cartes_violet.append(carte)

            elif carte.get_couleur() == "rose":

                cartes_rose.append(carte)

            elif carte.get_couleur() == "bleu":

                cartes_bleu.append(carte)
            
            elif carte.get_couleur() == "cyan":

                cartes_cyan.append(carte)


            print(carte.get_nombre())

        print(cartes_violet,cartes_rose,cartes_bleu,cartes_cyan)

    def __str__(self):
        
        self.affichage = []
        
        for carte in self.main_joueur:

            self.affichage.append(str(carte))

        return str(self.affichage)

deck = Deck()
deck.remplir_entier()
deck.melange()

mains = Main(deck)
mains.creer_main()
print(mains)
mains.trier_mains()
