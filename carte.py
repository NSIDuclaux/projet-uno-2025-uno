class Carte:
    
    def __init__(self,couleur,nombre):

        #0 = Jaune  #0 #1 #2 #3 #4 #5 #6 #7 #8 #9 
        #1 = Rouge  #Sans inverse = 10 #Passer son tour = 11 # +2 = 12
        #2 = Bleu   #+4 13, #changer de couleur = 14
        #3 = Vert
        #4 = Noir
        
        self.couleur = couleur
        self.nombre = nombre

    def typeCarte (self):

        if 0 <= self.nombre <= 9 :

            return self.nombre

        elif self.nombre == 10:

            return "Sens Inverse"

        elif self.nombre == 11:

            return "Interdit de jouer"

        elif self.nombre == 12:

            return "+2 Cartes"

        elif self.nombre == 13:

            return ("+4 Cartes", "")

        elif self.nombre == 14:

            return ("Changez de Couleur", "")

    def structuration(self):

        if type(self.typeCarte) == str :
        
            if self.couleur == 0:

                self.couleur = "Jaune"

            elif self.couleur == 1:

                self.couleur = "Rouge"

            elif self.couleur == 2:

                self.couleur = "Bleu"

            elif self.couleur == 3:

                self.couleur = "Vert"

            return str(self.typeCarte + self.couleur)

        else :

            return str(self.typeCarte[0])
    
    def getcouleur(self):

        return (self.couleur)

    def getnombre(self):
        
        return (self.nombre)

    def __str__ (self):

        return self.structuration()

carte = Carte(0,5)
print(carte)