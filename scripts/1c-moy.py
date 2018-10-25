#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

#Titre: 1c-moy
#Saisi de plusieurs prénoms + notes, fait la moyenne des notes, quand on appuie sur q l'on quitte le prog.
#Gans Quentin
#15/10/18

#Import
import operator


#Fonction qui check l'input d'un nombre
def inputNote():
  note = input('Entrez une note : ')

  #Si c'est pas un nombre on retry
  while(note.isdigit() == False):
    note = input('Entrez une note avec des nombres : ')
  return int(note)

#Fonction qui check l'input d'un string
def inputPrenom():
  nom = input('Entrez un prénom : ')
  
  #Si c'est pas un string on retry
  while(nom.isalnum() == False):
    nom = input('Entrez un prenom avec des lettres : ')
  return str(nom) 

#Variables qu'on aime tant <3
dict = {}
tour = 0
sum = 0

#Tant que tour est égale a 0
while tour == 0:
    nom = inputPrenom()
    #Si l'on appuie sur q l'on quitte le prog la classique.
    if nom == "q":

        #On ajoute dans le dico ;)
        for liste in sorted(dict):
            full = dict[liste]
            print(full)
            sum += int(full)
            
        #Calcul de la moyenne des notes saisi.    
        print("Votre moyenne est égale a : ")
        moy = sum / len(dict)
        print(moy)
        print("Liste des notes : ")
        #On fait le top 5 des notes
        print(sorted(dict.items(), key=operator.itemgetter(1), reverse = True)[:5])
        break
    
    else:
        note = inputNote()
        dict[nom] = note

