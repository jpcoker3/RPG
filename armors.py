class armor:
    def __init__(self, name, level, health_bonus, speed_bonus, stamina_bonus, armor_bonus, mana_bonus, piece):
        self.name = name
        self.level = level
        self.health_bonus = health_bonus
        self.speed_bonus = speed_bonus
        self.stamina_bonus = stamina_bonus
        self.armor_bonus = armor_bonus
        self.mana_bonus = mana_bonus
        self.type = type
        
    name = ""
    level = 0
    health_bonus = 0
    speed_bonus = 0
    stamina_bonus = 0
    armor_bonus = 0
    mana_bonus = 0
    piece = ""
    

#enter name, level, health_bonus, speed_bonus, stamina_bonus, armor_bonus, mana bonus
boots_of_bongo = armor("Boots of Bongo", 0,10, 0, 10, 4,0, "boots")
    
    
    
armors = [
    boots_of_bongo
    
          
          
    ]
    
def get_armors():
    return armors