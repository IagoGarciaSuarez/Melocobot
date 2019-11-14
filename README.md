# imonekbot
Bot para el discord de los Come Eucaliptos

Log:
    11/11/2019 -    El bot se inicia y lee mensajes de todos los canales, pero sólo envía al canal especificado, en este momento es 'bot-commands'.
    13/11/2019 -    Saludo de inicio de bot establecido. Cuando el bot se enciende enviará el saludo al canal del bot.
    14/11/2019 -    Mejorado el comando de inicio del juego. Se añade el argumento np para iniciar la creación del personaje, pero no hay persistencia del mismo.
                    Nuevo sistema de archivos. Cuando un usuario inicia el juego, se crea una carpeta dentro del directorio BotPG_Users/ situado en la raíz del programa con su id y que contendrá todos los archivos de sus personajes.