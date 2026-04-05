"""Implémentation du type abstrait pile en POO"""


class Chainon:
    def __init__(self, element=None, suivant=None):
        """element est la valeur du chainon et suivant est le chainon qui suit"""
        self.element = element
        self.suivant = suivant


class Pile:
    def __init__(self):
        """Crée une pile vide"""
        self.summit = Chainon()

    def taille(self):
        """Retourne le nombre d'éléments dans la pile"""
        long = 0
        chainon = self.summit
        while chainon.element is not None:
            chainon = chainon.suivant
            long = long + 1
        return long

    def est_vide(self) -> bool:
        """Retourne True si la pile est vide et False sinon"""
        return self.summit.element is None

    def empiler(self, element):
        """Empile element qu sommet de la pile"""
        self.summit = Chainon(element, self.summit)

    def depiler(self):
        """Retourne l'élément situé au sommet de la pile
        et le supprime de celle-ci"""
        item = self.summit.element
        self.summit = self.summit.suivant
        return item

    def sommet(self):
        """Retourne la valeur du sommet de la pile"""
        return self.summit.element

