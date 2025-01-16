from random import randint
from deck import Deck
class Main :

    def __init__ (self, deck, main = []):
        self.deck = deck
        self.main = main

    def main (deck):
        main =[]
        for i in range(7):
            i = randint(108)
            nb = Deck[i]
            main.append(nb)
            Deck.remove(i)

        
    def __str__(self):

        return str(self.main())

    def retirer (num,main):
        main.remove(num)

deck = Deck
#main = 
#print(main)