#!/bin/env python3.6

# Name: 3b-opt.py
# Description: Script qui permet d'effectuer une sauvegarde sur N repertoires
# Date: 05/10/18
# Gans Quentin / Axel Paris

# Import des modules
import signal
import shutil
import gzip
import os
import sys
import argparse


# Fonction qui quitte proprement le prog
def end_prog(sig, frame):
    supprArchive()
    sys.exit(0)

signal.signal(signal.SIGINT, end_prog)


# Fonction qui cree une archive
def createArchive(save_directory, archive):
    os.remove(save_directory + '/'+archive+'.tar.gz')
    shutil.move(archive + '.tar.gz', save_directory)


# Fontion qui supprime l'archive déjà existante
def supprArchive(path_archive):
    if os.path.exists(path_archive + '.tar.gz'):
        os.remove(path_archive + '.tar.gz')


# Defini le lien du dossier a sauvegarder
def get_path():
  if args.path:
    return args.path
  else:
    return '~/B2-Python/scripts'


# Defini le lien du dossier a sauvegarder
def get_save_directory(args):
    if args.save:
        return '~/data/' + args.save
    else:
        return '~/data/'


# Defini le lien du dossier ou seront les archives
def get_paths_to_save(args):
  if args.path:
        paths = args.path.split(',')
        return paths
  else:
        print('Vous devez renseigner un repertoire a archiver')
        exit()


# Variables
parser = argparse.ArgumentParser()
parser.add_argument("-p" ,"--path", help="Lien vers le dossier a archiver")
parser.add_argument("-s" ,"--save", help="Lien dans le dossier /data ou seront les archives")
args = parser.parse_args()


paths_to_save = get_paths_to_save(args)
save_directory = os.path.expanduser(get_save_directory(args))


archive_number = 0


for path_data in paths_to_save:
    archive_number = archive_number+1
    archive_name = 'archive'+str(archive_number)

    path_data = os.path.expanduser(path_data)
    print('archive_name: '+archive_name)
    print(save_directory)


    # On try pour voir si l'archive existe sinon on la crée
    try:
        os.makedirs(path_data, exist_ok=True)
    except OSError:
        if not os.path.isdir(path_data):
            raise


    # On regarde si on a les permissions W & R
    if os.access(path_data, os.W_OK and os.R_OK):

        # On crée l'archive
        shutil.make_archive('AHAHAH', 'gztar', save_directory)

        # On regarde si une ancienne save existe
        if os.path.exists(save_directory+'/'+archive_name+'.tar.gz'):

            # On va lire à l'interieur de la save existante
            with gzip.open(save_directory+'/'+archive_name+'.tar.gz', 'rb') as f:
                exist_save = f.read()
            # On va lire la nouvelle save maintenant
            with gzip.open(save_directory+'/'+archive_name+'.tar.gz', 'rb') as f:
                new_save = f.read()

            # On compare les deux save
            if exist_save != new_save:
                # On supprime l'ancienne et on sauvegarde la nouvelle
                createArchive(save_directory, archive_name)
                sys.stdout.write('Succes : La sauvegarde a ete effectuer\n')

            else:
                supprArchive(save_directory+archive_name)
                sys.stdout.write('Erreur : La sauvegarde existe deja\n')

        else:
            shutil.move(archive_name+'.tar.gz', save_directory)
            sys.stdout.write('Succes : La sauvegarde a été effectuer\n')

    else:
        sys.stderr.write('Erreur : Vous ne disposez pas des droits sur le répertoire de destination\n')

