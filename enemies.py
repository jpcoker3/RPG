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
    speed = 70
    health = 50

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

def get_enemy(level):
    unit = enemy(
        get_name(),  #name
        random.randrange(level -1, level +1), #level
        (5*level)+5, #damage
        random.randrange(50, 150), #speed
        random.randrange(4*level + 1, 12*level+2) #health
    )
    
    
    return unit