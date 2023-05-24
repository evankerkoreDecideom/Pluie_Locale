# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas
import shutil
import datetime

path_googlesheet = "C:\\GitHub\\Pluie_Locale\\Secrets\\GoogleSheetID.txt"
transco_filename = "transco_user_personne.csv"

fait_entete_csv = "id_personne;id_temporalite;valeur\n"
folder_input = "C:\\GitHub\\Pluie_Locale\\Data\\Sources\\"
archive_folder_output = "C:\\GitHub\\Pluie_Locale\\Data\\Sources\\Archives\\"
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

def copy_and_archive(folder_in, folder_out, name):
    file_archived = name + "_" + datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + ".csv"
    file_in = folder_in + name + ".csv"
    file_out = folder_out + file_archived
    shutil.copy(file_in , file_out)

googleSheetId = get_secret(path_googlesheet)
    
transco_df = get_transco_in_df(folder_output + transco_filename)

for onglet in get_liste_onglet(transco_df):
    url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
    	googleSheetId,
    	onglet)
    data_df = pandas.read_csv(url)[["date", "valeur"]]
    data_df.to_csv(folder_input + onglet + ".csv", sep=";", index=False)
    copy_and_archive(folder_input, archive_folder_output, onglet)