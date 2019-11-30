from BotPG import Quality

class Armor:
    armorDict = {
        "Armadura de hierro": 1,
        "Esmegma": 2,
        "Chisito": 3,
        "Otiak": 4,
        "Ipsirk": 4,
        "Alaok": 5,
        "Asupdu": 6,
        "Uwumor": 8,
        "Ceraldelfin": 9,
        "Plátano": 10
    }
    

    def __init__(self, name):
        self._name = name
        self._baseArmor = armorDict[name]
        self._quality = Quality(Quality.qualityDict[name])
        self._bonusArmor = 0

    def addArmor(self, armor):
        self._bonusArmor += Armor

    def getArmor(self):
        armor = self._baseArmor + self.getArmor*self._quality.getQualityDmg() + self._bonusArmor
        return armor

    def getName(self):
        return self._name

    def getDefense(self):
        return self._defense