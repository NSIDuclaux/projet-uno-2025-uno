from deck import Deck
class Main :

    def __init__ (self, deck):

        self.deck = deck
        self.main_joueur = []

    def creer_main (self):

        for i in range (7):

            self.main_joueur.append(self.deck.retirer_carte())

        return self.main_joueur
    
    def choix_carte(self, num_carte):
        self.num_carte = num_carte
        self.main_joueur.pop(num_carte)

    def nb_main(self):
        lg_main = len(self.main_joueur)
        return lg_main
    
    def ajouter_carte(self,carte):

        self.main_joueur.append(carte)

    def __str__(self):

        return str(self.main_joueur)



# deck = Deck()
# deck.remplir_entier()
# deck.melange()
