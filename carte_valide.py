from carte import Carte
from main_joueur import *
def carte_valide(carteposee, cartepropose):
    if type(cartepropose) == str or type(carteposee) == str:
        return True
    if carteposee.couleur == "noire":
        return True
    if carteposee.couleur == cartepropose.couleur:
        return True
    if cartepropose.nombre == 13 or cartepropose.nombre == 14:
        return True
    if cartepropose.nombre == carteposee.nombre:
        return True
    return False
def carte_valide2(couleur, cartepropose):
    if couleur == cartepropose.get_couleur():
        return True
    if cartepropose == "+4 Cartes" or cartepropose == "Changez de Couleur":
        return True
    if cartepropose.nombre == 13 or cartepropose.nombre == 14:
        return True
    if couleur == cartepropose.get_couleur():
        return True
    return False

def renvoie_valide(carteposee, main):
    c = -1
    for k in main.main_joueur:
        c = c + 1
        if carteposee.nombre == k.nombre or k.nombre == 13 or k.nombre == 12:
            return c
    return False

def renvoie_valide_plus(carteposee, main):
    c = -1
    for k in main.main_joueur:
        c = c + 1
        if carteposee.nombre == k.nombre or k.nombre == 13:
            return c
    return False

def renvoie_valide2(cartepropose):
    if cartepropose.nombre == 13 or cartepropose.nombre == 12:
        return True
    else:
        return False

def renvoie_valide_plus2(carte):
    if carte.nombre == 13:
        return True
    else:
        return False
    

#cartepose = "jaune"
#cartepropose = Carte(0, 8)
#print(carte_valide2("jaune", cartepropose))
