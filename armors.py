import random
from copy import copy

class armor:
    #set some initial values
    def __init__(self, name:str, level:int, rarity:str, piece:str,class_type:str="", health_bonus:int = 0, speed_bonus:int = 0, stamina_bonus:int = 0, stamina_regen_bonus:int = 0, mana_regen_bonus:int = 0, armor_bonus:int = 0, mana_bonus:int = 0, regen_bonus:int = 0,luck_bonus:int = 0):
        self.name = name
        self.level = level
        self.health_bonus = health_bonus
        self.speed_bonus = speed_bonus
        self.stamina_bonus = stamina_bonus
        
        self.stamina_regen_bonus = stamina_regen_bonus
        self.mana_regen_bonus = mana_regen_bonus
        self.class_type = class_type
        
        self.armor_bonus = armor_bonus
        self.mana_bonus = mana_bonus
        self.regen_bonus = regen_bonus
        self.luck_bonus = luck_bonus
        self.rarity = rarity
        self.piece = piece
    type = "armor"
    
    
#typing this on phone... 

#RARITY_enabled
#rare < 5
# legendary < 10
#mythic => 10


#squire_boots = armor(name = "Squires' Boots",class_type = "melee",level= 2,health_bonus= 6,speed_bonus= 4,stamina_bonus= 5,armor_bonus= 5,  regen_bonus= 3,luck_bonus= 2, rarity= "common",piece= "boots")

#common
boots_of_bongo = armor(name="Boots of Bongo",class_type = "melee", level= 1,health_bonus= 5,speed_bonus= 0,stamina_bonus= 10,armor_bonus= 4,rarity= "common",piece= "boots")

squire_chest = armor(name = "Squires' Chestplate",class_type = "melee",level= 2,health_bonus= 7,speed_bonus= 5,stamina_bonus= 8,armor_bonus= 5,  regen_bonus= 3,luck_bonus= 2, rarity= "common",piece= "chest")
squire_boots = armor(name = "Squires' Boots",class_type = "melee",level= 2,health_bonus= 6,speed_bonus= 4,stamina_bonus= 5,armor_bonus= 5,  regen_bonus= 3,luck_bonus= 2, rarity= "common",piece= "boots")

bowman_boots = armor(name = "Bowmans' Boots",class_type = "ranged",level= 2,health_bonus= 3,speed_bonus= 7,stamina_bonus= 5, rarity= "common",piece= "boots")
bowman_cloak = armor(name = "Bowmans' Cloak",class_type = "ranged",level= 2,health_bonus= 5,speed_bonus= 3,stamina_bonus= 5, rarity= "common",piece= "chest")
bowman_pants = armor(name = "Bowmans' Boots",class_type = "ranged",level= 2,health_bonus= 4,speed_bonus= 5,stamina_bonus= 5, rarity= "common",piece= "pants")
bowman_hood = armor(name = "Bowmans' Hood",class_type = "ranged",level= 2,health_bonus= 3,speed_bonus= 3,stamina_bonus= 5, rarity= "common",piece= "helmet")

messengers_pants = armor(name="Messengers' Pants",class_type = "ranged", level= 2, health_bonus= 5,speed_bonus= 15, stamina_bonus= 7,armor_bonus= 1, regen_bonus = 4,luck_bonus= 2,rarity= "common",piece= "pants" )

disciple_hood = armor(name = "Disciple's Hood", class_type="magic", level=2, health_bonus=1, mana_bonus=5, mana_regen_bonus=2, rarity="common", piece="helmet")
disciple_robe = armor(name = "Disciple's Robe", class_type="magic", level=2, health_bonus=5, mana_bonus=5, mana_regen_bonus=2, rarity="common", piece="chest")
disciple_pants = armor(name = "Disciple's Pants", class_type="magic", level=2, health_bonus=1, mana_bonus=5, mana_regen_bonus=2, rarity="common", piece="pants")
disciple_shoes = armor(name = "Disciple's Shoes", class_type="magic", level=2, health_bonus=1, mana_bonus=5, mana_regen_bonus=2, rarity="common", piece="boots")

#uncommon
drunkards_shirt = armor(name="Drunkard's Shirt",class_type = "melee",level= 3,health_bonus= 12,speed_bonus= -10,stamina_bonus= -10,armor_bonus= 10,regen_bonus= 5,luck_bonus= 0,rarity= "uncommon",piece= "chest")

ranger_cloak = armor(name= "Ranger's Cloak",class_type = "ranged", level=4, health_bonus=8, speed_bonus=8, stamina_bonus=14,armor_bonus=5, regen_bonus=5, luck_bonus=7, rarity="uncommon", piece="chest")
ranger_boots = armor(name= "Ranger's Boots",class_type = "ranged", level=4, health_bonus=6, speed_bonus=15, stamina_bonus=12,armor_bonus=3,  regen_bonus=3, luck_bonus=4, rarity="uncommon", piece="boots")
ranger_pants = armor(name= "Ranger's Pants",class_type = "ranged", level=4, health_bonus=9, speed_bonus=12, stamina_bonus=10,armor_bonus=3, regen_bonus=4, luck_bonus=4, rarity="uncommon", piece="pants")
ranger_helmet= armor(name= "Ranger's Helmet",class_type = "ranged", level=4, health_bonus=9, speed_bonus=12, stamina_bonus=10,armor_bonus=3, regen_bonus=4, luck_bonus=4, rarity="uncommon", piece="helmet")

knights_chestplate = armor(name = "Knights' Chestplate",class_type = "melee",level= 4,health_bonus= 10,speed_bonus= 4,stamina_bonus= 8,armor_bonus= 10,  regen_bonus= 5,luck_bonus= 0, rarity= "uncommon",piece= "chest")

#rare
milf = armor(name="Mailplate Ivory Luxor Facilitator",class_type = "melee",level= 5,health_bonus= 30,speed_bonus= 10,stamina_bonus= 20, armor_bonus = 10,regen_bonus= 5, rarity= "rare",piece= "chest")
assasins_hood = armor(name= "Assassin's Hood", class_type = "melee",level=6, health_bonus=15, speed_bonus=12, stamina_bonus=7,armor_bonus=3,  regen_bonus=2, luck_bonus=8, rarity="rare", piece="helmet")
assassins_cloak = armor(name= "Assassin's Cloak", class_type = "melee",level=6, health_bonus=18, speed_bonus=10, stamina_bonus=5,armor_bonus=6,  regen_bonus=4, luck_bonus=5, rarity="rare", piece="chest")

#legendary
head_of_terry = armor(name = "Head of Terry",class_type = "melee",level= 10, health_bonus= 50,speed_bonus= 50,rarity= "legendary",piece= "helmet")


#mythic
breastplate_of_dormamu = armor(name="Breastplate of Dormamu",class_type = "melee",level= 17,health_bonus= 50,speed_bonus= 40,armor_bonus= 15, regen_bonus= 15,luck_bonus= 10,rarity= "mythic",piece= "chest")
boots_of_hermes = armor(name = "Boots of Hermes",class_type = "melee",level= 17, speed_bonus= 60,stamina_bonus= 40, armor_bonus= 5, regen_bonus = 0, rarity= "mythic", piece = "boots")


armors = [
    #common
    boots_of_bongo,
    squire_chest,
    messengers_pants,
    squire_boots,
    
    bowman_hood,
    bowman_cloak,
    bowman_pants,
    bowman_boots,
    
    disciple_hood,
    disciple_robe,
    disciple_pants,
    disciple_shoes,
    #uncommon
    drunkards_shirt,
    ranger_cloak,
    ranger_boots,
    ranger_helmet,
    ranger_pants,
    knights_chestplate,
    
    #rare
    milf,
    assasins_hood,
    
    #legendary
    head_of_terry,
    
    #mythic
    breastplate_of_dormamu,
    boots_of_hermes
         
    ]



common = []
uncommon = []
rare = []
legendary = []
mythic = []

def update_lists():
    for armor in armors:
        update_level( armor)
        if(armor.rarity == "common"): common.append(armor)
        elif(armor.rarity == "uncommon"): uncommon.append(armor)
        elif(armor.rarity == "rare"): rare.append(armor)
        elif(armor.rarity == "legendary"): legendary.append(armor)
        elif(armor.rarity == "mythic"): mythic.append(armor)
    
    
def update_level( armor):
    if(armor.level == 1): armor.level = 1
    else: armor.level = random.randrange(armor.level -1, armor.level + 1 )

def get_armor(player, rarity):
    update_lists()
    
    find_correct_item = True
    while(find_correct_item):
        #choose rarity of item
        if(rarity == "common"):
            orig_piece = random.choice(common)
            if(player.class_dmg_type == "both"):
                orig_piece = random.choice(common)
            else:
                while(player.class_dmg_type != orig_piece.class_type):
                    orig_piece = random.choice(common)
            armor_piece = copy(orig_piece)
        elif(rarity == "uncommon"):
            if(player.class_dmg_type == "both"):
                orig_piece = random.choice(uncommon)
            else:
                while(player.class_dmg_type != orig_piece.class_type):
                    orig_piece = random.choice(uncommon)
            armor_piece = copy(orig_piece)
        elif(rarity == "rare"):
            if(player.class_dmg_type == "both"):
                orig_piece = random.choice(rare)
            else:
                while(player.class_dmg_type != orig_piece.class_type):
                    orig_piece = random.choice(rare)
            armor_piece = copy(orig_piece)
        elif(rarity == "legendary"):
            if(player.class_dmg_type == "both"):
                orig_piece = random.choice(legendary)
            else:
                while(player.class_dmg_type != orig_piece.class_type):
                 orig_piece = random.choice(legendary)
            armor_piece = copy(orig_piece)
        elif(rarity == "mythic"):
            if(player.class_dmg_type == "both"):
                orig_piece = random.choice(mythic)
            else:
                while(player.class_dmg_type != orig_piece.class_type):
                    orig_piece = random.choice(mythic)
            armor_piece = copy(orig_piece)
    
        if(armor_piece.level < (player.stats["Level"] + 2)):
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
    
def get_default_armor():
    #kinda self explanatory, set default items
    helmet_of_null = armor(name = "You have no Helmet equipped", level = 0, rarity ="default", piece ="helmet")
    chest_of_null = armor(name ="You have no Chest equipped",level = 0,rarity ="default", piece ="chest")
    pants_of_null = armor(name ="You have no Pants equipped",level = 0,rarity ="default", piece ="pants")
    boots_of_null = armor(name ="You have no Boots equipped",level = 0,rarity = "default", piece ="boots")
    
    default = [helmet_of_null, chest_of_null, pants_of_null, boots_of_null]
    
    return default