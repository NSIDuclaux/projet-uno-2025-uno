from carte import Carte

def carte_valide(carteposee, cartepropose):
    if carteposee.couleur == cartepropose.couleur:
        return True
    if cartepropose.nombre == carteposee.nombre:
        return True
    if cartepropose.nombre == 13 or cartepropose.nombre == 14:
        return True
    return False

# cartepose = Carte(3, 8)
# cartepropose = Carte(1, 14)
# print(carte_valide(cartepose, cartepropose))
#def carte_valide(carteposee, cartepropose):
    if carteposee[4] == cartepropose[4] or carteposee[5] == cartepropose[5] or carteposee[4] == cartepropose[5] or carteposee[5] == cartepropose[4]:
        return True
    if cartepropose[0:1] == carteposee[0:1]:
        return True
    if cartepropose[0:1] == 13 or cartepropose[0:1] == 14:
        return True
    return False