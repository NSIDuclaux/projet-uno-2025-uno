from carte import Carte

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
    if couleur == cartepropose.couleur:
        return True
    if couleur == "violet":
        couleur = 0
    if couleur == "rose":
        couleur = 1
    if couleur == "bleu":
        couleur = 2
    if couleur == "cyan":
        couleur = 3
    if cartepropose == "+4 Cartes" or cartepropose == "Changez de Couleur":
        return True
    if cartepropose.nombre == 13 or cartepropose.nombre == 14:
        return True
    if couleur == cartepropose.couleur:
        return True
    return False
#cartepose = "jaune"
#cartepropose = Carte(0, 8)
#print(carte_valide2("jaune", cartepropose))
