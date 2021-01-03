class TownHall:
    def __init__(self, lvl: int, giga_weapon=1):
        self.level = lvl
        if self.level >= 12:
            self.giga_weapon = giga_weapon

    def __str__(self):
        return "TH" + (str(self.level) + "-" + str(self.giga_weapon) if self.level >= 12 else str(self.level))
