#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

# Titre: 1a-add
# Demande deux nombres à l’utilisateur et affiche le résultat de l’addition des deux nombres. Et on check si c'est un int.
# Gans Quentin
# 15/10/18

import re

# Regex qui check si c'est un int
regex = re.compile('[0-9]+$')

numb1 = input('Entrez un premier nombre : ')
numb2 = input('Entrez un deuxieme nombre : ')


# Fontion qui affiche l'addition des 2 nombres saisi
def addition(nb1, nb2):
    if regex.match(str(nb1)) and regex.match(str(nb2)):
        return int(nb1) + int(nb2)
    # Si c'est pas un nombre RIP
    else:
        print('Pas un nombre sorry')


# On affiche tous ça
print(addition(numb1, numb2))
