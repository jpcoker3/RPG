import armors
import weapons
import skills
from copy import copy

#get default weapons and armor
default_equipt = armors.get_default_armor() + weapons.get_default_weapon()

#prompts user for name and returns it. Ask prompt as parameter
def get_name(message):
     #create character by name
    name_prompt = True
    
    while (name_prompt):
        #before call, print what the name is for.  
        name = input( message)
        name = name.lower()
        name = name.capitalize()
        
        name_confirm = input('Okay! is the name ' + name + ' correct? y/n: ')
        if(name_confirm == 'y'): name_prompt = False
        else: message = ("Please enter a name: ")
            
    return name

#for any XP increase, handles lvl ups and such
def recieve_xp(player, xp):
    player.current_xp += xp
    while(player.current_xp >= player.xp_to_lvl_up):
        player.stats["Level"] += 1
        print("Level increased to " + str(player.stats["Level"])+"!")
        player.current_xp = player.current_xp - player.xp_to_lvl_up
        player.xp_to_lvl_up += 10
        lvl_up(player)
        
        
def lvl_up(player):
    bad_input = True
    
    while (bad_input) :
        
        print("{:<2}{:<20} {:<5}".format('#', 'Name', 'Value'))
        print("{:<2}{:<20} {:<5}".format("1.","Max Health", "+10"))  
        print("{:<2}{:<20} {:<5}".format("2.","Max Mana", "+10")) 
        print("{:<2}{:<20} {:<5}".format("3.","Max Stamina", "+10")) 

        choice = input("What stat would you like to increase? Please enter a number: ")
        
        if(choice == "1"):
            player.stats["Health"] += 10
            player.max_health += 10
            bad_input = False
        elif(choice == "2"):
            player.stats["Mana"] += 10
            player.max_mana += 15
            bad_input = False
        elif(choice == "3"):
            player.stats["Stamina"] += 10
            player.max_stamina += 10
            bad_input = False
        
        else:
            bad_input = True
            print("Please enter a valid number (1-3)")
    
    
    print("{:<15}{:<20}".format( 'Name', 'Value'))
    print("{:<15}{:<20}".format("Max Health", str(player.max_health)))  
    print("{:<15}{:<20} ".format("Max Mana",str(player.max_mana))) 
    print("{:<15}{:<20} ".format("Max Stamina", str(player.max_stamina)))

    skills.get_skill(player)
        

class class_type_stats:
    def __init__(self, name:str, summary:str, class_dmg_type:str, health:int = 0, mana:int = 0, stamina_regen:int = 0, mana_regen:int = 0, stamina:int = 0, armor:int = 0, speed:int = 0, luck:int = 0, regen:int = 0, critical_chance:int = 0, critical_damage:int = 0):
        self.name = name
        self.health = health
        self.mana = mana
        
        self.stamina_regen = stamina_regen
        self.mana_regen = mana_regen
        
        self.stamina = stamina
        self.armor = armor
        self.speed = speed 
        
        self.luck = luck # Increases chance of getting heigher tier weapons and abilities
        self.regen = regen # flat health heal
        self.critical_chance = critical_chance # critical chance percent
        self.critical_damage = critical_damage # critical damage multiplier, x0.00
        self.summary = summary #summary of class stat changes
        self.class_dmg_type = class_dmg_type # magic, melee, ranged, affects what items and stats you can get
      
        
#template = class_type_stats(name = "", health= 0, mana=0, stamina= 0, armor=0, speed=0, luck=0, regen=0, critical_chance=0, critical_damage=0, summary="")


#weak = class_type_stats(name = "weak", class_dmg_type = "melee", health= -80,  regen=-10,  summary="-80 HP, -10 Regen. Test Class")
#op = class_type_stats(name = "op",class_dmg_type = "melee", health= 1000,  speed=1000,  regen=1000, critical_chance=200, critical_damage=10, summary="+1000 HP, +1000 Speed, +1000 Regen, +100 crit chance, + 10 Crit Multiplier. OP test class")
peasant = class_type_stats(name = "peasant",class_dmg_type = "melee",  summary="Default Stats")
idiot = class_type_stats(name = "idiot", health= -15,class_dmg_type = "melee", speed=-15,  luck=50, summary="+50 Luck, -15 Health, -15 Speed, ")
warrior = class_type_stats(name = "warrior",class_dmg_type = "melee",health =  50,  mana = -100,armor = 20, speed = -20,regen= 20,  summary= "+50 Health, +20 Armor, +20 Regen, -100 Mana, -20 Speed" )
gambler = class_type_stats(name = "gambler",class_dmg_type = "magic",health = -25, mana = -85, stamina = -15,armor =  5,speed =  25,luck= 10, regen = 5,critical_chance= 5,critical_damage= .25, summary= "+5 Armor, +25 Speed, +10 Luck, +5 Regen, +5% Crit Chance, +.25 Crit Damage Multiplier, -25 Health, -85 Mana, -15 Stamina  ")
ranger = class_type_stats(name = "ranger", health= -15,class_dmg_type = "ranged", stamina= 15, speed=20,   regen=5, critical_chance=15, critical_damage= 0.45, summary="+15 Stamina, +20 Speed, +5 Regen, +15% Critical Chance, +0.45 Critical Multiplier, -15 Health")
defender = class_type_stats(name = "defender", health= 100,  armor=50,class_dmg_type = "melee", speed= -30,  regen=20, critical_damage= -0.50, summary= "+100 Health, +50 Armor, +20 Regen, -30 Speed, -0.5 Critical Multiplier" )

classes = [ peasant, idiot, warrior, gambler, ranger, defender]

def add_class_stats(player, class_type):
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
    
    player.name = get_name('Welcome to the game! please enter a name to begin: ')
    
    print("\nTime to choose a class! Here are your options: ")                                             
    print("\n{:<15} {:<35} ".format('Class Name', 'Summary'))
    for choice in classes:
        print("\n{:<15} {:<35} ".format(choice.name.capitalize(),  choice.summary))
    
    
    choosing_class = True
    
    
    while(choosing_class):
        class_choice = input('\nWhat class would you like to be?: ')
        for name in classes:
            if(class_choice.lower() == name.name):
                add_class_stats(player, name)
                choosing_class = False
    
    
    player.critical_chance += default_equipt[4].critical_chance
    player.critical_damage += default_equipt[4].critical_damage
    player.skills.append(copy(skills.basic_attack))
    
        
    output_stats(player)
    output_offense_stats(player)
    next = input("\nPress anything to continue: ") 

def output_stats(player):
    print('Here are your stats: \n') 
    print("Class: " + player.class_type.capitalize())
    print("{:<10} {:<10}".format('Stat', 'Value'))
    for stat, val in player.stats.items():
        print("{:<10} {:<10}".format(stat, val))
    print("{:<10} {:<10}".format("Max Health", player.max_health))  
    print("{:<10} {:<10}".format("Max Mana", player.max_mana))  
    print("{:<10} {:<10}".format("Max Stamina", player.max_stamina))  
        
def output_offense_stats(player):
    print('Here are your offensive stats: \n')
    print("{:<20} {:<10}".format('Stat', 'Value'))
    print("{:<20} {:<10}".format("Physical Damage", player.weapon.ad))
    print("{:<20} {:<10}".format("Magical Damage", player.weapon.ap))
    print("{:<20} {:<10}".format("Critical Chance", round(player.critical_chance)))
    print("{:<20} {:<10}".format("Critical Damage", round(player.critical_damage,2)))
    print("{:<20} {:<10}".format("Armor Penetration", player.weapon.armor_pen))
    

    
#holds all character info
class char_info():
    weapon = default_equipt[4]
    helmet = default_equipt[0]
    chest = default_equipt[1]
    pants = default_equipt[2]
    boots = default_equipt[3]
    
    max_health = 100
    max_mana = 100
    max_stamina = 100
    
    mana_regen = round((5* max_mana)/100)
    stamina_regen = round((5* max_stamina)/100)
    
    
    critical_chance = 0
    critical_damage = 0
    
    name = 'EMPTY'
    class_type = 'EMPTY'
    class_dmg_type = 'EMPTY'
    gold_balance = 0
    current_xp = 0
    xp_to_lvl_up = 20

    stats = {
        "Health" : 100,
        "Mana": 100,
        "Stamina": 100,
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
