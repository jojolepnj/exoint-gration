"""Module manipulant des fichiers texte."""
from filecmp import *
def diff(file_first, file_second):
    for name in dcmp.diff_files:

        print("diff_file %s found in %s and %s" % (name, dcmp.left,

              dcmp.right))

    for sub_dcmp in dcmp.subdirs.values():

        diff(sub_dcmp)


	dcmp = dircmp(file_first, file_second) 
	
    return dcmp

def same(file_first, file_second):
    """Fonction retournant True si deux fichiers sont identiques."""
    return True
