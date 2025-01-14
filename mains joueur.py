from random import randint
from deck import Deck
class Main :

    def __init__ (self, Deck):
        self.Deck = Deck

    def main (Deck):

        nb = 0
        main = []
        for i in range(7):
            main.append(Deck[0])
            Deck.remove(Deck[0])
        return main
        
    def __str__(self):

        return str(self.main())

    def retirer (num,main):
        main.remove(num)

main = Main(Deck)
print(main)