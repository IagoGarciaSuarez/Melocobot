import os

def bienvenida(player_name):
    if (os.path.isdir("Koala")):
        return ('{} ha entrado en rpgbot. Elige qué personaje quieres utilizar:'.format(player_name))
    else:
        os.mkdir("Koala")
        return ('¿Tu primera vez? Vamos a crear tu personaje:')

def creacionPersonaje(character_name):
    f = open("{}.txt".format(character_name))