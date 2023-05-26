# -*- coding: utf-8 -*-

import pandas
import os
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

# ===================================
#   Récupérer du fichier téléchargé
# ===================================

def get_fullpath_downloaded_user():
    liste = list(Path("C:/Users").glob("**/transco_user_personne_a5q7y1p9k3.csv"))
    if (len(liste) != 0):
        return liste[0].__str__()
    else:
        return ""

# ==============================================
#   Déplacer et renommer le fichier téléchargé
# ==============================================

def move_files(filename_in, filename_out):
    os.rename(filename_in, filename_out)

# Récupération des données sur tous les chemins

df_path = get_df_from_csv(list(Path("C://").glob("**/Path.csv"))[0].__str__())
df_path_explicit = get_df_explicit(df_path)

# Constitustion des chemins

path_imp_src_exe =      get_value_from_df(df_path_explicit, "pf_imp_src_exe")
path_fait_exe =         get_value_from_df(df_path_explicit, "pf_fait_exe")
path_repo =             get_value_from_df(df_path_explicit, "p_repo")
path_rapport =          get_value_from_df(df_path_explicit, "pf_rapport")

# Se placer sur le repository

os.chdir(path_repo)

# Mettre à jour les données issues du GitHub

os.system("git pull")

# Si une nouvelle version de la base de données users et disponible on la met à disposition

if (get_fullpath_downloaded_user() != ""):
    path_file_user = get_value_from_df(df_path_explicit, "p_cibles") + get_value_from_df(df_path_explicit, "f_user")
    move_files(get_fullpath_downloaded_user(), path_file_user)

os.system(path_imp_src_exe)
os.system(path_fait_exe)
os.system(path_rapport)