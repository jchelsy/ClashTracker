from ...data import defense
from src.content.default import BaseBuilding


class Cannon(BaseBuilding):
    def __init__(self, level, gear_up=False):
        super().__init__(level)
        self.isGearedUp = gear_up

    def __str__(self):
        return "cannon"

    def setDesc(self):
        return "CANNON!"

    def setHP(self):
        return defense.CANNON[self.lvl]['hitpoints']

    def setBuildCost(self):
        return defense.CANNON[self.lvl + 1]['build_cost']

    def setBuildTime(self):
        return defense.CANNON[self.lvl + 1]['build_time']

    def setDPS(self):
        return defense.CANNON[self.lvl]['dmg_per_sec'], defense.CANNON[self.lvl]['dmg_per_shot']
