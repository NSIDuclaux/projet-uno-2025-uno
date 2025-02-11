from random import randint
from carte_valide import *
from main_joueur import *

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
    max = 0
    fr = [0,0,0,0]

    new_c = 0
    for k in range(len(Main_bot)):
        if carte_valide(carteMilieu, Main_bot[k]) == True:
            l = l + [(Main_bot[k], k)]
    for k in range(len(Main_bot)):
        if Main_bot[k].couleur == 0:
            fr[0] = fr[0] + 1
        if Main_bot[k].couleur == 1:
            fr[1] = fr[1] + 1
        if Main_bot[k].couleur == 2:
            fr[2] = fr[2] + 1
        if Main_bot[k].couleur == 3:
            fr[3] = fr[3] + 1
    if len(Main_player) <= 3:
        for k in range(len(l)):
            if l[k][0].nombre == 13:
                return (l[k])
            if l[k][0].nombre == 12:
                return (l[k])
    else:
        for g in range(len(fr)):
                    if fr[g] > max:
                        max = fr[g]
                        new_c = g
        for k in range(len(l)):
            if l[k][0].nombre != 13 and l[k][0].nombre !=12 and l[k][0].nombre !=11 and l[k][0].nombre !=14:
                if l[k][0].couleur == new_c:
                    return (l[k])
        for k in range(len(l)):
            if l[k][0].nombre != 13 and l[k][0].nombre !=12 and l[k][0].nombre !=11 and l[k][0].nombre !=14:
                return (l[k])
    return jouer_carte(Main_bot, carteMilieu)

def choix_complexe2(Main_bot, Main_player, couleur):
    l = []
    for k in range(len(Main_bot)):
        if carte_valide2(couleur, Main_bot[k]) == True:
            l = l + [(Main_bot[k], k)]
    if len(Main_player) <= 3:
        for k in range(len(l)):
            if l[k][0].nombre == 13:
                return (l[k])
            if l[k][0].nombre == 12:
                return (l[k])
    return jouer_carte2(Main_bot, couleur)


#a = list(dico.keys())