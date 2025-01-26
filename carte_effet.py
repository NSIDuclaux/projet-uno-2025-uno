class EffetCarte :

    def __init__ (self,carte,main,deck,sensHoraire,pouvoirJouer):

        self.carte = carte
        self.main = main
        self.deck = deck
        self.sensHoraire = sensHoraire
        self.pouvoirJouer = pouvoirJouer

    def inverse (self):

        if self.sens_horaire == True:

            self.sens_horaire = False

        else :

            self.sens_horaire = True

        return self.sens_horaire

    def interdit_jouer (self):

        self.pouvoirJouer = False

        return self.pouvoirJouer

    def plus_2_carte (self):

        for i in range (2):

            self.main.ajouter_carte(self.deck.retirer_carte())


    def changer_couleur(self):

        nouvelleCouleur = ""

        while nouvelleCouleur != "jaune" or nouvelleCouleur != "rouge" or nouvelleCouleur != "bleu" or nouvelleCouleur != "vert":
            nouvelleCouleur = str(input("Choissez une nouvelle couleur")).lower()

    def plus_4_carte (self):

        for i in range (4):

            self.main.ajouter_carte(self.deck.retirer_carte())

        nouvelleCouleur = ""

        while nouvelleCouleur != "jaune" or nouvelleCouleur != "rouge" or nouvelleCouleur != "bleu" or nouvelleCouleur != "vert":
            
            nouvelleCouleur = str(input("Choissez une nouvelle couleur")).lower()



