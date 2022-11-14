import random
import math

class weapon:
    def __init__ (self, name, level, damage, critical_chance, critical_damage,armor_pen, rarity):
        self.name = name
        self.level = level
        self.damage = damage
        self.critical_chance = critical_chance
        self.critical_damage = critical_damage
        self.armor_pen = armor_pen
        self.rarity = rarity
    type = "weapon"

# enter name, level, damage, crit chance, crit damage
sword_of_starter = weapon("Sword of Starter", 1, 7, 5, 2.1, 2, "common")
bow_of_critical = weapon("Bow of Critical", 1, 6, 20, 2.5, 0, "common")
dagger_of_shadows = weapon("Dagger of Shadows", 3, 17, 20, 2.7,7, "uncommon")
sword_of_storms = weapon("Sword of Storms", 5, 20, 18, 2.5, 8, "rare")
greatsword_of_amalur = weapon("Greatsword of Amalur", 7, 40, 10, 2.3, 10, "legendary")
hammer_of_thor = weapon("Hammer of Thor", 17, 70, 40, 3.1,0, "mythic")

weapons = [
    sword_of_starter,
    bow_of_critical,
    dagger_of_shadows,
    sword_of_storms,
    greatsword_of_amalur,
    hammer_of_thor
    
    
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
        print("Something is wrong with weapon selection")

def get_damage(player):
    #change damage based on level, so item is somewhat relevant
    level = player.stats["Level"] 
    damage = round(random.randrange(round(level * math.log(pow(level, 2)+1)), round(level * math.log(pow(level, 2)+1) + 2* level  + 1)))
    return damage

def get_default_weapon():
    #default weapon, fists, should be able to survive a couple rounds 
    fists = weapon("Fists", 1, 6, 5, 1.5, 0, "default")
    default_weapon = [fists]
    return default_weapon