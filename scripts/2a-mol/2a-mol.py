#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

#Name: 2a-moy
#Description: Jeu du plus ou moins qui lis dans un fichier.
#Date: 23/10/18
#Gans Quentin

#Importation de modules
import random
import re
import signal

#Fonction qui affiche la solution et au revoir
def message():
    return write_in_file('A la prochaine ! - La solution était', str(nbr))
    exit()

#Fonction qui quitte le prog si on CTRL+C
def end_game(sig, frame):
    write_in_file('Pas ouf de CTRL+C ')
    exit()

#Si il CTRL+C
signal.signal(signal.SIGINT, end_game)

#Fonction qui écrit dans un fichier
def write_in_file(msg):
  file = open("plusoumoins.txt", "w")
  file.write(msg)
  file.close()

#Fonction qui lis dans du fichier
def read_in_file():
  file = open("plusoumoins.txt", "r")
  msg = file.readline().strip()
  file.close()
  return msg

#Variables
coups = 0
end = False
nbr = random.randint(0,100)

write_in_file('Entrez un nombre entre 0 et 100 ! : ')

#Logique du jeu
while end is False :
    coups += 1
    #On va lire dans le file 
    saisi = read_in_file()

    #On check que ce soit un int 
    if re.match("^[0-9]+$", saisi):
        saisi = int(saisi)
        #Et qu'il ne soit pas au dessus de 100
        if saisi > 100:
            continue
           
        if saisi > nbr :
            write_in_file('Trop grand !')       
        elif saisi < nbr :
            write_in_file('Trop petit !')
        #Le joueur appui sur q pour quitter le prog
        elif saisi == 'q' :
            write_in_file(message())
        #Sinon on affiche win, on set le end en win
        else :
            write_in_file('Gg a toi ! Tu as trouver le nombre en',str(coups), 'coups')
            end = True
            write_in_file(message())

        
        
