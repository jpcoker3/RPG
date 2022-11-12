import random

class enemy:
    def __init__(self, name, level, damage, speed, health):
        self.name = name
        self.level = level
        self.damage = damage
        self.speed = speed
        self.health = health
    name = ""
    level = 0
    damage = 0
    speed = 0
    health = 0

first_names = [
    "Merlin",
    "Zorra",
    "Mercy",
    "Tabitha",
    "Hawk"
    
]

last_names = [
    "Hawthorne",
    "Silverbeard",
    "Blackbeard",
    "Bluebeard",
    "Griffin",
    "Raia"
    
]

def get_name():
    name = random.choice(first_names) + " " +random.choice(last_names)
    return name

def get_level(player_level):
    if(player_level == 0):
        return 0
    elif(player_level == 1):
        return 1
    elif( player_level <= 5):
        return random.randrange(player_level-1, player_level +1)
    elif(player_level <= 10):
        return random.randrange(player_level-2, player_level +3)
    else:
        return random.randrange(player_level - 4, player_level + 4)
    
def get_damage(level):
    damage =  random.randrange(( 5 +  level) , (10 + 4 * level) )
    return damage

def get_speed(level):
    speed = random.randrange( (50 + 2 * level), 100 + 4* level)
    return speed

def get_health(level):
    health = random.randrange(( 20 + 4 * level) , (60 + 8 * level) )
    return health 

def get_enemy(player):
    level = get_level(player.stats["Level"])
    
    unit = enemy(
        get_name(),  #name
        level, #level
        get_damage(level), #damage
        get_speed(level), #speed
        get_health(level) #health
    )
    
    
    return unit