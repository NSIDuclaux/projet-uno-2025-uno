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

    nouvelleCouleur = ""

    while nouvelleCouleur != "jaune" or nouvelleCouleur != "rouge" or nouvelleCouleur != "bleu" or nouvelleCouleur != "vert":
        nouvelleCouleur = str(input("Choissez une nouvelle couleur")).lower()

    print("La nouvelle couleur est",nouvelleCouleur)

    return nouvelleCouleur

def plus_4_carte (main,deck):

    for i in range (4):

        main.ajouter_carte(deck.retirer_carte())

    nouvelleCouleur = ""

    while nouvelleCouleur != "jaune" or nouvelleCouleur != "rouge" or nouvelleCouleur != "bleu" or nouvelleCouleur != "vert":
            
        nouvelleCouleur = str(input("Choissez une nouvelle couleur")).lower()

    print("Le joueur suivant reçoit 4 carte, et la nouvelle couleur est",nouvelleCouleur)

    return nouvelleCouleur