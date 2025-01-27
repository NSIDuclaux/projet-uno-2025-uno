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
       
        return len(self.main_joueur)
    
    def ajouter_carte(self,carte):

        self.main_joueur.append(carte)

    def est_vide (self):

        if len(self.main_joueur) == 0:

            return True
        
        else :
            
            return False

    def __str__(self):

        self.affichage = []

        for i in range (len(self.main_joueur)):

            element = str(i+1) + " | " + str(self.main_joueur[i])
            self.affichage.append(str(element))

        return str(self.affichage)

main = Main(deck)
main.creer_main()
#print(main)
