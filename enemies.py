import random
import math
from dataclasses import dataclass

@dataclass
class enemy:
    name:str
    level:int
    damage:int
    critical_chance:int
    critical_damage:int
    speed:int
    health:int
    armor:int
    armor_pen:int
    enemy_type:int
    

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
    "Clarion",
    "Carly",
    "James",
    "Harish",
    "Travis"
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
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    return name

def get_level(player_level):
    if(player_level == 0):
        return 0
    elif(player_level == 1):
        return 1
    elif( player_level <= 5):
        return random.randrange(player_level, player_level +1)
    else:
        return random.randrange(player_level-1, player_level +3)

    
def get_damage(level):
    damage =  round(random.randrange(round(math.log(level ** 2) + level), round(math.log(level ** 6) +  level + 1)))
    return level + damage

def get_speed(level):
    speed = random.randrange( (50 + 2 * level), 100 + 4* level)
    return speed

def get_health(level):
    health = random.randrange(( 20 + 4 * level) , (60 + 8 * level) )
    return health 

def get_critical_chance(level):
    critical_chance = random.randrange(5, 15 + round(level/2))
    return critical_chance

def get_armor(level):
    armor = random.randrange(round(math.log(level ** 2 + level)), round(math.log(level ** 2 +1) + 2*level+1))
    return armor

def get_critical_damage(level):
    critical_damage = random.randrange(11 + round(level/2), 15 +  round(level/2)) / 10
    return critical_damage

def get_armor_pen(level):
    armor_pen = random.randrange(0, level +1)
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
        get_damage(level), #damage
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
    # "random" stats for the boss
    boss_names_low = (
        "Slime Boss",
        "Orc",
        "Ogre",
        "Troll",
        "Giant",
        "Tavern Guard",
        "Goblin" 
    )
    
    boss_names_med = (
        "Goblin Chief",
        "Dragon",
        "Demon Chieftan",
        "Draconian Guardian",
    )
    
    boss_names_high = (
        "Draconian Lord",
        "Draconian God",
        "The Pope Himself",
        "Demon Lord",
        "Demon King",
        "Demon God"
    )
    
    #boss name
    if(game_round <= 40):
        boss_name = random.choice(boss_names_low)
    elif(game_round <= 80):
        boss_name = random.choice(boss_names_med)
    else:
        boss_name = random.choice(boss_names_high)
    
    #boss level is based on the round
    boss_level = round(game_round/5)
    
    #boss damage is based on the boss level (so based on the round)
    boss_damage = 10 + 2 * boss_level
    #boss crit chance is based on the boss level (so based on the round)
    boss_critical_chance = 10 + boss_level
    #set the boss critical damage, capped at 2.2
    boss_critical_damage = 1.0 + boss_level/50
    if(boss_critical_damage > 2.2):
        boss_critical_damage = 2.2
    #boss speed 
    boss_speed = 50 + 5 * boss_level
    #boss health
    boss_health = 60 + 11 * boss_level
    #boss armor
    boss_armor = 10 + 2 * boss_level
    #boss armor penetration
    boss_armor_pen = round(1.5 * boss_level)
    
    #create the boss
    if(game_round % 10 == 0):
        boss = enemy(
            boss_name, #name
            boss_level, #level
            boss_damage, #damage 
            boss_critical_chance, #critical chance
            boss_critical_damage, #critical damage
            boss_speed, #speed
            boss_health, #health
            boss_armor, #armor
            boss_armor_pen, #armor penetration
            "Boss" #enemy type
        )  
    else:
        print(f"\n\n\nBoss logic off. Recieved round = {str(game_round)}\n\n\n")
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
