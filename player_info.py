import armors
import weapons

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
        player.xp_to_lvl_up += 40
        lvl_up(player)
        
        
def lvl_up(player):
    bad_input = True
    
    while (bad_input) :
        
        print("{:<2}{:<20} {:<5}".format('#', 'Name', 'Value'))
        print("{:<2}{:<20} {:<5}".format("1.","Health", "+15"))  
        print("{:<2}{:<20} {:<5}".format("2.","Mana", "+10")) 
        print("{:<2}{:<20} {:<5}".format("3.","Stamina", " +10")) 
        print("{:<2}{:<20} {:<5}".format("4.","Armor", "+10")) 
        print("{:<2}{:<20} {:<5}".format("5.","Speed", "+10")) 
        print("{:<2}{:<20} {:<5}".format("6.","Luck", "+5")) 
        print("{:<2}{:<20} {:<5}".format("7.","Regen", "+5")) 
        print("{:<2}{:<20} {:<5}".format("8.","Critical Chance", "+5%"))
        print("{:<2}{:<20} {:<5}".format("9.","Critical Damage", "+0.15")) 
        
        choice = input("What stat would you like to increase? Please enter a number: ")
        
        if(choice == "1"):
            player.stats["Health"] += 15
            player.max_health += 15
            bad_input = False
        elif(choice == "2"):
            player.stats["Mana"] += 10
            player.max_mana += 15
            bad_input = False
        elif(choice == "3"):
            player.stats["Stamina"] += 10
            player.max_stamina += 15
            bad_input = False
        elif(choice == "4"):
            player.stats["Armor"] += 10
            bad_input = False
        elif(choice == "5"):
            player.stats["Speed"] += 10
            bad_input = False
        elif(choice == "6"):
            player.stats["Luck"] += 5
            bad_input = False
        elif(choice == "7"):
            player.stats["Regen"] += 5
            bad_input = False
        elif(choice == "8"):
            player.critical_chance += 5
            bad_input = False
        elif(choice == "9"):
            player.critical_damage += 0.15
            bad_input = False
        else:
            bad_input = True
            print("Please enter a valid number (1-9)")
    
    output_stats(player)
    print("\n")
    output_offense_stats(player)
        

class class_type_stats:
    def __init__(self, name, health, mana, stamina, armor, speed, level, luck, regen, critical_chance, critical_damage, summary):
        self.name = name
        self.health = health
        self.mana = mana
        self.stamina = stamina
        self.armor = armor
        self.speed = speed
        self.level = level
        self.luck = luck
        self.regen = regen
        self.critical_chance = critical_chance
        self.critical_damage = critical_damage
        self.summary = summary
      
        
#template = class_type_stats(name = "", health= 0, mana=0, stamina= 0, armor=0, speed=0, level=0, luck=0, regen=0, critical_chance=0, critical_damage=0, summary="")


warrior = class_type_stats(name = "warrior",health =  50,  mana = -100,stamina =  0,armor = 20, speed = -20,level= 0,luck= 0,regen= 20,critical_chance= 0,critical_damage= 0,  summary= "+50 Health, +20 Armor, +20 Regen, -100 Mana, -20 Speed" )
gambler = class_type_stats(name = "gambler",health = -25, mana = -85, stamina = -15,armor =  5,speed =  25,level= 0,luck= 10, regen = 10,critical_chance= 15,critical_damage= .25, summary= "+5 Armor, +25 Speed, +10 Luck, +10 Regen, +15% Crit Chance, +.25 Crit Damage Multiplier, -25 Health, -85 Mana, -15 Stamina  ")



classes = [warrior, gambler]

def add_class_stats(player, class_type):
    player.class_type = class_type.name.capitalize()
    
    player.max_health += class_type.health
    player.stats["Health"] += class_type.health
    
    player.max_mana += class_type.mana
    player.stats["Mana"] += class_type.mana
    
    player.max_stamina += class_type.stamina
    player.stats["Stamina"] += class_type.stamina
    
    player.stats["Armor"] += class_type.armor
    player.stats["Speed"] += class_type.speed
    player.stats["Level"] += class_type.level
    player.stats["Luck"] += class_type.luck
    player.stats["Regen"] += class_type.regen
    
    player.critical_chance += class_type.critical_chance
    player.critical_damage += class_type.critical_damage
    
    

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
    
        
    output_stats(player)
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
    print("{:<20} {:<10}".format("Damage", player.weapon.damage))
    print("{:<20} {:<10}".format("Critical Chance", player.critical_chance))
    print("{:<20} {:<10}".format("Critical Damage", player.critical_damage))
    print("{:<20} {:<10}".format("Armor Penetration", player.weapon.armor_pen))
    
    
#check for new skills on level up
def check_for_skills(player):
    if(player.char_type == "Warrior"):
        pass
    elif(player.char_type == "Wizard"):
        pass
    elif(player.char_type == "Rogue"):
        pass
    
    
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
    critical_chance = 0
    critical_damage = 0
    
    name = 'EMPTY'
    class_type = 'EMPTY'
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
        "Regen": 5
    }
    
    skills = {
        # to be implemented later
        #slash,
        #lunge,
        #etc
    }
