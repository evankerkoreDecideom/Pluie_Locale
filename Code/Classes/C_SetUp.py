from ..Tools import T_Files as TF
from ..Tools import T_Dataframe as TD
from ..Tools import T_Environment as TE

class C_SetUp:

    def __init__(self, filename_path):
        self.list_parameters_csv = filename_path
        self.list_parameters_clear = None
        self.fullpath_downloaded_gs = ''
        self.fullpath_downloaded_user = ''
        self.fullpath_downloaded_github = ''
        self.fullpath_downloaded_path = ''
        self.fullpath_downloaded_setup = ''
        self.hyperlink_github = ''
        self.fullpath_workspace_root = ''
        self.fullpath_workspace_data = ''
        self.fullpath_workspace_cible = ''
        self.fullpath_workspace_source = ''
        self.fullpath_workspace_archive = ''
        self.fullpath_workspace_secrets = ''

    def set_list_parameters_clear(self):
        dataframe_raw = TD.get_df_from_csv(self.list_parameters_csv)
        self.list_parameters_clear = TD.get_df_explicit(dataframe_raw)

    def set_fullpath_downloaded_gs(self):
        self.fullpath_downloaded_gs = TE.get_filepath_download + "GoogleSheetID_a5q7y1p9k3.txt"

    def creation_dossiers_workspace(self):
        TF.creation_dossier(self.fullpath_workspace_data)
        TF.creation_dossier(self.fullpath_workspace_cible)
        TF.creation_dossier(self.fullpath_workspace_source)
        TF.creation_dossier(self.fullpath_workspace_archive)
        TF.creation_dossier(self.fullpath_workspace_secrets)