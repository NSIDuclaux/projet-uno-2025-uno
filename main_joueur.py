from deck import Deck

class Main :

    def __init__ (self, deck, main = []):
        self.deck = deck
        self.main = main

    def main (deck):

        for carte in deck:

            print(carte)

        # for i in range(7):

        #     main.append(nb)
        #     Deck.remove(i)

        
    def __str__(self):

        return str(self.main())

    def retirer (num,main):
        main.remove(num)

deck = Deck
deck.remplir_entier()
deck.melange()
main = Main()
#print(main)