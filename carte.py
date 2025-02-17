class Carte:
    
    def __init__(self,couleur,nombre):

        #0 = Violet  #0 #1 #2 #3 #4 #5 #6 #7 #8 #9 
        #1 = Rose  #Sans inverse = 10 #Passer son tour = 11 # +2 = 12
        #2 = Bleu   #+4 13, #changer de couleur = 14
        #3 = Cyan
        #4 = Noir
        
        self.couleur = couleur
        self.nombre = nombre

    def type_carte (self):

        if 0 <= self.nombre <= 9 :

            return self.nombre

        if self.nombre == 10:

            return "Sens Inverse"

        if self.nombre == 11:

            return "Interdit de jouer"

        if self.nombre == 12:

            return "+2 Cartes"

        if self.nombre == 13:

            return ("+4 Cartes")

        if self.nombre == 14:

            return ("Changez de Couleur")

    def structuration(self):

        if type(self.type_carte()) == int or 10 <= self.nombre <= 12:
        
            if self.couleur == 0:

                self.newcouleur = "violet"

            elif self.couleur == 1:

                self.newcouleur = "rose"

            elif self.couleur == 2:

                self.newcouleur = "bleu"

            elif self.couleur == 3:

                self.newcouleur = "cyan"

            elif self.couleur == 4:
                
                self.newcouleur = "noire"

            return str(self.type_carte()) + " - " + self.newcouleur

        else :

            return str(self.type_carte())
            
    def effet_carte(self):

        if 0 <= self.nombre <= 10 :

            self.effet = 0

        elif self.nombre == 10:

            self.effet = 1

        elif self.nombre == 11:

            self.effet = 2

        elif self.nombre == 12:

            self.effet = 3

        elif self.nombre == 13:

            self.effet = 4

        elif self.nombre == 14:

            self.effet = 5

        return self.effet


    def get_nombre (self):

        return self.nombre
    
    def get_couleur (self):

        return self.couleur

    def __str__ (self):

        return str(self.structuration())

carte = Carte(2,10)
carte.effet_carte()
print(carte.effet)
print(carte)
print(carte.get_nombre())
print(carte.type_carte())