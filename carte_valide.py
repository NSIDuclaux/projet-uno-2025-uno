from carte import Carte

def carte_valide(carteposee, cartepropose):
    if type(cartepropose) == str or type(carteposee) == str:
        return True
    if carteposee.couleur == cartepropose.couleur:
        return True
    if cartepropose.nombre == 13 or cartepropose.nombre == 14:
        return True
    if cartepropose.nombre == carteposee.nombre:
        return True
    return False
def carte_valide2(couleur, cartepropose):
    if type(cartepropose) == str:
        return True
    if cartepropose.nombre == 13 or cartepropose.nombre == 14:
        return True
    if couleur == cartepropose.couleur:
        return True
    return False
# cartepose = Carte(3, 8)
# cartepropose = Carte(1, 14)
# print(carte_valide(cartepose, cartepropose))
