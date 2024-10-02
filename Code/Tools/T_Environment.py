import os

def get_filepath_download():
    try:
        return os.environ['USERPROFILE'] + '\\Downloads\\'
    except KeyError:
        print("Cette variable d'environnement n'est pas référencé !")