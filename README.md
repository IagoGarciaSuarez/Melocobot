# imonekbot
Bot para el discord de los Come Eucaliptos

_Log:_

    11/11/2019
    El bot se inicia y lee mensajes de todos los canales, pero sólo envía al canal especificado, en este momento es 'bot-commands'.

    13/11/2019
    Saludo de inicio de bot establecido. Cuando el bot se enciende enviará el saludo al canal del bot.
    
    14/11/2019
    Mejorado el comando de inicio del juego. Se añade el argumento np para iniciar la creación del personaje, pero no hay persistencia del mismo.
    Nuevo sistema de archivos. Cuando un usuario inicia el juego, se crea una carpeta dentro del directorio BotPG_Users/ situado en la raíz del programa con su id y que contendrá todos los archivos de sus personajes.
    
    14/11/2019
    Creado directorio BotPG para introducir los archivos para el juego BotPG y creadas las clases relacionadas con el personaje: Character, Weapon, Armor.
    
    15/11/2019
    Implementadas las clases Weapon.py y Quality.py. Se ha realizado una lista de las armas existentes con su daño. Cada arma se crea con una calidad, que será aleatoria y podrá ser Común, Rara, Épica o Legendaria. Según la calidad, habrá un incremento del daño base del arma.
    Algunas armas tienen un efecto especial explicado en la clase Weapon.py. Por ahora sólo la Framedrop y la Croquete tienen un efecto especial.    
    Establecida una funcion para añadir daño bonus para casos de bufos o, en el caso de la Croquete, el efecto pasivo.