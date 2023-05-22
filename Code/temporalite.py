# -*- coding: utf-8 -*-
"""
Created on Fri May 19 09:36:08 2023

@author: Decideom
"""

from datetime import datetime, timedelta

entete_csv = "id;date;annee;mois;jour\n"
nb_annee = 20
date_debut = datetime(2019,1,1,0,0,0)
path_output = "C:\\GitHub\\Data\\Cibles\\temporalite.csv"

def get_date_inc(date, inc):
    return date + timedelta(inc)

def get_date_format(date):
    return str(date.strftime('%d/%m/%Y'))[0:10]

def get_year(date):
    return str(date.year)

def get_month(date):
    return str(date.month)

def get_day(date):
    return str(date.day)

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
    
main(date_debut, path_output, nb_annee)