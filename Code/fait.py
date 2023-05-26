# -*- coding: utf-8 -*-
"""
Created on Fri May 19 13:09:58 2023

@author: Decideom
"""

import pandas
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

# ===============================================
#   Récupérer des données depuis un fichier CSV
# ===============================================

def get_df_from_csv2(path_input, filename_output):
    return pandas.read_csv(path_input + filename_output, sep=';')

# Récupération des données sur tous les chemins

df_path = get_df_from_csv(list(Path("C://").glob("**/Path.csv"))[0].__str__())
df_path_explicit = get_df_explicit(df_path)

# Constitustion des chemins

path_src =      get_value_from_df(df_path_explicit, "p_sources")
path_cible =    get_value_from_df(df_path_explicit, "p_cibles")
file_user =     get_value_from_df(df_path_explicit, "f_user")
file_tempo =    get_value_from_df(df_path_explicit, "f_temporalite")
file_fait =     get_value_from_df(df_path_explicit, "f_fait")

# Initialisation des variables 

entete_csv = "id_personne;id_temporalite;valeur\n"
lignes_fait = ""

# Récupération des données sur les utilisateurs et sur les temporalités

personne_df = get_df_from_csv2(path_cible, file_user)
temporalite_df = get_df_from_csv2(path_cible, file_tempo)

# Creation de la table des faits

liste_onglets = personne_df["onglet"]

for onglet in liste_onglets:
    id_personne = personne_df.query('onglet == "'+ onglet + '"')["id"].iloc[0]
    data_df = get_df_from_csv2(path_src, onglet + ".csv")
    for ligne in data_df.itertuples():
        id_temporalite = temporalite_df.query('date == "'+ ligne[1] + '"')["id"].iloc[0]
        lignes_fait = lignes_fait + str(id_personne) + ';' + str(id_temporalite) + ';' + str(ligne[2]) + '\n'

OutputFile = open(path_cible + file_fait, "w")
OutputFile.write(entete_csv + lignes_fait)
OutputFile.close()