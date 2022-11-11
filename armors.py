class armor:
    def __init__(self, name, level, health_bonus, speed_bonus, stamina_bonus, armor_bonus, mana_bonus, piece):
        self.name = name
        self.level = level
        self.health_bonus = health_bonus
        self.speed_bonus = speed_bonus
        self.stamina_bonus = stamina_bonus
        self.armor_bonus = armor_bonus
        self.mana_bonus = mana_bonus
        self.piece = piece
        
    name = ""
    level = 0
    health_bonus = 0
    speed_bonus = 0
    stamina_bonus = 0
    armor_bonus = 0
    mana_bonus = 0
    piece = ""
    type = "armor"
    

#enter name, level, health_bonus, speed_bonus, stamina_bonus, armor_bonus, mana bonus
boots_of_bongo = armor("Boots of Bongo", 0,10, 0, 10, 4,0, "boots")
    
    

armors = [
    boots_of_bongo
    
          
          
    ]
    
def get_armors():
    return armors

def get_default_armor():
    helmet_of_null = armor("You have no Helmet equipped", 0, 0, 0, 0, 0, 0, "helmet")
    chest_of_null = armor("You have no Chest equipped", 0, 0, 0, 0, 0, 0, "chest")
    legs_of_null = armor("You have no Leg Armor equipped", 0, 0, 0, 0, 0, 0, "legs")
    boots_of_null = armor("You have no Boots equipped", 0, 0, 0, 0, 0, 0, "boots")
    
    default = [helmet_of_null, chest_of_null, legs_of_null, boots_of_null]
    
    return default