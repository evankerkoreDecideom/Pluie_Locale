import Tools.T_Files as TF
import Tools.T_Dataframe as TD
import Tools.T_Environment as TE

class C_SetUp:

    def __init__(self):
        folder = TE.get_filepath_download()
        self.list_parameters_clear =                None
        self.fullpath_downloads_folder =            folder
        self.fullpath_downloads_folder_temp_log =   folder + 'Logs_Pluie_Locale\\'
        self.fullpath_downloaded_file_gs =          folder + 'GoogleSheetID_a5q7y1p9k3.txt'
        self.fullpath_downloaded_file_user =        folder + 'transco_user_personne_a5q7y1p9k3.csv'
        self.fullpath_downloaded_file_github =      folder + 'GitHub_a5q7y1p9k3.txt'
        self.fullpath_downloaded_file_path =        folder + 'Path_a5q7y1p9k3.csv'
        self.fullpath_downloaded_file_setup =       folder + 'Set_Up_a5q7y1p9k3.exe'
        self.hyperlink_github = ''
        self.fullpath_workspace_folder_root = ''
        self.fullpath_workspace_folder_data = ''
        self.fullpath_workspace_folder_cible = ''
        self.fullpath_workspace_folder_source = ''
        self.fullpath_workspace_folder_archive = ''
        self.fullpath_workspace_folder_secrets = ''
        self.fullpath_workspace_folder_logs = ''
        self.fullpath_workspace_file_gs = ''
        self.fullpath_workspace_file_user = ''
        self.fullpath_workspace_file_github = ''
        self.fullpath_workspace_file_path = ''
        self.fullpath_workspace_file_setup = ''
        self.namefile_log_setup = ''

    #  1.   On vérifie que les fichiers sont bien présents dans le dossier téléchargement

    def all_files_downloaded_are_here(self):
        return (TF.fichier_present(self.fullpath_downloaded_file_gs) and 
                TF.fichier_present(self.fullpath_downloaded_file_user) and
                TF.fichier_present(self.fullpath_downloaded_file_github) and
                TF.fichier_present(self.fullpath_downloaded_file_path) and
                TF.fichier_present(self.fullpath_downloaded_file_setup) )
    
    #  2.   On créé le dossier temporaire pour les logs le temps de la mise en place du projet
    
    def add_folder_temporary_log(self):
        TF.creation_dossier(self.fullpath_downloads_folder_temp_log)

    #  3.   Récupération des données de paramétrage

    def set_list_parameters_clear(self): # df : dataframe
        dataframe_raw = TD.get_df_from_csv(self.fullpath_downloaded_file_path)
        self.list_parameters_clear = TD.get_df_explicit(dataframe_raw)

    #  4.   Affectation des données de paramétrage aux attribut de l'objet

    def set_fullpath_workspace_folder_root(self):
        self.fullpath_workspace_folder_root = TD.get_value_from_df(self.list_parameters_clear, "__GITHUB__")

    def set_hyperlink_github(self):
        self.hyperlink_github = TD.get_value_from_df(self.list_parameters_clear, "v_link_github")

    def set_namefile_log_setup(self):
        self.namefile_log_setup = TD.get_value_from_df(self.list_parameters_clear, "f_log_su")

    def set_fullpath_workspace_folder_data(self):
        self.fullpath_workspace_folder_data = TD.get_value_from_df(self.list_parameters_clear, "p_data")

    def set_fullpath_workspace_folder_cible(self):
        self.fullpath_workspace_folder_cible = TD.get_value_from_df(self.list_parameters_clear, "p_cibles")

    def set_fullpath_workspace_folder_source(self):
        self.fullpath_workspace_folder_source = TD.get_value_from_df(self.list_parameters_clear, "p_sources")

    def set_fullpath_workspace_folder_archive(self):
        self.fullpath_workspace_folder_archive = TD.get_value_from_df(self.list_parameters_clear, "p_archives")

    def set_fullpath_workspace_folder_secrets(self):
        self.fullpath_workspace_folder_secrets = TD.get_value_from_df(self.list_parameters_clear, "p_secrets")

    def set_fullpath_workspace_folder_logs(self):
        self.fullpath_workspace_folder_logs = TD.get_value_from_df(self.list_parameters_clear, "p_logs")

    def set_fullpath_workspace_file_gs(self):
        self.fullpath_workspace_file_gs = self.fullpath_workspace_folder_secrets + TD.get_value_from_df(self.list_parameters_clear, "f_GS_ID")

    def set_fullpath_workspace_file_user(self):
        self.fullpath_workspace_file_user = self.fullpath_workspace_folder_cible + TD.get_value_from_df(self.list_parameters_clear, "f_user")

    def set_fullpath_workspace_file_github(self):
        self.fullpath_workspace_file_github = self.fullpath_workspace_folder_secrets + TD.get_value_from_df(self.list_parameters_clear, "f_github")

    def set_fullpath_workspace_file_path(self):
        self.fullpath_workspace_file_path = self.fullpath_workspace_folder_secrets + TD.get_value_from_df(self.list_parameters_clear, "f_path")

    def set_fullpath_workspace_file_setup(self):
        self.fullpath_workspace_file_setup = TD.get_value_from_df(self.list_parameters_clear, "p_dist") + TD.get_value_from_df(self.list_parameters_clear, "f_set_up")

    #  5. 

    def cloner_projet_depuis_github(self):
        self.set_hyperlink_github()
        TF.creation_dossier(self.fullpath_workspace_folder_root)
        TF.definir_dossier_actif(self.fullpath_workspace_folder_root)
        TF.cloner_projet_via_lien(self.hyperlink_github)

    def set_fullpath_all_folders_workspace(self):
        self.set_fullpath_workspace_folder_data()
        self.set_fullpath_workspace_folder_cible()
        self.set_fullpath_workspace_folder_source()
        self.set_fullpath_workspace_folder_archive()
        self.set_fullpath_workspace_folder_secrets()
        self.set_fullpath_workspace_folder_logs()

    def creation_dossiers_workspace(self):
        TF.creation_dossier(self.fullpath_workspace_folder_data)
        TF.creation_dossier(self.fullpath_workspace_folder_cible)
        TF.creation_dossier(self.fullpath_workspace_folder_source)
        TF.creation_dossier(self.fullpath_workspace_folder_archive)
        TF.creation_dossier(self.fullpath_workspace_folder_secrets)
        TF.creation_dossier(self.fullpath_workspace_folder_logs)

    def set_fullpath_all_files_workspace(self):
        self.set_fullpath_workspace_file_gs()
        self.set_fullpath_workspace_file_user()
        self.set_fullpath_workspace_file_github()
        self.set_fullpath_workspace_file_path()
        self.set_fullpath_workspace_file_setup()

    def deplacer_et_renommer_fichiers_downloads_vers_workspace(self):
        TF.deplacer_et_renommer_fichiers(self.fullpath_downloaded_file_gs, self.fullpath_workspace_file_gs)
        TF.deplacer_et_renommer_fichiers(self.fullpath_downloaded_file_user, self.fullpath_workspace_file_user)
        TF.deplacer_et_renommer_fichiers(self.fullpath_downloaded_file_github, self.fullpath_workspace_file_github)
        TF.deplacer_et_renommer_fichiers(self.fullpath_downloaded_file_path, self.fullpath_workspace_file_path)
        TF.deplacer_et_renommer_fichiers(self.fullpath_downloaded_file_setup, self.fullpath_workspace_file_setup)

    def transferer_fichiers_logs_temporaire_vers_workspace(self):
        TF.deplacer_fichiers(self.fullpath_downloads_folder_temp_log, self.fullpath_workspace_folder_logs, self.namefile_log_setup)

    def supprimer_dossier_temporaire_log(self):
        TF.supprimer_dossier_vide(self.fullpath_downloads_folder_temp_log)

    def afficher(self):
        print("---------------------------------------------------------------------------------")
        print(self.list_parameters_clear)
        print('fullpath_downloads_folder : ' + self.fullpath_downloads_folder)
        print('fullpath_downloaded_file_gs : '+ self.fullpath_downloaded_file_gs)
        print('fullpath_downloaded_file_user : '+ self.fullpath_downloaded_file_user)
        print('fullpath_downloaded_file_github : '+ self.fullpath_downloaded_file_github)
        print('fullpath_downloaded_file_path : '+ self.fullpath_downloaded_file_path)
        print('fullpath_downloaded_file_setup : '+ self.fullpath_downloaded_file_setup)
        print('hyperlink_github : '+ self.hyperlink_github)
        print('fullpath_workspace_folder_root : '+ self.fullpath_workspace_folder_root)
        print('fullpath_workspace_folder_data : '+ self.fullpath_workspace_folder_data)
        print('fullpath_workspace_folder_cible : '+ self.fullpath_workspace_folder_cible)
        print('fullpath_workspace_folder_source : '+ self.fullpath_workspace_folder_source)
        print('fullpath_workspace_folder_archive : '+ self.fullpath_workspace_folder_archive)
        print('fullpath_workspace_folder_secrets : '+ self.fullpath_workspace_folder_secrets)
        print('fullpath_workspace_file_gs : '+ self.fullpath_workspace_file_gs)
        print('fullpath_workspace_file_user : '+ self.fullpath_workspace_file_user)
        print('fullpath_workspace_file_github : '+ self.fullpath_workspace_file_github)
        print('fullpath_workspace_file_path : '+ self.fullpath_workspace_file_path)
        print('fullpath_workspace_file_setup : '+ self.fullpath_workspace_file_setup)
        print("---------------------------------------------------------------------------------")