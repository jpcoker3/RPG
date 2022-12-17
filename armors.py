import random
from copy import copy
from dataclasses import dataclass, field

@dataclass(kw_only = True)
class armor:
    #set some initial values
    name:str
    level:int
    rarity:str
    piece:str
    class_type:str=""
    health_bonus:int = 0
    speed_bonus:int = 0
    stamina_bonus:int = 0
    stamina_regen_bonus:int = 0
    mana_regen_bonus:int = 0
    armor_bonus:int = 0
    mana_bonus:int = 0
    regen_bonus:int = 0
    luck_bonus:int = 0
       
    type:int = field(init = False, default = "armor")
    
    
#typing this on phone... 

#RARITY_enabled
#rare < 5
# legendary < 10
#mythic => 10


#squire_boots = armor(name = "Squires' Boots",class_type = "melee",level= 2,health_bonus= 6,speed_bonus= 4,stamina_bonus= 5,armor_bonus= 5,  regen_bonus= 3,luck_bonus= 2, rarity= "common",piece= "boots")

#common
boots_of_bongo = armor(name="Boots of Bongo",class_type = "all", level= 1,health_bonus= 5,speed_bonus= 0,armor_bonus= 4,rarity= "common",piece= "boots")

squire_chest = armor(name = "Squires' Chestplate",class_type = "melee",level= 2,health_bonus= 7,speed_bonus= 5,stamina_bonus= 8,armor_bonus= 5,  regen_bonus= 3,luck_bonus= 2, rarity= "common",piece= "chest")
squire_boots = armor(name = "Squires' Boots",class_type = "melee",level= 2,health_bonus= 6,speed_bonus= 4,stamina_bonus= 5,armor_bonus= 5,  regen_bonus= 3,luck_bonus= 2, rarity= "common",piece= "boots")

bowman_boots = armor(name = "Bowmans' Boots",class_type = "ranged",level= 2,health_bonus= 3,speed_bonus= 7,stamina_bonus= 5, rarity= "common",piece= "boots")
bowman_cloak = armor(name = "Bowmans' Cloak",class_type = "ranged",level= 2,health_bonus= 5,speed_bonus= 3,stamina_bonus= 5, rarity= "common",piece= "chest")
bowman_pants = armor(name = "Bowmans' Boots",class_type = "ranged",level= 2,health_bonus= 4,speed_bonus= 5,stamina_bonus= 5, rarity= "common",piece= "pants")
bowman_hood = armor(name = "Bowmans' Hood",class_type = "ranged",level= 2,health_bonus= 3,speed_bonus= 3,stamina_bonus= 5, rarity= "common",piece= "helmet")

messengers_pants = armor(name="Messengers' Pants",class_type = "all", level= 2, health_bonus= 5,speed_bonus= 15,armor_bonus= 1, regen_bonus = 4,luck_bonus= 2,rarity= "common",piece= "pants" )

disciple_hood = armor(name = "Disciple's Hood", class_type="magic", level=2, health_bonus=1, mana_bonus=5, mana_regen_bonus=2, rarity="common", piece="helmet")
disciple_robe = armor(name = "Disciple's Robe", class_type="magic", level=2, health_bonus=5, mana_bonus=5, mana_regen_bonus=2, rarity="common", piece="chest")
disciple_pants = armor(name = "Disciple's Pants", class_type="magic", level=2, health_bonus=1, mana_bonus=5, mana_regen_bonus=2, rarity="common", piece="pants")
disciple_shoes = armor(name = "Disciple's Shoes", class_type="magic", level=2, health_bonus=1, mana_bonus=5, mana_regen_bonus=2, rarity="common", piece="boots")

#uncommon
drunkards_shirt = armor(name="Drunkard's Shirt",class_type = "all",level= 3,health_bonus= 12,speed_bonus= -10,stamina_bonus= -10,armor_bonus= 10,regen_bonus= 5,luck_bonus= 0,rarity= "uncommon",piece= "chest")

ranger_cloak = armor(name= "Ranger's Cloak",class_type = "ranged", level=4, health_bonus=8, speed_bonus=8, stamina_bonus=14,armor_bonus=5, regen_bonus=5, luck_bonus=7, rarity="uncommon", piece="chest")
ranger_boots = armor(name= "Ranger's Boots",class_type = "ranged", level=4, health_bonus=6, speed_bonus=15, stamina_bonus=12,armor_bonus=3,  regen_bonus=3, luck_bonus=4, rarity="uncommon", piece="boots")
ranger_pants = armor(name= "Ranger's Pants",class_type = "ranged", level=4, health_bonus=9, speed_bonus=12, stamina_bonus=10,armor_bonus=3, regen_bonus=4, luck_bonus=4, rarity="uncommon", piece="pants")
ranger_helmet= armor(name= "Ranger's Helmet",class_type = "ranged", level=4, health_bonus=9, speed_bonus=12, stamina_bonus=10,armor_bonus=3, regen_bonus=4, luck_bonus=4, rarity="uncommon", piece="helmet")

knights_chestplate = armor(name = "Knights' Chestplate",class_type = "melee",level= 4,health_bonus= 10,speed_bonus= 4,stamina_bonus= 8,armor_bonus= 10,  regen_bonus= 5,luck_bonus= 0, rarity= "uncommon",piece= "chest")

apprentice_hood = armor(name = "Apprentice's Hood", class_type="magic", level=4, health_bonus=6, mana_bonus=7, mana_regen_bonus=4,luck_bonus=3, rarity="uncommon", piece="helmet")
apprentice_robe = armor(name = "Apprentice's Robe", class_type="magic", level=4, health_bonus=8, mana_bonus=10, mana_regen_bonus=4,armor_bonus=8, rarity="uncommon", piece="chest")
apprentice_pants = armor(name = "Apprentice's Pants", class_type="magic", level=4, health_bonus=6, mana_bonus=8, mana_regen_bonus=4,speed_bonus=8, rarity="uncommon", piece="pants")
apprentice_shoes = armor(name = "Apprentice's Shoes", class_type="magic", level=4, health_bonus=6, mana_bonus=8, mana_regen_bonus=4,regen_bonus=8, rarity="uncommon", piece="boots")

seraphine_hood = armor(name = "Seraphine's Hood", class_type="all", level=4, health_bonus=12, regen_bonus=10, mana_regen_bonus=10, stamina_regen_bonus=10, speed_bonus=15, rarity="uncommon", piece="helmet")

#rare
milf = armor(name="Mailplate Ivory Luxor Facilitator",class_type = "all",level= 5,health_bonus= 30,speed_bonus= 10,stamina_bonus= 20,mana_bonus=20, armor_bonus = 10,regen_bonus= 5, rarity= "rare",piece= "chest")
assasins_hood = armor(name= "Assassin's Hood", class_type = "all",level=6, health_bonus=15, speed_bonus=12, stamina_bonus=7, mana_bonus=7,armor_bonus=3,  regen_bonus=2, luck_bonus=8, rarity="rare", piece="helmet")
assassins_cloak = armor(name= "Assassin's Cloak", class_type = "melee",level=6, health_bonus=18, speed_bonus=10, stamina_bonus=5,armor_bonus=6,  regen_bonus=4, luck_bonus=5, rarity="rare", piece="chest")

#legendary
head_of_terry = armor(name = "Head of Terry",class_type = "melee",level= 10, health_bonus= 50,speed_bonus= 50,rarity= "legendary",piece= "helmet")
armadillo_chest = armor(name="Armadillo Chestpiece", class_type="all",level =10, health_bonus= 40, speed_bonus= -20, armor_bonus= 40, regen_bonus=15, luck_bonus= -10,rarity="legendary", piece="chest")


#mythic
breastplate_of_dormamu = armor(name="Breastplate of Dormamu",class_type = "melee",level= 17,health_bonus= 50,speed_bonus= 40,armor_bonus= 15, regen_bonus= 15,luck_bonus= 10,rarity= "mythic",piece= "chest")
boots_of_hermes = armor(name = "Boots of Hermes",class_type = "all",level= 17, speed_bonus= 60,stamina_bonus= 40,mana_bonus=40, armor_bonus= 5, rarity= "mythic", piece = "boots")


any = [ 
    boots_of_bongo,
    messengers_pants,
    milf,
    breastplate_of_dormamu,
    boots_of_hermes,
    assasins_hood,       
    drunkards_shirt,
    seraphine_hood,
    armadillo_chest
]

melee = [
    squire_chest,
    squire_boots,
    head_of_terry,
    knights_chestplate
    
]

ranged = [
    bowman_hood,
    bowman_cloak,
    bowman_pants,
    bowman_boots,
    ranger_cloak,
    ranger_boots,
    ranger_helmet,
    ranger_pants
    
]

magic = [
    disciple_hood,
    disciple_robe,
    disciple_pants,
    disciple_shoes,
    apprentice_hood,
    apprentice_robe,
    apprentice_pants,
    apprentice_shoes
    
]
    



def update_lists():
    for armor in any:
        update_level(armor)
    for armor in melee:
        update_level(armor)
    for armor in ranged:
        update_level(armor)
    for armor in magic:
        update_level(armor)

        
def update_level( armor):
    if(armor.level == 1): armor.level = 1
    else: armor.level = random.randrange(armor.level -1, armor.level + 1 )


def get_armor(player, rarity):
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
                
            armor_piece = copy(orig_piece) #copy the armor piece
    
        elif(player.class_dmg_type == "ranged"):
            list = any + ranged  #set list
            
            orig_piece = random.choice(list)
            while(orig_piece.rarity != rarity):  #while the armor piece isnt the correct rarity, get armor again
                orig_piece = random.choice(list)
                
            armor_piece = copy(orig_piece) #copy the armor piece
      
        elif(player.class_dmg_type == "magic"):
            list = any + magic #set list
    
            orig_piece = random.choice(list)
            while(orig_piece.rarity != rarity):  #while the armor piece isnt the correct rarity, get armor again
                orig_piece = random.choice(list)
                
            armor_piece = copy(orig_piece) #copy the armor piece
       
        else:
            print("Incorrect class damage type")
#TODO add more armors of different levels so that this makes sense
        if(armor_piece.level < (player.stats["Level"] + 100)):
            find_correct_item = False
        else:
            find_correct_item = True
        
    
    #adjust item based on level                                                                   - Level, level +5
    if(armor_piece.health_bonus != 0): armor_piece.health_bonus += random.randrange(-player.stats["Level"],  player.stats["Level"]+5)
    if(armor_piece.speed_bonus != 0): armor_piece.speed_bonus += random.randrange(-player.stats["Level"],  player.stats["Level"]+5)
    if(armor_piece.stamina_bonus != 0): armor_piece.stamina_bonus += random.randrange(-player.stats["Level"],  player.stats["Level"]+5)
    
    if(armor_piece.stamina_regen_bonus != 0): armor_piece.stamina_regen_bonus += random.randrange(-player.stats["Level"],  player.stats["Level"]+5)
    if(armor_piece.mana_regen_bonus != 0): armor_piece.mana_regen_bonus += random.randrange(-player.stats["Level"],  player.stats["Level"]+5)
    
    if(armor_piece.armor_bonus != 0): armor_piece.armor_bonus += random.randrange(-player.stats["Level"],  player.stats["Level"]+5)
    if(armor_piece.mana_bonus != 0): armor_piece.mana_bonus += random.randrange(-player.stats["Level"],  player.stats["Level"]+5)
    if(armor_piece.regen_bonus != 0): armor_piece.regen_bonus += random.randrange(-player.stats["Level"],  player.stats["Level"]+5)
    if(armor_piece.luck_bonus != 0): armor_piece.luck_bonus += random.randrange(-player.stats["Level"],  player.stats["Level"]+5)
    #return item 
    return armor_piece
    
    
#kinda self explanatory, set default items
def get_default_armor():
    helmet_of_null = armor(name = "You have no headpiece equipped", level = 0, rarity ="default", piece ="helmet")
    chest_of_null = armor(name ="You have no Chest equipped",level = 0,rarity ="default", piece ="chest")
    pants_of_null = armor(name ="Tighty Whities",level = 0,rarity ="default", piece ="pants")
    boots_of_null = armor(name ="You have no Boots equipped",level = 0,rarity = "default", piece ="boots")
    
    default = [helmet_of_null, chest_of_null, pants_of_null, boots_of_null]
    return default