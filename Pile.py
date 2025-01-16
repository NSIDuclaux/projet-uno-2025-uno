"""Implémentation des piles avec des listes Python"""


def creer():
    """Retourne une pile vide"""
    return []


def taille(pile):
    """Retourne le nombre d'éléments de la pile"""
    return len(pile)


def est_vide(pile):
    """Retourne True si la pile est vide, False sinon"""
    return pile == []


def empiler(pile, element):
    """Empile un nouvel élément au sommet de la pile"""
    pile.append(element)


def depiler(pile):
    """Retourne l'élément situé au sommet de la pile
    et le supprime de celle-ci"""
    if not est_vide(pile):
        return pile.pop()
    else:
        return None


def sommet(pile):
    """Retourne l'élément situé au sommet de la pile"""
    if not est_vide(pile):
        return pile[-1]
    else:
        return None