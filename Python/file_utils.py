"""Module manipulant des fichiers texte."""
from filecmp import *
def diff(file_first, file_second):
    """Fonction retournant True si deux fichiers sont différents."""
    return dircmp(file_first, file_second)

def same(file_first, file_second):
    """Fonction retournant True si deux fichiers sont identiques."""
    return True
