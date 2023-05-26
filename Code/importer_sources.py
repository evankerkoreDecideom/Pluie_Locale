# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas
import shutil
import datetime
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

# =================================
#   Récupérer de données diverses
# =================================

def get_transco_in_df(path_input):
    return pandas.read_csv(path_input, sep=';')

def get_liste_onglet(df):
    return df["onglet"]

def get_secret(path):
    f=open(path, 'r')
    chaine = f.readlines()[0]
    f.close()
    return chaine

# ================================
#   Archiver les données sources
# ================================

def copy_and_archive(folder_in, folder_out, name):
    file_archived = name + "_" + datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + ".csv"
    file_in = folder_in + name + ".csv"
    file_out = folder_out + file_archived
    shutil.copy(file_in , file_out)
    
# Récupération des données sur tous les chemins

df_path = get_df_from_csv(list(Path("C://").glob("**/Path.csv"))[0].__str__())
df_path_explicit = get_df_explicit(df_path)

# Constitustion des chemins

path_file_gs =      get_value_from_df(df_path_explicit, "p_secrets") +  get_value_from_df(df_path_explicit, "f_GS_ID")
path_file_user =    get_value_from_df(df_path_explicit, "p_cibles") +   get_value_from_df(df_path_explicit, "f_user")
path_src =     get_value_from_df(df_path_explicit, "p_sources")
path_archive = get_value_from_df(df_path_explicit, "p_archives")

# Initialisation des variables 

fait_entete_csv = "id_personne;id_temporalite;valeur\n"
googleSheetId = get_secret(path_file_gs)
    
# Récupération des données sur les utilisateurs

transco_df = get_transco_in_df(path_file_user)

# Pour chaque saisie utilisateur on exporte et on archive un fichier CSV

for onglet in get_liste_onglet(transco_df):
    url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
    	googleSheetId,
    	onglet)
    data_df = pandas.read_csv(url)[["date", "valeur"]]
    data_df.to_csv(path_src + onglet + ".csv", sep=";", index=False)
    copy_and_archive(path_src, path_archive, onglet)