import random
import math
from copy import copy

class weapon:
    def __init__ (self, name:str, level:int, rarity:str, ad:int = 0, ap:int = 0, critical_chance:int = 0, critical_damage:float = 0, armor_pen:int = 0):
        self.name = name
        self.level = level
        self.ad = ad
        self.ap = ap
        self.critical_chance = critical_chance
        self.critical_damage = critical_damage
        self.armor_pen = armor_pen
        self.rarity = rarity
    type = "weapon"
    
        
#RARITY_enabled
#rare < 5
# legendary < 10
#mythic => 10

#template = weapon(name = "", level= 0, ad= 0, ap = 0, critical_chance= 0, critical_damage= 0, armor_pen= 0, rarity=  "")

#common
sword_of_starter = weapon(name = "Sword of Starter", level = 1,ad = 7,ap = 10,critical_chance= 5,critical_damage= 2.1,armor_pen= 2, rarity="common")
bow_of_critical = weapon(name="Bow of Critical", level=1, ad=6,ap = 10,critical_chance= 20,critical_damage= 2.5,armor_pen= 0,rarity= "common")
rangers_bow = weapon(name = "Ranger's Bow", level= 2, ad= 8,ap = 10, critical_chance= 15, critical_damage= 1.8 , armor_pen= 3, rarity=  "common")

#uncommon
dagger_of_shadows = weapon(name="Dagger of Shadows",level= 3,ad= 12,ap = 10,critical_chance= 20,critical_damage= 2.7,armor_pen = 7, rarity = "uncommon")
knights_sword = weapon(name = "Knight's Sword", level= 4, ad= 14,ap = 10,critical_chance= 10, critical_damage= 1.8, armor_pen= 4, rarity= "uncommon")

#rare
sword_of_storms = weapon(name = "Sword of Storms", level = 5,ad= 15,ap = 10,critical_chance= 25,critical_damage= 2.7,armor_pen= 8,rarity= "rare")
sword_of_sea = weapon(name = "Sword of the Sea", level= 5, ad= 20,ap = 10,critical_chance= 10, critical_damage= 2.3, armor_pen= 20, rarity= "rare")

#legendary
greatsword_of_amalur = weapon(name = "Greatsword of Ezekiel",level= 10,ad= 30,ap = 10,critical_chance= 15,critical_damage= 2.3,armor_pen= 30,rarity= "legendary")

#mythic
hammer_of_thor = weapon(name= "Hammer of Thor", level = 17,ad= 40,ap = 10,critical_chance= 40,critical_damage= 2.7,armor_pen= 0,rarity= "mythic")
poseidons_trident = weapon(name = "Poseidon's Trident", level= 15, ad= 60,ap = 10, critical_chance= 0, critical_damage= 0, armor_pen= 20, rarity=  "mythic")
bow_of_artemis = weapon(name = "Bow of Artemis", level= 15, ad= 30,ap = 10,critical_chance= 75, critical_damage= 3.2 , armor_pen= 10, rarity=  "")


weapons = [
    #common
    sword_of_starter,
    bow_of_critical,
    rangers_bow,
    
    #uncommon
    dagger_of_shadows,
    knights_sword,
    
    #rare
    sword_of_storms,
    sword_of_sea,
    
    #legendary
    greatsword_of_amalur,
    
    #mythic
    hammer_of_thor,
    poseidons_trident,
    bow_of_artemis
    
    
]

common = []
uncommon = []
rare = []
legendary = []
mythic = []

def update_lists():
    for weapon in weapons:
        #gets new weapon level = +- 1 of base level
        update_level(weapon)
        # add weapon to list of matching rarity
        if(weapon.rarity == "common"): common.append(weapon)
        elif(weapon.rarity == "uncommon"): uncommon.append(weapon)
        elif(weapon.rarity == "rare"): rare.append(weapon)
        elif(weapon.rarity == "legendary"): legendary.append(weapon)
        elif(weapon.rarity == "mythic"):mythic.append(weapon)

def update_level( weapon):
    if(weapon.level == 1): weapon.level = 1
    else: weapon.level = random.randrange(weapon.level -1, weapon.level+ 1 )

def get_weapon(player, rarity):
    update_lists()
    
    find_correct_item = True
    while(find_correct_item):
        #choose rarity, update damage, return weapon
        if(rarity == "common"):
            orig_item = random.choice(common)
            weapon = copy(orig_item)
            weapon.ad += get_damage(weapon)

        elif(rarity == "uncommon"):
            orig_item = random.choice(uncommon)
            weapon = copy(orig_item)
            weapon.ad += get_damage(weapon)

        elif(rarity == "rare"):
            orig_item = random.choice(uncommon)
            weapon = copy(orig_item)
            weapon.ad += get_damage(weapon)

        elif(rarity == "legendary"):
            orig_item = random.choice(legendary)
            weapon = copy(orig_item)
            weapon.ad += get_damage(weapon)

        elif(rarity == "mythic"):
            orig_item = random.choice(mythic)
            weapon = copy(orig_item)
            weapon.ad += get_damage(weapon)
        else:
            print("Something is wrong with weapon selection")
            
        if(weapon.level < (player.stats["Level"] + 2)):
            find_correct_item = False
        else:
            find_correct_item = True        
            
            
    #adjust item based on level                                                                   - Level, Level
    if(weapon.critical_chance != 0): weapon.critical_chance += random.randrange(-player.stats["Level"],  player.stats["Level"])
    if(weapon.critical_chance < 0): weapon.critical_chance = 0
    
    if(weapon.critical_damage != 0): weapon.critical_damage +=round((random.randrange(-player.stats["Level"], round( player.stats["Level"] / 2)))/10 , 2)
    if(weapon.critical_damage < 0): weapon.critical_damage = 0
    
    if(weapon.armor_pen != 0): weapon.armor_pen += random.randrange(-player.stats["Level"],  round(player.stats["Level"] / 3 ))
    if(weapon.armor_pen < 0): weapon.armor_pen = 0


    #return item 
    return weapon

def get_damage(weapon):
    #change damage based on level, so item is somewhat relevant
    level = weapon.level
    damage = round(random.randrange(round(level * math.log(pow(level, 2)+1)), round(level * math.log(pow(level, 2)+1) + 2* level  + 1)))
    return damage

def get_default_weapon():
    #default weapon, fists, should be able to survive a couple rounds 
    fists = weapon(name="Fists",level= 1,ad= 6,ap =6, critical_chance= 5,critical_damage= 1.5,armor_pen= 0,rarity= "default")
    default_weapon = [fists]
    return default_weapon