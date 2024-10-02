import Log.L_Template as LT

class L_Setup(LT.L_Template):

    def __init__(self, folder):
        super().__init__(folder + 'Set Up', False, 'Code / Set_Up')

    def project_imported_succesfully(self):
        self.logger.info('Le projet a été importé avec succès.')

    def folder_temp_log_already_exist(self):
        self.logger.error('Le dossier temporaire des logs existe déjà !')

    def folder_temp_log_unfoundable(self):
        self.logger.error('La création du dossier temporaire des logs rencontre un problème !')

    def import_du_projet_en_echec(self):
        self.logger.error("La commande GIT CLONE ... a échoué !")