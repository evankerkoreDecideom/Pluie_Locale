import os

def get_filepath_download():
    env_vars = os.environ
    result = ''
    for key, value in env_vars.items():
        if key == 'USERPROFILE':
            return value + '\\Downloads\\'
            exit
    if result == '':
        print('la partie log sera à faire plus tard !')