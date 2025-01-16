from deck import Deck
class Main :

    def __init__ (self, deck):

        self.deck = list(deck)
        self.main_joueur = []

    def main (self):

        for i in range (7):

            self.main_joueur.append(self.deck[0])
            self.deck.remove(0)

        return self.main_joueur()

    def __str__(self):

        return str(self.main())



deck = Deck()
deck.remplir_entier()
deck.melange()

main = Main(deck)
main.main()
#main = 
#print(main)