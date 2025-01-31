from random import randint
from carte_valide import *



def jouer_carte(Main_bot, carteMilieu):
    for k in range(len(Main_bot)):
        if carte_valide(carteMilieu, Main_bot[k]) == True:
            return (Main_bot[k], k)
        
def jouer_carte2(Main_bot, couleur):
    for k in range(len(Main_bot)):
        if carte_valide2(couleur, Main_bot[k]) == True:
            return (Main_bot[k], k)
        
def choix_complexe(Main_bot, Main_player, carteMilieu):
    l = []
    for k in range(len(Main_bot)):
        if carte_valide(carteMilieu, Main_bot[k]) == True:
            l = l + [(Main_bot[k], k)]
    if len(Main_player) <= 4:
        for k in range(len(l)):
            if l[k][0].nombre == 13:
                return (l[k])
            if l[k][0].nombre == 12:
                return (l[k])
    else:
        for k in range(len(l)):
            if l[k][0].nombre != 13 and l[k][0].nombre !=12 and l[k][0].nombre !=11 and l[k][0].nombre !=14:
                return (l[k])
    return jouer_carte(Main_bot, carteMilieu)

def choix_complexe2(Main_bot, Main_player, couleur):
    l = []
    for k in range(len(Main_bot)):
        if carte_valide2(couleur, Main_bot[k]) == True:
            l = l + [(Main_bot[k], k)]
    if len(Main_player) <= 4:
        for k in range(len(l)):
            if l[k][0].nombre == 13:
                return (l[k])
            if l[k][0].nombre == 12:
                return (l[k])
    return jouer_carte2(Main_bot, couleur)