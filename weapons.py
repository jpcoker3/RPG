class weapon:
    def __init__ (self, name, level, damage, critical_chance, critical_damage, hands):
        self.name = name
        self.level = level
        self.damage = damage
        self.critical_chance = critical_chance
        self.critical_damage = critical_damage
        self.hands = hands
    name = ""
    level = 0
    damage = 0
    critical_chance = 0
    critical_damage = 1
    hands = 0

# enter name, level, damage, crit chance, crit damage, hands
sword_of_starter = weapon("Sword of Starter", 0, 1, 100, 1, 2)
bow_of_critical = weapon("Bow of Critical", 0, 1, 100, 10, 2)

    



weapons = [
    sword_of_starter,
    bow_of_critical
    
    
    
]


def get_weapons():
    return weapons