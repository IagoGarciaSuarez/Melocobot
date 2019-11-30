class Character():
    '''
    Las estadísticas contemplan:
    - HP
    '''
    def __init__(self, name, lvl = [0, 0], money = 0, stats = [0], weapon = None, armor = None):
        self.name = name
        self.lvl = lvl
        self.money = money
        self.stats = stats
        self.weapon = weapon
        self.armor = armor

    def __str__(self):
        charInfo = [self.name, self.lvl, self.money, self.stats, self.weapon, self.armor]
        return charInfo