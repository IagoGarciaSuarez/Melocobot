from BotPG import Weapon
from BotPG import Armor

class Character:
    '''
    Las estadísticas contemplan:
    - HP
    '''
    def __init__(self, name, lvl = [0, 0], money = 0, stats = [0], weapon = Weapon.Weapon("Arma de hierro"), armor = Armor.Armor("Armadura de hierro")):
        self.name = name
        self.lvl = lvl
        self.money = money
        self.stats = stats
        self.weapon = weapon
        self.armor = armor

    def __str__(self):
        charInfo = "constructor del personaje"
        #"{\"Level\": [{0}, {1}],\n\"Money\": {2},\n\"Stats\": [{3}],\n\"Weapon\":[{4}, {5}],\n\"Armor\":[{6}, {7}]}".format(self.name, self.lvl[0], 
        #self.lvl[1], self.money, self.stats[0], "nombre arma", "nombre calidad arma", "self.armor.getName()", "self.armor.getQuality().getName()")
        return charInfo