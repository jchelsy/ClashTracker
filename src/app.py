from src import content
from src import data


class Control:
    def __init__(self, user, townhall_level):
        self.name = user
        self.townhall = content.TownHall(townhall_level)
        # Resources
        self.gold_mines = []
        self.elixir_collectors = []
        self.dark_elixir_drills = []
        self.gold_storages = []
        self.elixir_storages = []
        self.dark_elixir_storages = []
        self.clan_castle = None
        # Army
        self.army_camps = []
        self.barracks = []
        self.dark_barracks = []
        self.laboratory = None
        self.spell_factory = None
        self.dark_spell_factory = None
        self.workshop = None
        # Defenses
        self.cannons = []
        self.archer_towers = []
        self.mortars = []
        self.air_defenses = []
        self.wizard_towers = []
        self.air_sweepers = []
        self.hidden_teslas = []
        self.bomb_towers = []
        self.xbows = []
        self.inferno_towers = []
        self.eagle_artillery = None
        self.giga_tesla = None
        self.giga_inferno = None
        self.scattershots = []
        # Walls
        self.walls = []
        # Traps
        self.bombs = []
        self.spring_traps = []
        self.air_bombs = []
        self.giant_bombs = []
        self.seeking_air_mines = []
        self.skeleton_traps = []
        self.tornado_trap = None

    def initialize(self):
        self.cannons.append(content.Cannon(12))
        self.cannons.append(content.Cannon(12))
        self.cannons.append(content.Cannon(12))
        self.cannons.append(content.Cannon(13))
        self.cannons.append(content.Cannon(13))

    def printDefenseData(self, item):
        items = eval('self.' + item)
        max_num = data.TOWNHALL[self.townhall.level]['buildings']['defense'][items[0].__str__()][0]
        if items:
            print(item.capitalize() + ":")
            for i in range(len(items)):
                # print("(%d/%d)" % (i + 1, max_num))
                print("(%d/%d) lv.%-6d %-10d" % (i + 1, max_num, items[i].lvl, items[i].nextUpgradeCost))

            if len(items) < max_num:
                not_built = max_num - len(items)
                for i in range(not_built):
                    print("(%d/%d) lv.%-6s %-10d" % (i + len(items) + 1, max_num, '---', data.CANNON[1]['build_cost']))

    def print(self) -> None:
        user = "Jchelsy (TH" + str(self.townhall.level) + ")"
        print("=" * (20 if len(user) <= 20 else len(user)))
        print(user.center(20))
        print("=" * (20 if len(user) <= 20 else len(user)))
        print()
        # Defenses
        self.printDefenseData("cannons")

        # # Defenses
        # print("Defenses".center(20))
        # print(("=" * 10).center(20))
        # print("Cannons:")
        # print("")
        #
        # print("Archer Towers")
        # print("Mortars")
        # print("Air Defenses")
        # print("Wizard Towers")
        # print("Air Sweepers")
        # print("Hidden Teslas")
        # print("Bomb Towers")
        # print("X-Bows")
        # print("Inferno Towers")
        # print("Eagle Artillery")
        # print("Scattershots")
        # # Traps
        # print("Bombs")
        # print("Spring Traps")
        # print("Air Bombs")
        # print("Giant Bombs")
        # print("Seeking Air Bombs")
        # print("Skeleton Traps")
        # print("Tornado Trap")
        # # Army
        # print("Army Camps")
        # print("Barracks")
        # print("Dark Barracks")
        # print("Laboratory")
        # print("Spell Factory")
        # print("Dark Spell Factory")
        # print("Workshop")
        # # Resources
        # print("Gold Mines")
        # print("Elixir Collectors")
        # print("Dark Elixir Drills")
        # print("Gold Storages")
        # print("Elixir Storages")
        # print("Dark Elixir Storages")
        # print("Clan Castle")
        # # Heroes
        # print("Barbarian King")
        # print("Archer Queen")
        # print("Grand Warden")
        # print("Royal Champion")
        # # Troop Upgrades
        # print("Barbarian")
        # print("Archer")
        # print("Giant")
        # print("Goblin")
        # print("Wall Breaker")
        # print("Balloon")
        # print("Wizard")
        # print("Healer")
        # print("Dragon")
        # print("P.E.K.K.A")
        # print("Baby Dragon")
        # print("Miner")
        # print("Electro Dragon")
        # print("Yeti")
        # # Dark Troop Upgrades
        # print("Minion")
        # print("Hog Rider")
        # print("Valkyrie")
        # print("Golem")
        # print("Witch")
        # print("Lava Hound")
        # print("Bowler")
        # print("Ice Golem")
        # print("Headhunter")
        # # Spells
        # print("Lightning Spell")
        # print("Healing Spell")
        # print("Rage Spell")
        # print("Jump Spell")
        # print("Freeze Spell")
        # print("Clone Spell")
        # print("Invisibility Spell")
        # # Dark Spells
        # print("Poison Spell")
        # print("Earthquake Spell")
        # print("Haste Spell")
        # print("Skeleton Spell")
        # print("Bat Spell")
        # # Siege Machines
        # print("Wall Wrecker")
        # print("Battle Blimp")
        # print("Stone Slammer")
        # print("Siege Barracks")
        # print("Log Launcher")
        # # Walls
        # print("Walls")
