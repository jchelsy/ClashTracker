TOWNHALL = {
    1: {
        'hitpoints': 450,
        'build_cost': 0,
        'build_time': None,
        'storage_capacity': (1000, 1000, 0),  # (Gold, Elixir, Dark Elixir)
        'buildings': {  # (number available, maximum level)
            'resource': {
                'gold_mine': (1, 2),
                'elixir_collector': (1, 2),
                'dark_elixir_drill': (),
                'gold_storage': (1, 1),
                'elixir_storage': (1, 1),
                'dark_elixir_storage': (),
                'clan_castle': ()
            },
            'army': {
                'army_camp': (1, 1),
                'barracks': (1, 3),
                'dark_barracks': (),
                'laboratory': (),
                'spell_factory': (),
                'dark_spell_factory': (),
                'workshop': ()
            },
            'defense': {
                'cannon': (2, 2),
                'archer_tower': (),
                'mortar': (),
                'air_defense': (),
                'wizard_tower': (),
                'air_sweeper': (),
                'hidden_tesla': (),
                'bomb_tower': (),
                'xbow': (),
                'inferno_tower': (),
                'eagle_artillery': (),
                'giga_tesla': (),
                'giga_inferno': (),
                'scattershot': (),
                'walls': ()
            },
            'traps': {
                'bomb': (),
                'spring_trap': (),
                'air_bomb': (),
                'giant_bomb': (),
                'seeking_air_mine': (),
                'skeleton_trap': (),
                'tornado_trap': ()
            }
        }
    },
    2: {
        'hitpoints': 1600,
        'build_cost': 1000,
        'build_time': '10s',
        'storage_capacity': (1000, 1000, 0),  # (Gold, Elixir, Dark Elixir)
        'buildings': {  # (number available, maximum level)
            'resource': {
                'gold_mine': (2, 4),
                'elixir_collector': (2, 4),
                'dark_elixir_drill': (),
                'gold_storage': (1, 3),
                'elixir_storage': (1, 3),
                'dark_elixir_storage': (),
                'clan_castle': (1, 1)  # Insufficient storage at TH2, but buying extra gold can unlock
            },
            'army': {
                'army_camp': (1, 2),
                'barracks': (2, 4),
                'dark_barracks': (),
                'laboratory': (),
                'spell_factory': (),
                'dark_spell_factory': (),
                'workshop': ()
            },
            'defense': {
                'cannon': (2, 3),
                'archer_tower': (1, 2),
                'mortar': (),
                'air_defense': (),
                'wizard_tower': (),
                'air_sweeper': (),
                'hidden_tesla': (),
                'bomb_tower': (),
                'xbow': (),
                'inferno_tower': (),
                'eagle_artillery': (),
                'giga_tesla': (),
                'giga_inferno': (),
                'scattershot': (),
                'walls': (25, 2)
            },
            'traps': {
                'bomb': (),
                'spring_trap': (),
                'air_bomb': (),
                'giant_bomb': (),
                'seeking_air_mine': (),
                'skeleton_trap': (),
                'tornado_trap': ()
            }
        }
    },
    3: {
        'hitpoints': 1850,
        'build_cost': 4000,
        'build_time': '2h',
        'storage_capacity': (10000, 10000, 0),  # (Gold, Elixir, Dark Elixir)
        'buildings': {  # (number available, maximum level)
            'resource': {
                'gold_mine': (3, 6),
                'elixir_collector': (3, 6),
                'dark_elixir_drill': (),
                'gold_storage': (2, 6),
                'elixir_storage': (2, 6),
                'dark_elixir_storage': (),
                'clan_castle': (1, 1)
            },
            'army': {
                'army_camp': (2, 3),
                'barracks': (2, 5),
                'dark_barracks': (),
                'laboratory': (1, 1),
                'spell_factory': (),
                'dark_spell_factory': (),
                'workshop': ()
            },
            'defense': {
                'cannon': (2, 4),
                'archer_tower': (1, 3),
                'mortar': (1, 1),
                'air_defense': (),
                'wizard_tower': (),
                'air_sweeper': (),
                'hidden_tesla': (),
                'bomb_tower': (),
                'xbow': (),
                'inferno_tower': (),
                'eagle_artillery': (),
                'giga_tesla': (),
                'giga_inferno': (),
                'scattershot': (),
                'walls': (50, 3)
            },
            'traps': {
                'bomb': (2, 2),
                'spring_trap': (),
                'air_bomb': (),
                'giant_bomb': (),
                'seeking_air_mine': (),
                'skeleton_trap': (),
                'tornado_trap': ()
            }
        }
    },
    4: {
        'hitpoints': 2100,
        'build_cost': 25000,
        'build_time': '8h',
        'storage_capacity': (50000, 50000, 0),  # (Gold, Elixir, Dark Elixir)
        'buildings': {  # (number available, maximum level)
            'resource': {
                'gold_mine': (4, 8),
                'elixir_collector': (4, 8),
                'dark_elixir_drill': (),
                'gold_storage': (2, 8),
                'elixir_storage': (2, 8),
                'dark_elixir_storage': (),
                'clan_castle': (1, 2)
            },
            'army': {
                'army_camp': (2, 4),
                'barracks': (3, 6),
                'dark_barracks': (),
                'laboratory': (1, 2),
                'spell_factory': (),
                'dark_spell_factory': (),
                'workshop': ()
            },
            'defense': {
                'cannon': (2, 5),
                'archer_tower': (2, 4),
                'mortar': (1, 2),
                'air_defense': (1, 2),
                'wizard_tower': (),
                'air_sweeper': (),
                'hidden_tesla': (),
                'bomb_tower': (),
                'xbow': (),
                'inferno_tower': (),
                'eagle_artillery': (),
                'giga_tesla': (),
                'giga_inferno': (),
                'scattershot': (),
                'walls': (75, 4)
            },
            'traps': {
                'bomb': (2, 2),
                'spring_trap': (2, 1),
                'air_bomb': (),
                'giant_bomb': (),
                'seeking_air_mine': (),
                'skeleton_trap': (),
                'tornado_trap': ()
            }
        }
    },
    5: {
        'hitpoints': 2400,
        'build_cost': 150000,
        'build_time': '12h',
        'storage_capacity': (100000, 100000, 0),  # (Gold, Elixir, Dark Elixir)
        'buildings': {  # (number available, maximum level)
            'resource': {
                'gold_mine': (5, 10),
                'elixir_collector': (5, 10),
                'dark_elixir_drill': (),
                'gold_storage': (2, 9),
                'elixir_storage': (2, 9),
                'dark_elixir_storage': (),
                'clan_castle': (1, 2)
            },
            'army': {
                'army_camp': (3, 5),
                'barracks': (3, 7),
                'dark_barracks': (),
                'laboratory': (1, 3),
                'spell_factory': (1, 1),
                'dark_spell_factory': (),
                'workshop': ()
            },
            'defense': {
                'cannon': (3, 6),
                'archer_tower': (3, 6),
                'mortar': (1, 3),
                'air_defense': (1, 3),
                'wizard_tower': (1, 2),
                'air_sweeper': (),
                'hidden_tesla': (),
                'bomb_tower': (),
                'xbow': (),
                'inferno_tower': (),
                'eagle_artillery': (),
                'giga_tesla': (),
                'giga_inferno': (),
                'scattershot': (),
                'walls': (100, 5)
            },
            'traps': {
                'bomb': (4, 3),
                'spring_trap': (2, 1),
                'air_bomb': (2, 2),
                'giant_bomb': (),
                'seeking_air_mine': (),
                'skeleton_trap': (),
                'tornado_trap': ()
            }
        }
    },
    6: {
        'hitpoints': 2800,
        'build_cost': 750000,
        'build_time': '1d',
        'storage_capacity': (300000, 300000, 0),  # (Gold, Elixir, Dark Elixir)
        'buildings': {  # (number available, maximum level)
            'resource': {
                'gold_mine': (6, 10),
                'elixir_collector': (6, 10),
                'dark_elixir_drill': (),
                'gold_storage': (2, 10),
                'elixir_storage': (2, 10),
                'dark_elixir_storage': (),
                'clan_castle': (1, 3)
            },
            'army': {
                'army_camp': (3, 6),
                'barracks': (3, 8),
                'dark_barracks': (),
                'laboratory': (1, 4),
                'spell_factory': (1, 2),
                'dark_spell_factory': (),
                'workshop': ()
            },
            'defense': {
                'cannon': (3, 7),
                'archer_tower': (3, 7),
                'mortar': (2, 4),
                'air_defense': (2, 4),
                'wizard_tower': (2, 3),
                'air_sweeper': (1, 2),
                'hidden_tesla': (),
                'bomb_tower': (),
                'xbow': (),
                'inferno_tower': (),
                'eagle_artillery': (),
                'giga_tesla': (),
                'giga_inferno': (),
                'scattershot': (),
                'walls': (125, 6)
            },
            'traps': {
                'bomb': (4, 3),
                'spring_trap': (4, 1),
                'air_bomb': (2, 2),
                'giant_bomb': (1, 2),
                'seeking_air_mine': (),
                'skeleton_trap': (),
                'tornado_trap': ()
            }
        }
    },
    7: {
        'hitpoints': 3300,
        'build_cost': 1200000,
        'build_time': '2d',
        'storage_capacity': (500000, 500000, 2500),  # (Gold, Elixir, Dark Elixir)
        'buildings': {  # (number available, maximum level)
            'resource': {
                'gold_mine': (6, 11),
                'elixir_collector': (6, 11),
                'dark_elixir_drill': (1, 3),
                'gold_storage': (2, 11),
                'elixir_storage': (2, 11),
                'dark_elixir_storage': (1, 2),
                'clan_castle': (1, 3)
            },
            'army': {
                'army_camp': (4, 6),
                'barracks': (4, 9),
                'dark_barracks': (1, 2),
                'laboratory': (1, 5),
                'spell_factory': (1, 3),
                'dark_spell_factory': (),
                'workshop': ()
            },
            'defense': {
                'cannon': (5, 8),
                'archer_tower': (4, 8),
                'mortar': (3, 5),
                'air_defense': (3, 5),
                'wizard_tower': (2, 4),
                'air_sweeper': (1, 3),
                'hidden_tesla': (2, 3),
                'bomb_tower': (),
                'xbow': (),
                'inferno_tower': (),
                'eagle_artillery': (),
                'giga_tesla': (),
                'giga_inferno': (),
                'scattershot': (),
                'walls': (175, 7)
            },
            'traps': {
                'bomb': (6, 4),
                'spring_trap': (4, 2),
                'air_bomb': (2, 3),
                'giant_bomb': (2, 2),
                'seeking_air_mine': (1, 1),
                'skeleton_trap': (),
                'tornado_trap': ()
            }
        }
    },
    8: {
        'hitpoints': 3900,
        'build_cost': 2000000,
        'build_time': '3d',
        'storage_capacity': (750000, 750000, 5000),  # (Gold, Elixir, Dark Elixir)
        'buildings': {  # (number available, maximum level)
            'resource': {
                'gold_mine': (6, 12),
                'elixir_collector': (6, 12),
                'dark_elixir_drill': (2, 3),
                'gold_storage': (3, 11),
                'elixir_storage': (3, 11),
                'dark_elixir_storage': (1, 4),
                'clan_castle': (1, 4)
            },
            'army': {
                'army_camp': (4, 6),
                'barracks': (4, 10),
                'dark_barracks': (2, 4),
                'laboratory': (1, 6),
                'spell_factory': (1, 3),
                'dark_spell_factory': (1, 2),
                'workshop': ()
            },
            'defense': {
                'cannon': (5, 10),
                'archer_tower': (5, 10),
                'mortar': (4, 6),
                'air_defense': (3, 6),
                'wizard_tower': (3, 6),
                'air_sweeper': (1, 4),
                'hidden_tesla': (3, 6),
                'bomb_tower': (1, 2),
                'xbow': (),
                'inferno_tower': (),
                'eagle_artillery': (),
                'giga_tesla': (),
                'giga_inferno': (),
                'scattershot': (),
                'walls': (225, 8)
            },
            'traps': {
                'bomb': (6, 5),
                'spring_trap': (6, 3),
                'air_bomb': (4, 3),
                'giant_bomb': (3, 3),
                'seeking_air_mine': (2, 1),
                'skeleton_trap': (2, 2),
                'tornado_trap': ()
            }
        }
    },
    9: {
        'hitpoints': 4600,
        'build_cost': 3000000,
        'build_time': '4d',
        'storage_capacity': (1000000, 1000000, 10000),  # (Gold, Elixir, Dark Elixir)
        'buildings': {  # (number available, maximum level)
            'resource': {
                'gold_mine': (7, 12),
                'elixir_collector': (7, 12),
                'dark_elixir_drill': (3, 6),
                'gold_storage': (4, 11),
                'elixir_storage': (4, 11),
                'dark_elixir_storage': (1, 6),
                'clan_castle': (1, 5)
            },
            'army': {
                'army_camp': (4, 7),
                'barracks': (4, 11),
                'dark_barracks': (2, 6),
                'laboratory': (1, 7),
                'spell_factory': (1, 4),
                'dark_spell_factory': (1, 4),
                'workshop': ()
            },
            'defense': {
                'cannon': (5, 11),
                'archer_tower': (6, 11),
                'mortar': (4, 7),
                'air_defense': (4, 7),
                'wizard_tower': (4, 7),
                'air_sweeper': (2, 5),
                'hidden_tesla': (4, 7),
                'bomb_tower': (1, 3),
                'xbow': (2, 3),
                'inferno_tower': (),
                'eagle_artillery': (),
                'giga_tesla': (),
                'giga_inferno': (),
                'scattershot': (),
                'walls': (250, 10)
            },
            'traps': {
                'bomb': (6, 6),
                'spring_trap': (6, 4),
                'air_bomb': (4, 4),
                'giant_bomb': (4, 3),
                'seeking_air_mine': (4, 2),
                'skeleton_trap': (2, 3),
                'tornado_trap': ()
            }
        }
    },
    10: {
        'hitpoints': 5500,
        'build_cost': 5000000,
        'build_time': '6d',
        'storage_capacity': (1500000, 1500000, 20000),  # (Gold, Elixir, Dark Elixir)
        'buildings': {  # (number available, maximum level)
            'resource': {
                'gold_mine': (7, 13),
                'elixir_collector': (7, 13),
                'dark_elixir_drill': (3, 7),
                'gold_storage': (4, 11),
                'elixir_storage': (4, 11),
                'dark_elixir_storage': (1, 6),
                'clan_castle': (1, 6)
            },
            'army': {
                'army_camp': (4, 8),
                'barracks': (4, 12),
                'dark_barracks': (2, 7),
                'laboratory': (1, 8),
                'spell_factory': (1, 5),
                'dark_spell_factory': (1, 5),
                'workshop': ()
            },
            'defense': {
                'cannon': (6, 13),
                'archer_tower': (7, 13),
                'mortar': (4, 8),
                'air_defense': (4, 8),
                'wizard_tower': (4, 9),
                'air_sweeper': (2, 6),
                'hidden_tesla': (4, 8),
                'bomb_tower': (2, 4),
                'xbow': (3, 4),
                'inferno_tower': (2, 3),
                'eagle_artillery': (),
                'giga_tesla': (),
                'giga_inferno': (),
                'scattershot': (),
                'walls': (275, 11)
            },
            'traps': {
                'bomb': (6, 7),
                'spring_trap': (6, 5),
                'air_bomb': (5, 4),
                'giant_bomb': (5, 4),
                'seeking_air_mine': (5, 3),
                'skeleton_trap': (3, 4),
                'tornado_trap': ()
            }
        }
    },
    11: {
        'hitpoints': 6800,
        'build_cost': 7000000,
        'build_time': '10d',
        'storage_capacity': (2000000, 2000000, 20000),  # (Gold, Elixir, Dark Elixir)
        'buildings': {  # (number available, maximum level)
            'resource': {
                'gold_mine': (7, 14),
                'elixir_collector': (7, 14),
                'dark_elixir_drill': (3, 8),
                'gold_storage': (4, 12),
                'elixir_storage': (4, 12),
                'dark_elixir_storage': (1, 6),
                'clan_castle': (1, 7)
            },
            'army': {
                'army_camp': (4, 9),
                'barracks': (4, 13),
                'dark_barracks': (2, 8),
                'laboratory': (1, 9),
                'spell_factory': (1, 6),
                'dark_spell_factory': (1, 5),
                'workshop': ()
            },
            'defense': {
                'cannon': (7, 15),
                'archer_tower': (8, 15),
                'mortar': (4, 10),
                'air_defense': (4, 9),
                'wizard_tower': (5, 10),
                'air_sweeper': (2, 7),
                'hidden_tesla': (4, 9),
                'bomb_tower': (2, 6),
                'xbow': (4, 5),
                'inferno_tower': (2, 5),
                'eagle_artillery': (1, 2),
                'giga_tesla': (),
                'giga_inferno': (),
                'scattershot': (),
                'walls': (300, 12)
            },
            'traps': {
                'bomb': (6, 8),
                'spring_trap': (6, 5),
                'air_bomb': (5, 5),
                'giant_bomb': (5, 5),
                'seeking_air_mine': (5, 3),
                'skeleton_trap': (3, 4),
                'tornado_trap': (1, 2)
            }
        }
    },
    12: {
        'hitpoints': 7500,
        'build_cost': 9500000,
        'build_time': '14d',
        'storage_capacity': (2000000, 2000000, 20000),  # (Gold, Elixir, Dark Elixir)
        'buildings': {  # (number available, maximum level)
            'resource': {
                'gold_mine': (7, 14),
                'elixir_collector': (7, 14),
                'dark_elixir_drill': (3, 8),
                'gold_storage': (4, 13),
                'elixir_storage': (4, 13),
                'dark_elixir_storage': (1, 7),
                'clan_castle': (1, 8)
            },
            'army': {
                'army_camp': (4, 10),
                'barracks': (4, 14),
                'dark_barracks': (2, 9),
                'laboratory': (1, 10),
                'spell_factory': (1, 6),
                'dark_spell_factory': (1, 5),
                'workshop': (1, 3)
            },
            'defense': {
                'cannon': (7, 17),
                'archer_tower': (8, 17),
                'mortar': (4, 12),
                'air_defense': (4, 10),
                'wizard_tower': (5, 11),
                'air_sweeper': (2, 7),
                'hidden_tesla': (5, 10),
                'bomb_tower': (2, 7),
                'xbow': (4, 6),
                'inferno_tower': (3, 6),
                'eagle_artillery': (1, 3),
                'giga_tesla': (1, 5),
                'giga_inferno': (),
                'scattershot': (),
                'walls': (300, 13)
            },
            'traps': {
                'bomb': (6, 8),
                'spring_trap': (8, 5),
                'air_bomb': (6, 6),
                'giant_bomb': (6, 5),
                'seeking_air_mine': (6, 3),
                'skeleton_trap': (3, 4),
                'tornado_trap': (1, 3)
            }
        }
    },
    13: {
        'hitpoints': 8200,
        'build_cost': 12000000,
        'build_time': '18d',
        'storage_capacity': (2000000, 2000000, 20000),  # (Gold, Elixir, Dark Elixir)
        'buildings': {  # (number available, maximum level)
            'resource': {
                'gold_mine': (7, 14),
                'elixir_collector': (7, 14),
                'dark_elixir_drill': (3, 8),
                'gold_storage': (4, 14),
                'elixir_storage': (4, 14),
                'dark_elixir_storage': (1, 8),
                'clan_castle': (1, 9)
            },
            'army': {
                'army_camp': (4, 11),
                'barracks': (4, 14),
                'dark_barracks': (2, 9),
                'laboratory': (1, 11),
                'spell_factory': (1, 6),
                'dark_spell_factory': (1, 5),
                'workshop': (1, 5)
            },
            'defense': {
                'cannon': (7, 19),
                'archer_tower': (8, 19),
                'mortar': (4, 13),
                'air_defense': (4, 11),
                'wizard_tower': (5, 13),
                'air_sweeper': (2, 7),
                'hidden_tesla': (5, 12),
                'bomb_tower': (2, 8),
                'xbow': (4, 8),
                'inferno_tower': (3, 7),
                'eagle_artillery': (1, 4),
                'giga_tesla': (),
                'giga_inferno': (1, 5),
                'scattershot': (2, 2),
                'walls': (300, 14)
            },
            'traps': {
                'bomb': (7, 9),
                'spring_trap': (9, 5),
                'air_bomb': (6, 8),
                'giant_bomb': (6, 7),
                'seeking_air_mine': (7, 4),
                'skeleton_trap': (3, 4),
                'tornado_trap': (1, 3)
            }
        }
    }
}
