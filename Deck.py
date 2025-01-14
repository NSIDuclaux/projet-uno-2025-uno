from carte import Carte
class Deck:
    def __init__(self, n_carte=108, list_allc = []):
        self.n_carte = n_carte
        self.list_allc = list_allc

    def __str__(self):
        return str(self.list_allc)

    def remplir_entier(self):
        for c in range(4):
            for n in range(9):
                self.list_allc = self.list_allc + [Carte(c,n+1)]
        for c in range(4):
            self.list_allc = self.list_allc + [Carte(c,0)]
        for c in range(4):
            for k in range(2):
                self.list_allc = self.list_allc + [Carte(c,12)]
        for c in range(4):
            for k in range(2):
                self.list_allc = self.list_allc + [Carte(c,10)]
        for c in range(4):
            for k in range(2):
                self.list_allc = self.list_allc + [Carte(c,11)]
        for k in range(4):
            self.list_allc = self.list_allc + [Carte(4,14)]
        for k in range(4):
            self.list_allc = self.list_allc + [Carte(4,13)]
        
d = Deck()
d.remplir_entier()
print(d)