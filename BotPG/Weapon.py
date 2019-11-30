from Quality import Quality

class Weapon():
    dmgDict = {
        "Croquete": 0
        "Arma de hierro": 1
        "Masamune": 2
        "Sierrita": 2**
        "Zorrita": 3
        "Bicaya": 5
        "Takumi": 6
        "Framedrop": 8
        "Boyuguei": 9
        "Leyenevedaya": 10
    }

    '''EFECTOS DE ARMA LEGENDARIA:
        Croquetation: Los enemigos no soportan a Croquete. Tienen flashbacks del día del nacimiento del puto niño retrasado y sienten una punzada en el corazón.
                Cada turno tiene una probabilidad del 30% de aumentar su daño base en 20.
        Pierdoframeslpm: El pibe enemigo pierde frames y no logra realizar su ataque correctamente.
                Posibilidad del 20% de no recibir daño del ataque enemigo.'''

    effectValue = {
        "Croquete": 20
        "Framedrop": 20
    }

    def __init__(self, name):
        self._name = name
        self._baseDmg = dmgDict[name]
        self._quality = Quality(qualityDict[name])
        self._bonusDmg = 0

    def getName():
        return self._name

    def addDmg(dmg):
        self._bonusDmg += dmg

    def getDamage(self):
        damage = self._baseDmg + self._baseDmg*self._quality.getQualityDmg() + self._bonusDmg
        if (self.getName == "Croquete"):
            damage += effectValue["Croquete"] + effectValue["Croquete"]*self._quality.getQualityDmg
        return damage