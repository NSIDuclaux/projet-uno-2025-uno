from carte import *

def tri_selection(tableau: list) -> list:
    """Trie en place par sélection le tableau passé en paramètre."""
    for i in range(len(tableau)):
        min = i
        for j in range(i+1, len(tableau)):
            if tableau[j].get_nombre() < tableau[min].get_nombre():
                min = j
        tableau[i], tableau[min] = tableau[min], tableau[i]
    return tableau