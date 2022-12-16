import armors
import weapons
import skills
from copy import copy
from dataclasses import dataclass

#get default weapons and armor
default_equipt = armors.get_default_armor() + weapons.get_default_weapons()

#prompts user for name and returns it. Ask prompt as parameter
def get_name(message):
     #create character by name
    name = input( message)
    name = name.lower()
    name = name.capitalize()
    
    return name

#for any XP increase, handles lvl ups and such
def recieve_xp(player, xp):
    player.current_xp += xp
    while(player.current_xp >= player.xp_to_lvl_up):
        player.stats["Level"] += 1
        print("Level increased to " + str(player.stats["Level"])+"!")
        player.current_xp = player.current_xp - player.xp_to_lvl_up
        player.xp_to_lvl_up += 7
        lvl_up(player)
        
        
#handles level up
def lvl_up(player):
    if(player.class_dmg_type == "any"):
        player.max_stamina += 5
        player.max_mana += 5
        player.max_health += 10
        print("You have leveled up! You have gained 5 Stamina, 5 Mana, and 10 Health!")
    elif(player.class_dmg_type == "melee"):
        player.max_stamina += 10
        player.max_health += 15
        print("You have leveled up! You have gained 10 Stamina and 15 Health!")
    elif(player.class_dmg_type == "ranged"):
        player.max_stamina += 10
        player.max_health += 15
        print("You have leveled up! You have gained 10 Stamina and 15 Health!")
    elif(player.class_dmg_type == "magic"):
        player.max_mana += 10
        player.max_health += 15
        print("You have leveled up! You have gained 10 Mana and 15 Health!")

    skills.get_skill(player)
        
        
#handles class data, all optional except name, summary, and class_dmg_type
  
@dataclass
class class_type_stats:
    name:str
    summary:str  #summary of class stat changes
    class_dmg_type:str  # magic, melee, ranged,any. affects what items and stats you can get
    health:int = 0
    mana:int = 0 #default 50
    mana_regen:int = 0 #starts at 50
    stamina:int = 0 #default 50
    stamina_regen:int = 0 #starts at 50
    armor:int = 0 #default 0
    speed:int = 0 #default 100
    luck:int = 0 # Increases chance of getting heigher tier weapons and abilities
    regen:int = 0 # heal at end of encounter, default 0. 
    critical_chance:int = 0 # critical chance percent
    critical_damage:int = 0 # critical damage multiplier, x0.00
   
   
   
        
#template = class_type_stats(name = "", health= 0, mana=0, stamina= 0, armor=0, speed=0, luck=0, mana_regen = 0, stamina_regen = 0, regen=0, critical_chance=0, critical_damage=0, class_dmg_type = "", summary="")

peasant = class_type_stats(name = "peasant",class_dmg_type = "all",  summary="Default Stats")
idiot = class_type_stats(name = "idiot", health= -15,class_dmg_type = "all", speed=-15,  luck=50, summary="+50 Luck, -15 Health, -15 Speed, ")
warrior = class_type_stats(name = "warrior",class_dmg_type = "melee",health =  50,armor = 20, speed = -20,regen= 20,  summary= "+50 Health, +20 Armor, +20 HP Regen, -20 Speed" )
gambler = class_type_stats(name = "gambler",class_dmg_type = "magic",health = -25,armor =  5,speed =  25,luck= 10,critical_chance= 10,critical_damage= -.5, summary= "+5 Armor, +25 Speed, +10 Luck, +10% Crit Chance, -0.5 Crit Damage Multiplier, -25 Health ")
ranger = class_type_stats(name = "ranger", health= -15,class_dmg_type = "ranged",stamina_regen=5, stamina= 20, speed=20, critical_chance=15, critical_damage= 0.45, summary="+20 Stamina, +20 Speed, +5 Stamina Regen, +15% Critical Chance, +0.45 Critical Multiplier, -15 Health")
defender = class_type_stats(name = "defender", health= 100,  armor=50,class_dmg_type = "melee", speed= -30,  regen=20, critical_damage= -0.65, summary= "+100 Health, +50 Armor, +20 HP Regen, -30 Speed, -0.65 Critical Multiplier" )
wizzard = class_type_stats(name = "wizzard",class_dmg_type = "magic", mana=25,health =10, luck=15, mana_regen = 10, summary="+25 Mana, +10 Health, +10 Mana Regen, +15 Luck")


classes = [ peasant, idiot, warrior, gambler, ranger, defender,wizzard]

def add_class_stats(player, class_type):
    if(class_type.class_dmg_type == "melee"):
        class_type.mana = -50
    elif(class_type.class_dmg_type == "ranged"):
        class_type.mana = -50
    elif(class_type.class_dmg_type == "magic"):
        class_type.stamina = -50
    elif(class_type.class_dmg_type == "any"):
        class_type.mana = -25
        class_type.stamina = -25
    
    player.class_type = class_type.name.capitalize()
    player.class_dmg_type = class_type.class_dmg_type
    
    player.max_health += class_type.health
    player.stats["Health"] += class_type.health
    
    player.max_mana += class_type.mana
    player.stats["Mana"] += class_type.mana
    
    player.mana_regen += class_type.mana_regen
    player.stamina_regen += class_type.stamina_regen
    
    player.max_stamina += class_type.stamina
    player.stats["Stamina"] += class_type.stamina
    
    player.stats["Armor"] += class_type.armor
    player.stats["Speed"] += class_type.speed
    player.stats["Luck"] += class_type.luck
    player.stats["Regen"] += class_type.regen
    
    player.critical_chance += class_type.critical_chance
    player.critical_damage += round(class_type.critical_damage,2)
    
    

#create new char -- has prompts
def char_create(player):
    
    #get name
    player.name = get_name('Welcome to the game! please enter a name to begin: ')
    
    #choose class
    print("\nTime to choose a class! Here are your options: ")                                             
    print("\n{:<15}{:<10}{:<35} ".format('Class Name','Type', 'Summary'))
    for choice in classes:
        print("\n{:<15}{:<10}{:<35} ".format(choice.name.capitalize(), choice.class_dmg_type.capitalize(), choice.summary))
    #loop until valid class is chosen
    choosing_class = True
    while(choosing_class):
        class_choice = input('\nWhat class would you like to be?: ')
        for name in classes:
            if(class_choice.lower() == name.name):
                add_class_stats(player, name)
                choosing_class = False
    
    #get default weapon depending on class damage type
    if(player.class_dmg_type == "any"):
        player.weapon = copy(default_equipt[4]) #stick
    elif(player.class_dmg_type == "melee"):
        player.weapon = copy(default_equipt[5]) #rusty_butter_knife
    elif(player.class_dmg_type == "ranged"):
        player.weapon = copy(default_equipt[6]) #slingshot
    elif(player.class_dmg_type == "magic"):
        player.weapon = copy(default_equipt[7]) #magic_stick
        
    
    player.critical_chance += player.weapon.critical_chance
    player.critical_damage += player.weapon.critical_damage
    player.skills.append(copy(skills.basic_attack)) #add basic attack skill
    
        
    output_stats(player)
    print("\n")
    output_offense_stats(player)
    next = input("\nPress anything to continue: ") 

#output stats
def output_stats(player):
    print('Here are your stats: \n') 
    print("Class: " + player.class_type.capitalize()) #god I love using capitalize
    print("{:<12} {:<10}".format('Stat', 'Value'))
    for stat, val in player.stats.items():
        if(val >0):  #only print stats that are greater than 0, applies to mana and stamina
            print("{:<12} {:<10}".format(stat, val))
    print("{:<12} {:<10}".format("Max Health", player.max_health))  
    
    #same from comment above, mana and stamina are a little funky so only print relevant info
    if(player.max_mana > 0):
        print("{:<12} {:<10}".format("Max Mana", player.max_mana))  
    if(player.max_stamina > 0):
        print("{:<12} {:<10}".format("Max Stamina", player.max_stamina))  
        
#output offensive stats
def output_offense_stats(player):
    print('Here are your offensive stats:')
    print("{:<20} {:<10}".format('Stat', 'Value'))
    if(player.weapon.ad > 0):
        print("{:<20} {:<10}".format("Physical Damage", player.weapon.ad))
    if(player.weapon.ap > 0):
        print("{:<20} {:<10}".format("Magical Damage", player.weapon.ap))
    print("{:<20} {:<10}".format("Critical Chance", round(player.critical_chance)))
    print("{:<20} {:<10}".format("Critical Damage", round(player.critical_damage,2)))
    print("{:<20} {:<10}".format("Armor Penetration", player.weapon.armor_pen))
    

    
#holds all character info
class char_info():
    weapon = None
    helmet = default_equipt[0]
    chest = default_equipt[1]
    pants = default_equipt[2]
    boots = default_equipt[3]
    
    max_health = 100
    max_mana = 50
    max_stamina = 50
    
    mana_regen = 5
    stamina_regen = 5
    
    
    critical_chance = 0
    critical_damage = 0
    
    name = 'EMPTY'
    class_type = 'EMPTY'
    class_dmg_type = 'EMPTY'
    gold_balance = 0
    current_xp = 0
    xp_to_lvl_up = 10

    stats = {
        "Health" : 100,
        "Mana": 50,
        "Stamina": 50,
        "Armor": 0,
        "Speed": 100,
        "Level": 1,
        "Luck" : 0,
        "Regen": 0
    }
    
    skills = [
        
        # to be implemented later
        #slash,
        #lunge,
        #etc
    ]
