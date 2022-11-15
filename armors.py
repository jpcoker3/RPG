import random
from copy import copy

class armor:
    #set some initial values
    def __init__(self, name, level, health_bonus, speed_bonus, stamina_bonus, armor_bonus, mana_bonus, regen_bonus,luck_bonus, rarity, piece):
        self.name = name
        self.level = level
        self.health_bonus = health_bonus
        self.speed_bonus = speed_bonus
        self.stamina_bonus = stamina_bonus
        self.armor_bonus = armor_bonus
        self.mana_bonus = mana_bonus
        self.regen_bonus = regen_bonus
        self.luck_bonus = luck_bonus
        self.rarity = rarity
        self.piece = piece
    type = "armor"
    
    
    
#RARITY_enabbled
#rare < 5
# legendary < 10
#mythic => 10


#template = armor(name= "", level=0, health_bonus=0, speed_bonus=0, stamina_bonus=0,armor_bonus=0, mana_bonus=0, regen_bonus=0, luck_bonus=0, rarity="", piece="")

#common
boots_of_bongo = armor(name="Boots of Bongo",level= 1,health_bonus= 5,speed_bonus= 0,stamina_bonus= 10,armor_bonus= 4, mana_bonus= 0,regen_bonus= 0,luck_bonus= 0,rarity= "common",piece= "boots")
knights_chestplate = armor(name = "Knights' Chestplate",level= 2,health_bonus= 5,speed_bonus= 5,stamina_bonus= 8,armor_bonus= 5, mana_bonus= 0, regen_bonus= 5,luck_bonus= 1, rarity= "common",piece= "chest")
messengers_pants = armor(name="Messengers' Pants",level= 1, health_bonus= 5,speed_bonus= 15, stamina_bonus= 7,armor_bonus= 1,mana_bonus= 0, regen_bonus = 4,luck_bonus= 2,rarity= "common",piece= "pants" )

#uncommon
drunkards_shirt = armor(name="Drunkards' Shirt",level= 3,health_bonus= 12,speed_bonus= -10,stamina_bonus= -10,armor_bonus= 10,mana_bonus= 0,regen_bonus= 5,luck_bonus= 0,rarity= "uncommon",piece= "chest")
ranger_cloak = armor(name= "Ranger's Cloak", level=4, health_bonus=8, speed_bonus=7, stamina_bonus=14,armor_bonus=5, mana_bonus=0, regen_bonus=5, luck_bonus=7, rarity="uncommon", piece="chest")
ranger_boots = armor(name= "Ranger's Boots", level=4, health_bonus=6, speed_bonus=15, stamina_bonus=12,armor_bonus=3, mana_bonus=0, regen_bonus=3, luck_bonus=4, rarity="uncommon", piece="boots")
ranger_pants = armor(name= "Ranger's Boots", level=4, health_bonus=9, speed_bonus=12, stamina_bonus=10,armor_bonus=3, mana_bonus=0, regen_bonus=4, luck_bonus=4, rarity="uncommon", piece="pants")


#rare
milf = armor(name="Mailplate Ivory Luxor Facilitator",level= 5,health_bonus= 30,speed_bonus= 10,stamina_bonus= 20, armor_bonus = 10, mana_bonus = 0,regen_bonus= 5, luck_bonus= 0,rarity= "rare",piece= "chest")
assasins_hood = armor(name= "Assassin's Hood", level=6, health_bonus=15, speed_bonus=12, stamina_bonus=7,armor_bonus=3, mana_bonus=0, regen_bonus=2, luck_bonus=8, rarity="rare", piece="helmet")
assassins_cloak = armor(name= "Assassin's Cloak", level=6, health_bonus=18, speed_bonus=10, stamina_bonus=5,armor_bonus=6, mana_bonus=0, regen_bonus=4, luck_bonus=5, rarity="rare", piece="chest")

#legendary
head_of_terry = armor(name = "Head of Terry",level= 10, health_bonus= 50,speed_bonus= 50,stamina_bonus= 0,armor_bonus= 0,mana_bonus= 0,regen_bonus= 0,luck_bonus= 0,rarity= "legendary",piece= "helmet")


#mythic
breastplate_of_dormamu = armor(name="Breastplate of Dormamu",level= 17,health_bonus= 50,speed_bonus= 40,stamina_bonus= 0,armor_bonus= 15, mana_bonus= 0,regen_bonus= 15,luck_bonus= 10,rarity= "mythic",piece= "chest")
boots_of_hermes = armor(name = "Boots of Hermes",level= 17, health_bonus= 0,speed_bonus= 60,stamina_bonus= 40, armor_bonus= 5, mana_bonus = 0, regen_bonus = 0,luck_bonus= 15,rarity= "mythic", piece = "boots")


armors = [
    #common
    boots_of_bongo,
    knights_chestplate,
    messengers_pants,
    
    #uncommon
    drunkards_shirt,
    ranger_cloak,
    ranger_boots,
    
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
            armor_piece = copy(orig_piece)
        elif(rarity == "uncommon"):
            orig_piece = random.choice(uncommon)
            armor_piece = copy(orig_piece)
        elif(rarity == "rare"):
            orig_piece = random.choice(rare)
            armor_piece = copy(orig_piece)
        elif(rarity == "legendary"):
            orig_piece = random.choice(legendary)
            armor_piece = copy(orig_piece)
        elif(rarity == "mythic"):
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
    if(armor_piece.armor_bonus != 0): armor_piece.armor_bonus += random.randrange(-player.stats["Level"],  player.stats["Level"]+5)
    if(armor_piece.mana_bonus != 0): armor_piece.mana_bonus += random.randrange(-player.stats["Level"],  player.stats["Level"]+5)
    if(armor_piece.regen_bonus != 0): armor_piece.regen_bonus += random.randrange(-player.stats["Level"],  player.stats["Level"]+5)
    if(armor_piece.luck_bonus != 0): armor_piece.luck_bonus += random.randrange(-player.stats["Level"],  player.stats["Level"]+5)
    #return item 
    return armor_piece
    
def get_default_armor():
    #kinda self explanatory, set default items
    helmet_of_null = armor("You have no Helmet equipped", 0, 0, 0, 0, 0,0, 0,0, "default", "helmet")
    chest_of_null = armor("You have no Chest equipped", 0, 0, 0, 0, 0,0, 0,0,"default", "chest")
    pants_of_null = armor("You have no Pants equipped", 0, 0, 0, 0, 0,0, 0,0,"default", "pants")
    boots_of_null = armor("You have no Boots equipped", 0, 0, 0, 0, 0,0, 0,0,"default", "boots")
    
    default = [helmet_of_null, chest_of_null, pants_of_null, boots_of_null]
    
    return default