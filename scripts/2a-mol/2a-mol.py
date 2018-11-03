#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

#Name: 2a-moy
#Description: Jeu du plus ou moins qui lit dans un fichier.
#Date: 23/10/18
#Gans Quentin

#Importation de modules
import random
import signal

#Fonction qui affiche la solution et au revoir
def message():
    return write_in_file('A la prochaine ! - La solution était', str(nbr))
    exit()

#Fonction qui écrit dans un fichier
def write_in_file(msg):
  file = open(path_file, "w")
  file.write(msg)
  file.close()

#Fonction qui lis dans du fichier
def read_in_file():
  file = open(path_file, "r")
  input = file.readline().strip()
  file.close()
  return input

#Fonction qui check si c'est un nombre
def checkNumber():
  number = read_in_file()
  #Si c'est pas un nombre on retry
  while(number.isdigit() == False):
    number = read_in_file()
  return int(number)

#Fonction jeu qui va retourner trop grand, trop petit ou gagné
def game():
  if (nbr == saisi):
    end = True
    return 'gagné'
  elif (saisi > nbr):
    return 'trop grand'
  else:
    return 'trop petit'

#Fonction qui quitte le prog si on CTRL+C
def end_game(sig, frame):
    write_in_file('\nPas ouf de CTRL+C ')
    exit()

#Si il CTRL+C
signal.signal(signal.SIGINT, end_game)

#Variables
path_file = "plusoumoins.txt"
end = False
nbr = random.randint(0,100)
saisi = -1

write_in_file('Entrez un nombre entre 0 et 100 ! : ')

#Logique du jeu
while (saisi != nbr and end == False):
    saisi = checkNumber()
    result = game()
    write_in_file(result)
    write_in_file(message())

        
