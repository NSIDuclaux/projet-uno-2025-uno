from random import *
from carte_valide import *
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

def plus_2_carte (main,bot,deck,carte,pile_milieu,coef):
    valide = False
    for k in range(main.nb_main()):
        if renvoie_valide2(main.main_joueur[k]) == True:
            valide = True
    if valide == True:
        print("renvoie possible")
        print(main)
        valid = False
        while valid == False:
            numeroChoisie = -1
            while int(numeroChoisie) < 0 or int(numeroChoisie) >= main.nb_main():
                numeroChoisie = input("Choissez une carte")
                if int(numeroChoisie) >= 0 and int(numeroChoisie) < main.nb_main():
                    valid = renvoie_valide2(main.main_joueur[int(numeroChoisie)]) 
        carteChoisie = main.choix_carte(int(numeroChoisie))
        print("La carte retourné est :",carteChoisie)
        pile_milieu.append(carteChoisie)
        deck.ajouter_carte(carteChoisie)
        if carteChoisie.nombre == 14:
            coef = coef + 4
        else:
            coef = coef + 2
        plus_2_carte_bot(bot,main,deck,carte,pile_milieu,coef)

    else:
        coef = coef + 2
        for i in range (coef):

            main.ajouter_carte(deck.retirer_carte())

        print("Le joueur suivant reçoit "+ str(coef) +" carte")
        return 's'

def plus_2_carte_bot (bot,main,deck,carte,pile_milieu,coef):
    valide = False
    for k in range(bot.nb_main()):
        if renvoie_valide2(bot.main_joueur[k]) == True:
            valide = True
    if valide == True:
        print("Renvoie de carte")
        carteChoisie = renvoie_valide(carte,bot)
        c = bot.main_joueur[carteChoisie]
        print("La carte retourné est :", c)
        pile_milieu.append(c)
        deck.ajouter_carte(c)
        if c.nombre == 14:
            coef = coef + 4
        else:
            coef = coef + 2
        plus_2_carte(main,bot,deck,carte,pile_milieu,coef)
    else:
        coef = coef + 2
        for i in range (coef):

            bot.ajouter_carte(deck.retirer_carte())
        print("Le joueur suivant reçoit "+ str(coef) +" carte")
        return 's'

def changer_couleur():

    nouvelleCouleur = ["", 1]

    while nouvelleCouleur[0] != "violet" and nouvelleCouleur[0] != "cyan" and nouvelleCouleur[0] != "rose" and nouvelleCouleur[0] != "bleu":
        nouvelleCouleur[0] = input("Choissez une nouvelle couleur")
    print("La nouvelle couleur est",nouvelleCouleur[0])

    return nouvelleCouleur

def plus_4_carte (main,deck):

    for i in range (4):

        main.ajouter_carte(deck.retirer_carte())

    nouvelleCouleur = ["", 1]

    while nouvelleCouleur[0] != "violet" and nouvelleCouleur[0] != "cyan" and nouvelleCouleur[0] != "rose" and nouvelleCouleur[0] != "bleu":
        nouvelleCouleur[0] = input("Choissez une nouvelle couleur")
    
    print("Le joueur suivant reçoit 4 carte, et la nouvelle couleur est",nouvelleCouleur[0])

    return nouvelleCouleur

def bot_changer_couleur():

    c = randint(0,3)
    d = ["violet","rose","bleu","cyan"]
    nouvelleCouleur= [d[c], 1]
    print("La nouvelle couleur est",nouvelleCouleur[0])

    return nouvelleCouleur

def bot_plus_4_carte (main,deck):

    for i in range (4):

        main.ajouter_carte(deck.retirer_carte())

    c = randint(0,3)
    d = ["violet","rose","bleu","cyan"]
    nouvelleCouleur= [d[c], 1]

    print("Le joueur suivant reçoit 4 carte, et la nouvelle couleur est",nouvelleCouleur[0])

    return nouvelleCouleur