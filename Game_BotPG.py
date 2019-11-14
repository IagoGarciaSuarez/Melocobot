import os

prefix = '%'

def usrDir(destination):
    return os.path.join('BotPG_Users', f'{destination}')

def gameStart(player_name, user_id):
    pjExiste = [1, f'''
        {player_name} ya tienes un personaje creado. Opciones disponibles:
            ·{prefix}botpg pjlist --> Muestra tus personajes creados.
            ·{prefix}botpg select <personaje> --> Selecciona tu personaje.
            ·{prefix}botpg edit <personaje> --> Editar a tu personaje.
            ·{prefix}botpg reset <personaje> --> Reinicia tu personaje al nivel 0''']

    pjNoExiste = [0, f'Bienvenido a BotPG, {player_name}, para crear un personaje nuevo escribe {prefix}botpg np.']
    user_directory = usrDir(user_id)    
    numOfChars = sum([len(files) for r, d, files in os.walk(usrDir(user_id))])

    if (os.path.isdir(user_directory) and numOfChars):
        return pjExiste

    elif (not os.path.isdir(user_directory)):
        os.mkdir(user_directory)
        return pjNoExiste
    
    else:
        return pjNoExiste

def charCreation(char_name):
    s = 'El personaje se llamará {}.'.format(char_name)
    return s
