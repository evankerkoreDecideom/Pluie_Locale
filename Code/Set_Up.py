# -*- coding: utf-8 -*-
"""
Created on Thu May 25 09:09:55 2023

@author: Decideom
"""

import os
import pandas
import shutil
import time
from pathlib import Path

# ============================================
#   Récupérer des chemins et nom de fichiers
# ============================================

def get_df_from_csv(filename_csv):
    return pandas.read_csv(filename_csv, sep=';')[["cle", "valeur"]]

def get_df_explicit(dataframe):
    return dataframe.apply(lambda x: x.replace(
                            {'____':get_value_from_df(dataframe, "__GITHUB__")}
                            ,regex=True))

def get_value_from_df(dataframe, valeurCle):
    return dataframe[dataframe.cle == valeurCle]["valeur"].iloc[0]

# =====================================================
#   Récupérer une information contenu dans un fichier
# =====================================================

def get_one_data_from_file(path):
    f=open(path, 'r')
    data = f.readlines()[0]
    f.close()
    return data

# ======================================
#   Récupérer des fichiers téléchargés
# ======================================

def get_fullpath_downloaded_googlesheet():
    liste = list(Path("C:/Users").glob("**/GoogleSheetID_a5q7y1p9k3.txt"))
    if (len(liste) != 0):
        return liste[0].__str__()
    else:
        return ""

def get_fullpath_downloaded_user():
    liste = list(Path("C:/Users").glob("**/transco_user_personne_a5q7y1p9k3.csv"))
    if (len(liste) != 0):
        return liste[0].__str__()
    else:
        return ""

def get_fullpath_downloaded_github():
    liste = list(Path("C:/Users").glob("**/GitHub_a5q7y1p9k3.txt"))
    if (len(liste) != 0):
        return liste[0].__str__()
    else:
        return ""

def get_fullpath_downloaded_path():
    liste = list(Path("C:/Users").glob("**/Path_a5q7y1p9k3.csv"))
    if (len(liste) != 0):
        return liste[0].__str__()
    else:
        return ""

def get_fullpath_downloaded_setup():
    liste = list(Path("C:/Users").glob("**/Set_Up_a5q7y1p9k3.exe"))
    if (len(liste) != 0):
        return liste[0].__str__()
    else:
        return ""

def move_files(filename_in, filename_out):
    os.rename(filename_in, filename_out)

def get_path_file_Path():
    return get_value_from_df(df_path_explicit, "p_secrets") + get_value_from_df(df_path_explicit, "f_path")

# Récupération de la liste des fichiers téléchargés depuis Google Drive

fullpath_downloaded_gs =        get_fullpath_downloaded_googlesheet()
fullpath_downloaded_user =      get_fullpath_downloaded_user()
fullpath_downloaded_github =    get_fullpath_downloaded_github()
fullpath_downloaded_path =      get_fullpath_downloaded_path()
fullpath_downloaded_setup =     get_fullpath_downloaded_setup()

# Récupération des données liées aux chemins

df_path = get_df_from_csv(fullpath_downloaded_path)
df_path_explicit = get_df_explicit(df_path)

# Variable contenant le chemin du dossier contenant le repository

path_container_repository = get_value_from_df(df_path_explicit, "__GITHUB__")

# Création du dossier qui va contenir le repository

os.mkdir(path_container_repository)
os.chdir(path_container_repository)

# Récupération du projet Git Hub

link_github = get_value_from_df(df_path_explicit, "v_link_github")
os.system("git clone " + link_github)

# Finalisation de la construction de l'arborescence

path_data =     get_value_from_df(df_path_explicit, "p_data")
path_cible =    get_value_from_df(df_path_explicit, "p_cibles")
path_source =   get_value_from_df(df_path_explicit, "p_sources")
path_archive =  get_value_from_df(df_path_explicit, "p_archives")
path_secrets =  get_value_from_df(df_path_explicit, "p_secrets")

os.mkdir(path_data)
os.mkdir(path_cible)
os.mkdir(path_source)
os.mkdir(path_archive)
os.mkdir(path_secrets)

# Déplacement et renommage des données téléchargées vers le projet

path_file_setup = get_value_from_df(df_path_explicit, "p_dist") + get_value_from_df(df_path_explicit, "f_set_up")
path_file_user = path_cible     + get_value_from_df(df_path_explicit, "f_user")
path_file_Path = path_secrets   + get_value_from_df(df_path_explicit, "f_path")
path_file_GSID = path_secrets   + get_value_from_df(df_path_explicit, "f_GS_ID")
path_file_github = path_secrets + get_value_from_df(df_path_explicit, "f_github")

move_files(fullpath_downloaded_path,    path_file_Path)
move_files(fullpath_downloaded_gs,      path_file_GSID)
move_files(fullpath_downloaded_user,    path_file_user)
move_files(fullpath_downloaded_github,  path_file_github)
move_files(fullpath_downloaded_setup,   path_file_setup)

# Exécution de l'exécutable

temporalite_exe = get_value_from_df(df_path_explicit, "p_dist") + get_value_from_df(df_path_explicit, "f_temporalite_exe")
os.system(temporalite_exe)