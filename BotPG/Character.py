class Character():
    def __init__(self, name):
        self.name = name
        self.lvl = [1, 0]
        self.money = 0
        self.stats = []
        self.currentWeapon = None
        self.currentArmor = None