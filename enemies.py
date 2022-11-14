import random
import math

class enemy:
    def __init__(self, name, level, damage, critical_chance, critical_damage, speed, health, armor, armor_pen, enemy_type):
        self.name = name
        self.level = level
        self.damage = damage
        self.critical_chance = critical_chance
        self.critical_damage = critical_damage
        self.speed = speed
        self.health = health
        self.armor = armor
        self.armor_pen = armor_pen
        self.enemy_type = enemy_type

first_names = [
    "Merlin",
    "Zorra",
    "Mercy",
    "Tabitha",
    "Hawk",
    "Alastair",
    "Aeron",
    "Altalune",
    "Andreas",
    "Arthur",
    "Rune",
    "Rowena",
    "Nox",
    "Percival",
    "Owain",
    "Nimue",
    "River",
    "Luna",
    "Mirian",
    "Lancelot",
    "Lucan",
    "Lucian",
    "Galahad",
    "Faye",
    "Elderic",
    "Darius",
    "Dawn",
    "Elaine",
    "Evander",
    "Clarion"
]

last_names = [
    "Hawthorne",
    "Silverbeard",
    "Blackbeard",
    "Bluebeard",
    "Griffin",
    "Raia",
    "Albion",
    "Ashsorrow",
    "Dauntless",
    "Asteria",
    "Broffet",
    "Bertillion",
    "Crowstrike",
    "Cinderhell",
    "Clanwing",
    "Clawroot",
    "Grasshammer",
    "Hazekeep",
    "Hydrabreath",
    "Humblebringer",
    "Ironclad",
    "Irongrip",
    "Keenstone",
    "Leafwater",
    "Longhorn"
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
    damage =  round(random.randrange(round(math.log(pow(level, 2)) + level), round(math.log(pow(level, 6)) +  level + 1)))
    return damage

def get_speed(level):
    speed = random.randrange( (50 + 2 * level), 100 + 4* level)
    return speed

def get_health(level):
    health = random.randrange(( 20 + 4 * level) , (60 + 8 * level) )
    return health 

def get_critical_chance(level):
    critical_chance = random.randrange(5, 15)
    return critical_chance

def get_armor(level):
    armor = random.randrange(round(math.log(pow(level,2) + level)), round(math.log(pow(level, 2)+1) + 2*level+1))
    return armor

def get_critical_damage(level):
    critical_damage = random.randrange(11 + round(level/2), 15 +  round(level/2)) / 10
    return critical_damage

def get_armor_pen(level):
    armor_pen = random.randrange(level, level +1)
    return armor_pen

def get_enemy(player):
    if(player.stats["Level"] == 0):
        level = 1
    elif(player.stats["Level"] == 1):
        level = 2
    else:
        level = get_level(player.stats["Level"])
    
    unit = enemy(
        get_name(),  #name
        level, #level
        level + get_damage(level), #damage
        get_critical_chance(level), #critical chance
        get_critical_damage(level), #critical damage
        get_speed(level), #speed
        get_health(level), #health
        get_armor(level), #armor
        get_armor_pen(level), #armor penetration
        "enemy" # enemy type
    )
    
    
    return unit

def get_boss(game_round):
    if(game_round == 10):
        boss = enemy(
            "Slime Boss", #name
            2, #level
            10, #damage
            15, #crit chance
            1.5, #critical damage,
            75, #speed
            125, #health,
            20, #armor
            4, #armor_pen   
            "Boss"
        )
    elif(game_round == 20):
        boss = enemy(
            "Tavern Guard", # name
            4, # level
            15, #damage
            15, #crit chance
            2.0, #crit damage
            100, #speed
            175, #health
            40, #armor
            8, # armor pen
            "Boss"
        )
        pass
    else:
        print("Boss logic off. Recieved round = " + str(game_round))
        boss = enemy( 
                     " MissingNo ",
                     999, #level
                     999, #damage,
                     100, #critical_chance
                     10, #crit damage
                     999, # speed
                     999, #health
                     999, #armor
                     999, #armmor_pen
                     "Boss"
                     )
    
    return boss
