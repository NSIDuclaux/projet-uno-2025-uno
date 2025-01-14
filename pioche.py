from random import shuffle
from deck import d 
class Pioche():
    def __init__(self, liste):
        self.liste = liste

    def mélanger(self):
        self.liste = shuffle(self.liste)

    def __str__(self):
        return str(self.liste)
p = Pioche(d)
p.mélanger()
print(p)