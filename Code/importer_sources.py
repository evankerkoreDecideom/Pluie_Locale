# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas

path_googlesheet = "C:\\GitHub\\Pluie_Locale\\Secrets\\GoogleSheetID.txt"
transco_filename = "transco_user_personne.csv"

fait_entete_csv = "id_personne;id_temporalite;valeur\n"
folder_input = "C:\\GitHub\\Pluie_Locale\\Data\\Sources\\"
folder_output = "C:\\GitHub\\Pluie_Locale\\Data\\Cibles\\"

def get_transco_in_df(path_input):
    return pandas.read_csv(path_input, sep=';')

def get_liste_onglet(df):
    return df["onglet"]

def get_secret(path):
    f=open(path, 'r')
    chaine = f.readlines()[0]
    f.close()
    return chaine

googleSheetId = get_secret(path_googlesheet)
    
transco_df = get_transco_in_df(folder_output + transco_filename)

for onglet in get_liste_onglet(transco_df):
    url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
    	googleSheetId,
    	onglet)
    data_df = pandas.read_csv(url)[["date", "valeur"]]
    data_df.to_csv(folder_input + onglet + ".csv", sep=";", index=False)