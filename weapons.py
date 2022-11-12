import random

class weapon:
    def __init__ (self, name, level, damage, critical_chance, critical_damage, rarity):
        self.name = name
        self.level = level
        self.damage = damage
        self.critical_chance = critical_chance
        self.critical_damage = critical_damage
        self.rarity = rarity
    name = ""
    level = 0
    damage = 0
    critical_chance = 0
    critical_damage = 2
    rarity = "common"
    type = "weapon"

# enter name, level, damage, crit chance, crit damage
sword_of_starter = weapon("Sword of Starter", 0, 7, 5, 2, "common")
bow_of_critical = weapon("Bow of Critical", 0, 5, 20, 2.5, "common")


weapons = [
    sword_of_starter,
    bow_of_critical
    
    
]

common = []
uncommon = []
rare = []
legendary = []
ultimate = []

def update_lists():
    for weapon in weapons:
        if(weapon.rarity == "common"): common.append(weapon)
        elif(weapon.rarity == "uncommon"): uncommon.append(weapon)
        elif(weapon.rarity == "rare"): rare.append(weapon)
        elif(weapon.rarity == "legendary"): legendary.append(weapon)
        elif(weapon.rarity == "ultimate"): ultimate.append(weapon)



def get_weapon(player, rarity):
    update_lists()
    
    #choose rarity, update damage, return weapon
    if(rarity == "common"):
        weapon = random.choice(common)
        weapon.damage += get_damage(player)
        return weapon
    elif(rarity == "uncommon"):
        weapon = random.choice(uncommon)
        weapon.damage += get_damage(player)
        return weapon
    elif(rarity == "rare"):
        weapon = random.choice(rare)
        weapon.damage += get_damage(player)
        return weapon
    elif(rarity == "legendary"):
        weapon = random.choice(legendary)
        weapon.damage += get_damage(player)
        return weapon
    elif(rarity == "ultimate"):
        weapon = random.choice(ultimate)
        weapon.damage += get_damage(player)
        return weapon
    else:
        print("uh oh")

def get_damage(player):
    #change damage based on level, so item is somewhat relevant
    level = player.stats["Level"] 
    damage = random.randrange(3* level, 5*level +1) + level
    return damage

def get_default_weapon():
    #default weapon, fists, should be able to survive a couple rounds 
    fists = weapon("Fists", 0, 5, 0, 0, "default")
    default_weapon = [fists]
    return default_weapon