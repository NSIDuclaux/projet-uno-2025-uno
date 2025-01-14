from random import randint
class Main :

    def __init__ (self, deck):
        self.deck = deck

    def main (deck):
        nb = 0
        main = []
        for i in range(7):
            i = randint(108)
            nb = deck[i]
            main.append(nb)
            deck.remove(i)

        
    def __str__(self):
        return main


