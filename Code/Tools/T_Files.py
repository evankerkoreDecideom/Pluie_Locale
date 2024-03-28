import os

def deplacer_fichiers_de_downloads_vers_workspace(fullpath_filename_in, fullpath_filename_out):
    os.rename(fullpath_filename_in, fullpath_filename_out)

def recuperer_une_donnee_depuis_fichier(path):
    f=open(path, 'r')
    data = f.readlines()[0]
    f.close()
    return data

def creation_dossier(fullpath_folder):
    os.mkdir(fullpath_folder)

def definir_dossier_actif(fullpath_folder):
    os.chdir(fullpath_folder)

def cloner_projet_via_lien(lien_github):
    os.system("git clone " + lien_github)