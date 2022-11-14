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
      
        
    #health mana stamina armor speed level luck regen crit chance, crit damage
warrior = class_type_stats("warrior", 50, -50, 0, 15, 0, 0, 0, 10, 0, 0, "+ 50 Health, - 50 Mana, + 15 Armor, +10 Regen" )
wizzard = class_type_stats("wizzard", 0, 50, -30, 0, 30, 0, 20, 15, 0, 0, "+ 50 Mana, - 30 Stamina, + 30 Speed, + 20 Luck, + 15 Regen" )

classes = [warrior, wizzard]

def add_class_stats(player, class_type):
    player.class_type = class_type.name
    
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
        print("\n{:<15} {:<35} ".format(choice.name,  choice.summary))
    
    
    choosing_class = True
    
    
    while(choosing_class):
        class_choice = input('\nWhat class would you like to be? (lowercase): ')
        for name in classes:
            if(class_choice == name.name):
                add_class_stats(player, name)
                choosing_class = False
        
        
    print('Here are your stats: \n') 
    print("{:<10} {:<10}".format('Name', 'Value'))
    for stat, val in player.stats.items():
        print("{:<10} {:<10}".format(stat, val))
    input()
    

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
    legs = default_equipt[2]
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
        "Level": 0,
        "Luck" : 0,
        "Regen": 5
    }
