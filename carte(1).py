class Carte:
    
    def __init__(self,couleur,nombre):

        #0 = Jaune  #0 #1 #2 #3 #4 #5 #6 #7 #8 #9 
        #1 = Rouge  #Sans inverse = 10 #Passer son tour = 11 # +2 = 12
        #2 = Bleu   #+4 13, #changer de couleur = 14
        #3 = Vert
        #4 = Noir
        
        self.couleur = couleur
        self.nombre = nombre

    def __structuration__(self):
        
        pass
        
    
    def getcouleur(self):

        return (self.couleur)

    def getnombre(self):
        
        return (self.nombre)

    def __str__ (self):

        return str(self.couleur,self.nombre)