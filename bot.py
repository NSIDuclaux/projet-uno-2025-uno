from random import randint
from cartevalide import carte_valide

def jouer_carte(Main_bot, carteMilieu):
    for k in range(len(Main_bot)):
        if carte_valide(carteMilieu, Main_bot[k]) == True:
            return Main_bot[k]