#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

#Name: 1d-moy
#Description: Jeu du plus ou moins.
#Date: 19/10/18
#Gans Quentin

#Importation de modules
import random
import re
import signal

#Variables
coups = 0
end = False
nbr = random.randint(0,100)

#Fonction qui affiche la solution et au revoir
def message():
    return print('A la prochaine ! - La solution était',str(nbr))
    exit()

#Fonction qui quitte le prog si on CTRL+C
def end_game(sig, frame):
    print('\nPas ouf de CTRL+C ')
    exit()

#Si il CTRL+C
signal.signal(signal.SIGINT, end_game)

#Logique du jeu
while end is False :
    coups += 1
    saisi = input('Entrez un nombre entre 0 et 100 ! : ')

    #On check que ce soit un int 
    if re.match("^[0-9]+$", saisi):
        saisi = int(saisi)
        #Et qu'il ne soit pas au dessus de 100
        if saisi < 0 and saisi > 100:
            print('Entrez un nombre en 0 et 100 svp ! :')
            continue
           
        if saisi > nbr :
            print ('Trop grand !')       
        elif saisi < nbr :
            print ('Trop petit !')
        #Le joueur appui sur q pour quitter le prog
        elif saisi == 'q' :
            message()
        #Sinon on affiche win, on set le end en win
        else :
            print ('Gg a toi ! Tu as trouver le nombre en',str(coups), 'coups')
            end = True
            message()
    
        
        
