import random
import player_info

class armor:
    #set some initial values
    def __init__(self, name, level, health_bonus, speed_bonus, stamina_bonus, armor_bonus, mana_bonus, regen_bonus, rarity, piece):
        self.name = name
        self.level = level
        self.health_bonus = health_bonus
        self.speed_bonus = speed_bonus
        self.stamina_bonus = stamina_bonus
        self.armor_bonus = armor_bonus
        self.mana_bonus = mana_bonus
        self.regen_bonus = regen_bonus
        self.rarity = rarity
        self.piece = piece
        
    #defaults
    name = ""
    level = 0
    health_bonus = 0
    speed_bonus = 0
    stamina_bonus = 0
    armor_bonus = 0
    mana_bonus = 0
    regen_bonus = 0
    rarity = "common"
    piece = ""
    type = "armor"
    

#enter name, level, health_bonus, speed_bonus, stamina_bonus, armor_bonus, mana bonus
boots_of_bongo = armor("Boots of Bongo", 0,10, 0, 10, 4,0,0, "common", "boots")
chest_of_milkers = armor("Chest of Milkers", 4, 30, -20, 15, 10, 0,0, "uncommon", "chest")
milf = armor("Mailplate Ivory Luxor Facilitator", 10, 70, 20, 30, 10, 0,0, "rare", "chest")
head_of_terry = armor("Head of Terry", 11, 50, 50, 0, 0, 0, "legendary", "helmet")


armors = [
    boots_of_bongo,
    chest_of_milkers,
    milf,
    head_of_terry
         
    ]



common = []
uncommon = []
rare = []
legendary = []
ultimate = []

def update_lists():
    for armor in armors:
        if(armor.rarity == "common"): common.append(armor)
        elif(armor.rarity == "uncommon"): uncommon.append(armor)
        elif(armor.rarity == "rare"): rare.append(armor)
        elif(armor.rarity == "legendary"): legendary.append(armor)
        elif(armor.rarity == "ultimate"): ultimate.append(armor)
    
def get_armor(player, rarity):
    update_lists()
    
    #choose rarity of item
    if(rarity == "common"):
        armor_piece = random.choice(common)
    elif(rarity == "uncommon"):
        armor_piece = random.choice(uncommon)
    elif(rarity == "rare"):
        armor_piece = random.choice(rare)
    elif(rarity == "legendary"):
        armor_piece = random.choice(legendary)
    elif(rarity == "ultimate"):
        armor_piece = random.choice(ultimate)
    
    #adjust item based on level
    if(armor_piece.health_bonus != 0): armor_piece.health_bonus += random.randrange(0, 2* player.stats["Level"]+1)
    elif(armor_piece.speed_bonus != 0): armor_piece.speed_bonus += random.randrange(0, 2* player.stats["Level"]+1)
    elif(armor_piece.stamina_bonus != 0): armor_piece.stamina_bonus += random.randrange(0, 2* player.stats["Level"]+1)
    elif(armor_piece.armor_bonus != 0): armor_piece.armor_bonus += random.randrange(0, 2* player.stats["Level"]+1)
    elif(armor_piece.mana_bonus != 0): armor_piece.mana_bonus += random.randrange(0, 2* player.stats["Level"]+1)
    elif(armor_piece.regen_bonus != 0): armor_piece.regen_bonus += random.randrange(0, 2* player.stats["Level"]+1)
    
    #return item 
    return armor_piece
    
def get_default_armor():
    #kinda self explanatory, set deault items
    helmet_of_null = armor("You have no Helmet equipped", 0, 0, 0, 0, 0,0, 0, "default", "helmet")
    chest_of_null = armor("You have no Chest equipped", 0, 0, 0, 0, 0,0, 0,"default", "chest")
    legs_of_null = armor("You have no Leg Armor equipped", 0, 0, 0, 0, 0,0, 0,"default", "legs")
    boots_of_null = armor("You have no Boots equipped", 0, 0, 0, 0, 0,0, 0,"default", "boots")
    
    default = [helmet_of_null, chest_of_null, legs_of_null, boots_of_null]
    
    return default