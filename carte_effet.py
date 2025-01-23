class EffetCarte :

    def __init__ (self,carte,main,deck):

        self.carte = carte
        self.main = main
        self.deck = deck

    def inverse (self):

        

    def interdit_jouer (self):

        return False

    def plus_2_carte (self):

        for i in range (2):

            self.main.ajouter_carte(self.deck.retirer_carte())


    def changer_couleur(self):

        pass

    def plus_4_carte (self):

        #utilisé changé de couleur + 

        for i in range (4):

            self.main.ajouter_carte(self.deck.retirer_carte())

