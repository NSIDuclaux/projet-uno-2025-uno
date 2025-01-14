from random import randint
class Main :

    def __init__ (self, Deck):
        
        self.Deck = Deck

    def main (Deck):

        nb = 0
        main = []
        for i in range(7):
            i = randint(108)
            nb = Deck[i]
            main.append(nb)
            Deck.remove(i)

        
    def __str__(self):

        return self.main()

    def retirer (num,main):
        main.remove(num)
