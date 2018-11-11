#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

# Name : 2b-mol
# Description : Resolution du 2a
# Date : 09/11/18
# Gans Quentin

# Importation des modules
import signal
import random
import time


# Fonction qui quitte le prog si on CTRL+C
def end_game(sig, frame):
    write_in_file('Pas ouf de CTRL+C ')
    exit()


# Si il CTRL+C
signal.signal(signal.SIGINT, end_game)


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
    msg = file.read()
    file.close()
    return msg



# Variables
end = False
nbr = random.randint(0, 100)
max = 100
min = 0
total = 0

# Logique du jeu
while end is False:

    print("Max : " + str(max) + " Min : " + str(min))

    total = round((max + min) / 2)
    write_in_file(str(total))

    print(total)
    time.sleep(4)

    choice = read_in_file()
    print("Le choix est : " + choice)

    if choice == 'Gg a toi !':
        end = True
        print("Win !")

    elif choice == 'Trop grand !':
        max = choice
        print('Trop grand')

    elif choice == 'Trop petit !':
        min = choice
        print('Trop petit')

message()
