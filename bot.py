from random import randint
from carte_valide import *


def jouer_carte(Main_bot, carteMilieu):
    for k in range(len(Main_bot)):
        if carte_valide(carteMilieu, Main_bot[k]) == True:
            return Main_bot[k]
def jouer_carte2(Main_bot, couleur):
    for k in range(len(Main_bot)):
        if carte_valide2(couleur, Main_bot[k]) == True:
            return Main_bot[k]