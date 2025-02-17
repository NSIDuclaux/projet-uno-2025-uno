from carte import Carte
from random import shuffle

class Deck:
    def __init__(self, n_carte=108, list_allc = []):
        self.n_carte = n_carte
        self.list_allc = list_allc

    def remplir_entier(self):

        for i in range(2):

            for c in range(4):
            
                for n in range(9):
                    self.list_allc = self.list_allc + [Carte(c,n+1)]
        for c in range(4):
            for n in range(2):
                self.list_allc = self.list_allc + [Carte(c,0)]
        for c in range(4):
            
            for k in range(2):
                self.list_allc = self.list_allc + [Carte(c,12)]
        for c in range(4):
            
            for k in range(10):
                self.list_allc = self.list_allc + [Carte(c,10)]
        for c in range(4):
            
            for k in range(2):
                self.list_allc = self.list_allc + [Carte(c,11)]
        for k in range(0):
            self.list_allc = self.list_allc + [Carte(4,14)]
        for k in range(0):
            self.list_allc = self.list_allc + [Carte(4,13)]

    def melange(self):

        shuffle(self.list_allc)

    def retirer_carte(self):

        return self.list_allc.pop(0)

    def ajouter_carte(self, carte):

        self.list_allc.append(carte)

    def choix_carte(self, id):

        return self.list_allc[id]
        
        
    def __str__(self):

        self.affichage = []

        for i in range (len(self.list_allc)):

            element =  str(self.list_allc[i]) + " | " 
            print(element)
            self.affichage.append(str(element))

        return str(self.affichage)
        
#d = Deck()
#d.remplir_entier()
#d.melange()
#print(d.retirer_carte())
#print(d)
#carte = d.choix_carte(2)
#print(carte)
#print(carte.get_couleur())

