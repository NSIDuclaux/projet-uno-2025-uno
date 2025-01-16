from carte import Carte

def carte_valide(carteposee, cartepropose):
    if carteposee.couleur == cartepropose.couleur:
        return True
    if cartepropose.nombre == cartepose.nombre:
        return True
    if cartepropose.nombre == 13 or cartepropose.nombre == 14:
        return True







cartepose = Carte(5, 8)
cartepropose = Carte(5, 8)
carte_valide(cartepose, cartepropose)