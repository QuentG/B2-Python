#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

# Titre: 1b-dic
# Description :On saisi plusieurs string, on affiche le tableau de string ordonner en ordre alphabetique.
# Date: 15/10/18
# Gans Quentin

# Import
import re

reg = re.compile('^[a-zA-Z]+$')

# Variables
my_list = []
element = ""

while my_list != "":
    print("Salut a tous ! Saisi des prenoms ou sinon appuie sur q pour quitter !")
    element = input("Entrez un prenom pls :")


    # On test la regex
    if reg.match(element):
     my_list.append(element)


    # Quand on appuie sur q on quitte le prog
     if element == 'q':
           break

    else:
        print("ce n'est pas un prenom")


my_list = my_list[:-1]
# On ordonne
my_list.sort()
print(my_list)
