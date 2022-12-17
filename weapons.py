import random
import math
from copy import copy
from dataclasses import dataclass

@dataclass(kw_only = True)
class weapon:
    name:str
    level:int
    rarity:str
    class_type:str
    ad:int = 0
    ap:int = 0
    critical_chance:int = 0
    critical_damage:float = 0
    armor_pen:int = 0
        
    type:str = "weapon"
    
        
#RARITY_enabled
#rare < 5
# legendary < 10
#mythic => 10

#template = weapon(name = "", level= 0, ad= 0, ap = 0, critical_chance= 0, critical_damage= 0, armor_pen= 0, rarity=  "")

#common
sword_of_starter = weapon(name = "Sword of Starter", class_type = "melee", level = 1,ad = 7,critical_chance= 5,critical_damage= 2.1,armor_pen= 2, rarity="common")
apprentice_staff = weapon(name = "Apprentice's Staff", class_type = "magic", level = 1,ap = 10,critical_chance= 5,critical_damage= 2.1,armor_pen= 2, rarity="common")
bow_of_critical = weapon(name="Bow of Critical",class_type = "ranged", level=1, ad=6,critical_chance= 20,critical_damage= 2.5,armor_pen= 0,rarity= "common")
rangers_bow = weapon(name = "Ranger's Bow",class_type = "ranged", level= 2, ad= 8, critical_chance= 15, critical_damage= 1.8 , armor_pen= 3, rarity=  "common")

#uncommon
dagger_of_shadows = weapon(name="Dagger of Shadows",class_type = "melee",level= 3,ad= 12,critical_chance= 20,critical_damage= 2.7,armor_pen = 7, rarity = "uncommon")
knights_sword = weapon(name = "Knight's Sword", class_type = "melee",level= 4, ad= 14,critical_chance= 10, critical_damage= 1.8, armor_pen= 4, rarity= "uncommon")
hunters_compound_bow = weapon(name = "Hunter's Compound Bow",class_type = "ranged", level= 5, ad= 13, critical_chance= 20, critical_damage= 2.1 , armor_pen= 5, rarity=  "uncommon")
novice_staff = weapon(name="Novice Magestaff", class_type="magic", level=5, ap=12, critical_chance=10, critical_damage=1.80, armor_pen=3, rarity="uncommon")

#rare
sword_of_storms = weapon(name = "Sword of Storms",class_type = "melee", level = 6,ad= 15,critical_chance= 25,critical_damage= 2.7,armor_pen= 8,rarity= "rare")
sword_of_sea = weapon(name = "Sword of the Sea",class_type = "melee", level= 6, ad= 20,critical_chance= 10, critical_damage= 2.3, armor_pen= 20, rarity= "rare")
sceptre_of_knowledge = weapon(name="Sceptre of Knowledge", class_type="magic", level=6, ap=15, critical_chance=25, critical_damage=2.30, armor_pen=12, rarity="rare")
sniper_rifle = weapon(name = "Sniper Rifle",class_type = "ranged", level= 6, ad= 15,critical_chance= 25, critical_damage= 2.5 , armor_pen= 18, rarity=  "rare")

#legendary
greatsword_of_amalur = weapon(name = "Greatsword of Amalur",class_type = "melee",level= 10,ad= 25,critical_chance= 15,critical_damage= 2.3,armor_pen= 30,rarity= "legendary")
nightbane = weapon(name="Nightbane", class_type="ranged", level=10, ad=22, critical_chance=30, critical_damage=2.5, armor_pen=20, rarity="legendary")
jadis_wand = weapon(name="Jadis' Wand", class_type="magic", level=10, ap = 23,critical_chance=20, critical_damage=1.95,armor_pen=12, rarity="legendary" )

#mythic
hammer_of_thor = weapon(name= "Hammer of Thor",class_type = "melee", level = 17,ad= 40,critical_chance= 40,critical_damage= 2.7,armor_pen= 0,rarity= "mythic")
poseidons_trident = weapon(name = "Poseidon's Trident",class_type = "melee", level= 15, ad= 60, critical_chance= 0, critical_damage= 0, armor_pen= 20, rarity=  "mythic")
bow_of_artemis = weapon(name = "Bow of Artemis", class_type = "ranged",level= 15, ad= 30,critical_chance= 75, critical_damage= 3.2 , armor_pen= 10, rarity=  "mythic")
merlins_staff = weapon(name="Merlin's Staff", class_type="magic", level=15, ap=45, critical_chance=30, critical_damage=2.35, armor_pen=15, rarity="mythic")



any = [
    
    
    
]

ranged = [
    bow_of_critical,
    rangers_bow,
    bow_of_artemis,
    hunters_compound_bow,
    sniper_rifle,
    nightbane
    
]

melee = [
    sword_of_starter,
    sword_of_storms,
    sword_of_sea,
    dagger_of_shadows,
    knights_sword,
    greatsword_of_amalur,
    hammer_of_thor,
    poseidons_trident
    
]

magic = [
    apprentice_staff,
    merlins_staff,
    novice_staff,
    sceptre_of_knowledge,
    jadis_wand
]



common = []
uncommon = []
rare = []
legendary = []
mythic = []

#update lists with current weapons
def update_lists():
    for weapon in (ranged  + melee  + magic + any):
        #gets new weapon level = +- 1 of base level
        update_level(weapon)
        # add weapon to list of matching rarity
        if(weapon.rarity == "common"): common.append(weapon)
        elif(weapon.rarity == "uncommon"): uncommon.append(weapon)
        elif(weapon.rarity == "rare"): rare.append(weapon)
        elif(weapon.rarity == "legendary"): legendary.append(weapon)
        elif(weapon.rarity == "mythic"):mythic.append(weapon)

#make sure relevant level
def update_level( weapon):
    if(weapon.level == 1): weapon.level = 1
    else: weapon.level = random.randrange(weapon.level -1, weapon.level+ 1 )

#returns a random weapon of the correct rarity and type
def get_weapon(player, rarity):
    update_lists()
    
    find_correct_item = True
    while(find_correct_item):
        
        #check for player damage type
        if(player.class_dmg_type == "any"):
            list = any + melee + ranged + magic #set list
            
            orig_piece = random.choice(list)
            while(orig_piece.rarity != rarity):  #while the armor piece isnt the correct rarity, get armor again
                orig_piece = random.choice(list)
                
            armor_piece = copy(orig_piece) #copy the armor piece
            

        elif(player.class_dmg_type == "melee"):
            list = any + melee #set list
            
            orig_piece = random.choice(list)
            while(orig_piece.rarity != rarity):  #while the armor piece isnt the correct rarity, get armor again
                orig_piece = random.choice(list)
                
            new_weapon = copy(orig_piece) #copy the armor piece
    
        elif(player.class_dmg_type == "ranged"):
            list = any + ranged  #set list
            
            orig_piece = random.choice(list)
            while(orig_piece.rarity != rarity):  #while the armor piece isnt the correct rarity, get armor again
                orig_piece = random.choice(list)
                
            new_weapon = copy(orig_piece) #copy the armor piece
      
        elif(player.class_dmg_type == "magic"):
            list = any + magic #set list
    
            orig_piece = random.choice(list)
            while(orig_piece.rarity != rarity):  #while the armor piece isnt the correct rarity, get armor again
                orig_piece = random.choice(list)
                
            new_weapon = copy(orig_piece) #copy the armor piece
       
        else:
            print("Incorrect class damage type")
#TODO: add more weapons so that the level thing actually works
        if(new_weapon.level < (player.stats["Level"] + 100)):
            find_correct_item = False
        else:
            find_correct_item = True    
            
            
    #adjust item based on level                                                                   - Level, Level
    if(new_weapon.critical_chance != 0): new_weapon.critical_chance += random.randrange(-player.stats["Level"],  player.stats["Level"])
    if(new_weapon.critical_chance < 0): new_weapon.critical_chance = 0
    
    if(new_weapon.critical_damage != 0): new_weapon.critical_damage +=round((random.randrange(-player.stats["Level"], round( player.stats["Level"] / 2)))/10 , 2)
    if(new_weapon.critical_damage < 0): new_weapon.critical_damage = 0
    
    if(new_weapon.armor_pen != 0): new_weapon.armor_pen += random.randrange(-player.stats["Level"],  round(player.stats["Level"] / 3 ))
    if(new_weapon.armor_pen < 0): new_weapon.armor_pen = 0


    #return item 
    return new_weapon

def get_damage(weapon):
    #change damage based on level, so item is somewhat relevant
    level = weapon.level
    damage = round(random.randrange(round(level * math.log(pow(level, 2)+1)), round(level * math.log(pow(level, 2)+1) + 2* level  + 1)))
    return damage

def get_default_weapons():
    #default weapon, fists, should be able to survive a couple rounds 
    stick = weapon(name="Stick",class_type = "any",level= 1,ad= 4,ap =4, critical_chance= 5,critical_damage= 1.5,armor_pen= 0,rarity= "default")
    rusty_butter_knife = weapon(name="Rusty Butter Knife",class_type = "melee",level= 1,ad= 8, critical_chance= 2,critical_damage= 1.3,armor_pen= 0,rarity= "default")
    slingshot = weapon(name="Slingshot",class_type = "ranged",level= 1,ad= 6, critical_chance= 7,critical_damage= 1.7,armor_pen= 0,rarity= "default")
    magic_stick = weapon(name="Magic Stick",class_type = "magic",level= 1, ap =7, critical_chance= 5,critical_damage= 2.1,armor_pen= 0,rarity= "default")
    
    default_weapons = [stick, rusty_butter_knife, slingshot, magic_stick]
    return default_weapons