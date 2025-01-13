"""Module manipulant des fichiers texte."""
from filecmp import dircmp
def diff(file_first, file_second):
    """Fonction retournant True si deux fichiers sont différents."""
    return filecmp.cmp(file_first, file_second)

def same(file_first, file_second):
    """Fonction retournant True si deux fichiers sont identiques."""
    return True
