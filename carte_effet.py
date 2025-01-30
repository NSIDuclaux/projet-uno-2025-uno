from random import *
def inverse (sens_horaire):

    if sens_horaire == True:

        sens_horaire = False

        print("Le sens est antihoraire")

    else :

        sens_horaire = True
        print("Le sens est horaire")

    return sens_horaire

def interdit_jouer ():

    pouvoirJouer = False

    print("Le joueur suivant ne peut pas jouer")

    return pouvoirJouer

def plus_2_carte (main,deck):

    for i in range (2):

        main.ajouter_carte(deck.retirer_carte())

    print("Le joueur suivant reçoit 2 carte")


def changer_couleur():

    nouvelleCouleur = ["", 1]

    #while nouvelleCouleur[0] != "0" or nouvelleCouleur[0] != "1" or nouvelleCouleur[0] != "2" or nouvelleCouleur[0] != "3":
    nouvelleCouleur[0] = input("Choissez une nouvelle couleur")
    if nouvelleCouleur[0] == "0":
        nouvelleCouleur[0] == "rouge"
    if nouvelleCouleur[0] == "1":
        nouvelleCouleur[0] == "vert"
    if nouvelleCouleur[0] == "2":
        nouvelleCouleur[0] == "jaune"
    if nouvelleCouleur[0] == "3":
        nouvelleCouleur[0] == "bleu"
    print("La nouvelle couleur est",nouvelleCouleur[0])

    return nouvelleCouleur

def plus_4_carte (main,deck):

    for i in range (4):

        main.ajouter_carte(deck.retirer_carte())

    nouvelleCouleur = ["", 1]

    #while nouvelleCouleur[0] != "0" or nouvelleCouleur[0] != "1" or nouvelleCouleur[0] != "2" or nouvelleCouleur[0] != "3":
    nouvelleCouleur[0] = input("Choissez une nouvelle couleur")
    if nouvelleCouleur[0] == "0":
        nouvelleCouleur[0] == "rouge"
    if nouvelleCouleur[0] == "1":
        nouvelleCouleur[0] == "vert"
    if nouvelleCouleur[0] == "2":
        nouvelleCouleur[0] == "jaune"
    if nouvelleCouleur[0] == "3":
        nouvelleCouleur[0] == "bleu"
    print("Le joueur suivant reçoit 4 carte, et la nouvelle couleur est",nouvelleCouleur[0])

    return nouvelleCouleur

def bot_changer_couleur():

    c = randint(0,3)
    d = ["rouge","vert","bleu","jaune"]
    nouvelleCouleur= [d[c], 1]
    print("La nouvelle couleur est",nouvelleCouleur[0])

    return nouvelleCouleur

def bot_plus_4_carte (main,deck):

    for i in range (4):

        main.ajouter_carte(deck.retirer_carte())

    c = randint(0,3)
    d = ["rouge","vert","bleu","jaune"]
    nouvelleCouleur= [d[c], 1]

    print("Le joueur suivant reçoit 4 carte, et la nouvelle couleur est",nouvelleCouleur[0])

    return nouvelleCouleur