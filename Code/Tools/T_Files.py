import os

def deplacer_et_renommer_fichiers(fullpath_filename_in, fullpath_filename_out):
    os.rename(fullpath_filename_in, fullpath_filename_out)

def deplacer_fichiers(fullpath_folder_in, fullpath_folder_out, filename):
    os.replace(fullpath_folder_in + '\\' + filename, fullpath_folder_out + '\\' + filename)

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

def fichier_present(fullpath_file):
    return os.path.isfile(fullpath_file)

def supprimer_dossier_vide(dossier_vide):
    os.rmdir(dossier_vide)