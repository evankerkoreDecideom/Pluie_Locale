# -*- coding: utf-8 -*-
"""
Created on Thu May 25 09:09:55 2023

@author: Decideom
"""

import Classes.C_SetUp as CS
import Log.L_Setup as LS

# Exécution de l'exécutable

'''
temporalite_exe = get_value_from_df(df_path_explicit, "p_dist") + get_value_from_df(df_path_explicit, "f_temporalite_exe")
os.system(temporalite_exe)
''' 

def main():
    setup = CS.C_SetUp()
    # 1
    if (setup.all_files_downloaded_are_here()):

        # 2
        setup.add_folder_temporary_log()
        log_setup = LS.L_Setup(setup.fullpath_downloads_folder_temp_log)

        # 3
        setup.set_list_parameters_clear()

        
        setup.set_fullpath_workspace_folder_root()
        try:
            setup.cloner_projet_depuis_github()
            log_setup.project_imported_succesfully()
        except FileExistsError:
            log_setup.folder_temp_log_already_exist()
            exit()
        except FileNotFoundError:
            log_setup.folder_temp_log_unfoundable()
            exit()
        except Exception:
            log_setup.import_du_projet_en_echec()
            exit()
        setup.set_fullpath_all_folders_workspace()
        setup.creation_dossiers_workspace()
        setup.set_fullpath_all_files_workspace()
        setup.deplacer_et_renommer_fichiers_downloads_vers_workspace()
        
main()