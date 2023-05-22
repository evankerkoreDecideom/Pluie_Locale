# -*- coding: utf-8 -*-
"""
Created on Fri May 19 13:09:58 2023

@author: Decideom
"""

import pandas

folder_input = "C:\\GitHub\\Pluie_Locale\\Data\\Sources\\"
folder_output = "C:\\GitHub\\Pluie_Locale\\Data\\Cibles\\"

personne_filename_input = "transco_user_personne.csv"
temporalite_filename_input = "temporalite.csv"
fait_filename_output = "fait.csv"

entete_csv = "id_personne;id_temporalite;valeur\n"
ligne_fait = ""

def get_df_from_csv(path_input, filename_output):
    return pandas.read_csv(path_input + filename_output, sep=';')

personne_df = get_df_from_csv(folder_output, personne_filename_input)
temporalite_df = get_df_from_csv(folder_output, temporalite_filename_input)

liste_onglets = personne_df["onglet"]

for onglet in liste_onglets:
    id_personne = personne_df.query('onglet == "'+ onglet + '"')["id"].iloc[0]
    data_df = get_df_from_csv(folder_input, onglet + ".csv")
    for ligne in data_df.itertuples():
        id_temporalite = temporalite_df.query('date == "'+ ligne[1] + '"')["id"].iloc[0]
        ligne_fait = ligne_fait + str(id_personne) + ';' + str(id_temporalite) + ';' + str(ligne[2]) + '\n'

OutputFile = open(folder_output + fait_filename_output, "w")
OutputFile.write(entete_csv + ligne_fait)
OutputFile.close()