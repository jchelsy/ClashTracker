class BaseBuilding:
    def __init__(self, level, defense=True):
        self.lvl = level
        self.hp = self.setHP()
        self.desc = self.setDesc()
        self.nextUpgradeCost = self.setBuildCost()
        self.nextUpgradeDuration = self.setBuildTime()
        if defense:
            self.dmg_per_sec, self.dmg_per_shot = self.setDPS()

    def setDesc(self):
        raise NotImplementedError

    def setHP(self):
        raise NotImplementedError

    def setBuildCost(self):
        raise NotImplementedError

    def setBuildTime(self):
        raise NotImplementedError

    def setDPS(self):
        raise
