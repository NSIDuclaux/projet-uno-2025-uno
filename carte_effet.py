from carte import *
from deck import *
from main_joueur import *

def inverse (sens_horaire):

    if sens_horaire == True:

        sens_horaire = False

    else :

        sens_horaire = True

    return sens_horaire

def interdit_jouer ():

    pouvoirJouer = False

    return pouvoirJouer

def plus_2_carte (main,deck):

    for i in range (2):

        main.ajouter_carte(deck.retirer_carte())

def changer_couleur():

    nouvelleCouleur = ""

    while nouvelleCouleur != "jaune" or nouvelleCouleur != "rouge" or nouvelleCouleur != "bleu" or nouvelleCouleur != "vert":
            
        nouvelleCouleur = str(input("Choissez une nouvelle couleur")).lower()

    return nouvelleCouleur

def plus_4_carte (main,deck):

    for i in range (4):

        main.ajouter_carte(deck.retirer_carte())

        nouvelleCouleur = ""

    while nouvelleCouleur != "jaune" or nouvelleCouleur != "rouge" or nouvelleCouleur != "bleu" or nouvelleCouleur != "vert":
            
        nouvelleCouleur = str(input("Choissez une nouvelle couleur")).lower()

    return nouvelleCouleur
