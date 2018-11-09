#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

# Name: 2a-moy
# Description: Jeu du plus ou moins qui lis dans un fichier.
# Date: 23/10/18
# Gans Quentin

# Importation de modules
import random
import re
import signal


# Fonction qui affiche la solution et au revoir
def message():
    write_in_file('A la prochaine ! - La solution était', str(nbr))
    exit()


# Fonction qui écrit dans un fichier
def write_in_file(msg):
    file = open("plusoumoins.txt", "w")
    file.write(msg)
    file.close()


# Fonction qui lis dans du fichier
def read_in_file():
    file = open("plusoumoins.txt", "r")
    msg = file.readline().strip()
    file.close()
    return msg


# Fonction qui quitte le prog si on CTRL+C
def end_game(sig, frame):
    write_in_file('Pas ouf de CTRL+C ')
    exit()


# Si il CTRL+C
signal.signal(signal.SIGINT, end_game)

# Variables
end = False
nbr = random.randint(0, 100)

write_in_file('Bonjour, entrez un nombre entre 0 et 100 ! : ')

# Logique du jeu
while end is False:
    # On va lire dans le file
    saisi = read_in_file()
    # On check que ce soit un int
    if re.match("^[0-9]+$", saisi):
        saisi = int(saisi)
        # Et qu'il ne soit pas au dessus de 100
        if saisi < 0 and saisi > 100:
            write_in_file('Entrez un nombre entre 0 et 100 ! : ')
            continue
        if saisi > nbr:
            write_in_file('Trop grand !')
        elif saisi < nbr:
            write_in_file('Trop petit !')
        # Sinon on affiche win, on set le end en win
        else:
            write_in_file('Gg a toi ! ')
            end = True
            message()
