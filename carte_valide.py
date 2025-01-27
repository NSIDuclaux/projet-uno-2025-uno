from carte import Carte

def carte_valide(carteposee, cartepropose):
    if carteposee[4] == cartepropose[4]:
        return True
    if cartepropose[0:1] == carteposee[0:1]:
        return True
    if cartepropose[0:1] == 13 or cartepropose[0:1] == 14:
        return True
    return False

# cartepose = Carte(3, 8)
# cartepropose = Carte(1, 14)
# print(carte_valide(cartepose, cartepropose))