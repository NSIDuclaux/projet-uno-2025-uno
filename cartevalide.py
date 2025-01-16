from carte import Carte

def carte_valide(carteposee, cartepropose):
    if cartepropose.couleur != 5:
        if carteposee.couleur == cartepropose.couleur:
            return True
    if cartepropose.nombre < 10:
        if cartepropose.nombre == cartepose.nombre:
            return True








cartepose = Carte(5, 8)
cartepropose = Carte(5, 8)
carte_valide(cartepose, cartepropose)