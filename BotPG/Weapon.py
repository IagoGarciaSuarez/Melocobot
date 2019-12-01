from BotPG import Quality

class Weapon:
    dmgDict = {
        "Croquete": 0,
        "Arma de hierro": 1,
        "Masamune": 2,
        "Sierrita": 2,
        "Zorrita": 3,
        "Bicaya": 5,
        "Takumi": 6,
        "Framedrop": 8,
        "Boyuguei": 9,
        "Leyenevedaya": 10
    }

    '''EFECTOS DE ARMA LEGENDARIA:
        Croquetation: Los enemigos no soportan a Croquete. Tienen flashbacks del día del nacimiento del puto niño retrasado y sienten una punzada en el corazón.
                Cada turno tiene una probabilidad del 30% de aumentar su daño base en 20.
        Pierdoframeslpm: El pibe enemigo pierde frames y no logra realizar su ataque correctamente.
                Posibilidad del 20% de no recibir daño del ataque enemigo.'''

    effectValue = {
        "Croquete": 20,
        "Framedrop": 20
    }

    def __init__(self, name, quality=Quality.Quality()):
        self._name = name
        self._baseDmg = self.dmgDict[name]
        if name == 'Arma de hierro':
            self._quality = "Común"
        else:
            self._quality = quality
        self._bonusDmg = 0

    def getName(self):
        return self._name

    def getQuality(self):
        return self._quality

    def addDmg(self, dmg):
        self._bonusDmg += dmg

    def getDamage(self):
        damage = self._baseDmg + self._baseDmg*self._quality.getQualityBonus() + self._bonusDmg
        if (self.getName == "Croquete"):
            damage += self.effectValue["Croquete"] + self.effectValue["Croquete"]*self._quality.getQualityBonus
        return damage