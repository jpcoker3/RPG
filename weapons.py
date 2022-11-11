class weapon:
    def __init__ (self, name, level, damage, critical_chance, critical_damage):
        self.name = name
        self.level = level
        self.damage = damage
        self.critical_chance = critical_chance
        self.critical_damage = critical_damage
    name = ""
    level = 0
    damage = 0
    critical_chance = 0
    critical_damage = 1
    type = "weapon"

# enter name, level, damage, crit chance, crit damage
sword_of_starter = weapon("Sword of Starter", 0, 1, 100, 1)
bow_of_critical = weapon("Bow of Critical", 0, 1, 100, 10)

    



weapons = [
    sword_of_starter,
    bow_of_critical
    
    
    
]


def get_weapons():
    return weapons

def get_default_weapon():
    fists = weapon("Fists", 0, 1, 0, 0)
    default_weapon = [fists]
    return default_weapon