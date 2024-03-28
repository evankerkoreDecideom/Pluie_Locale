# -*- coding: utf-8 -*-
"""
Created on Fri May 19 09:36:08 2023

@author: Decideom
"""

import Tools.T_Dataframe as t_df
import Classes.C_SetUp as c_su
import pandas
import datetime as dt
from pathlib import Path
import os

# =========================================
#   Manipulation des données de type date
# =========================================

def get_date_inc(date, inc):
    return date + dt.timedelta(inc)

def get_date_format(date):
    return str(date.strftime('%d/%m/%Y'))[0:10]

def get_year(date):
    return str(date.year)

def get_month(date):
    return str(date.month)

def get_day(date):
    return str(date.day)

# ================================
#   Construction du fichiers CSV
# ================================

def ligne(date, inc):
    d = get_date_inc(date, inc)
    return str(inc) + ';'  + get_date_format(d) + ';' + get_year(d) + ';' + get_month(d) + ';' + get_day(d) + '\n'

def get_corps_in_str(date_debut, nb_annee):
    corps_csv = ""
    for i in range(365 * nb_annee):
        corps_csv = corps_csv + ligne(date_debut, i)
    return corps_csv

def get_csv_in_str(date_debut, nb_annee):
    return entete_csv + get_corps_in_str(date_debut, nb_annee)

def main(date_debut, path_output, nb_annee):
    OutputFile = open(path_output, "w")
    OutputFile.write(get_csv_in_str(date_debut, nb_annee))
    OutputFile.close()

# Initialisation des variables

entete_csv = "id;date;annee;mois;jour\n"
nb_annee = 20
date_debut = dt.datetime(2019,1,1,0,0,0)

# Constitustion du chemin du fichier CSV

df_path = t_df.get_df_from_csv(os.path.abspath("Path.csv"))
print(df_path)
print('')
df_path_explicit = t_df.get_df_explicit(df_path)
print(df_path_explicit)
print('')
path_csv_output = t_df.get_value_from_df(df_path_explicit, "p_cibles")  + t_df.get_value_from_df(df_path_explicit, "f_temporalite")
print(path_csv_output)
print('')

# Création du fichier CSV
    
#main(date_debut, path_csv_output, nb_annee)