import random
import weapons
from weapons import weapon 
import armors
from armors import armor
import encounters

#GLOBAL VARS
world_name = 'Placeholder'
prev_encounter = ""
classes = {
        1:'Warrior', 
        2:'Wizard', 
        3:'Rogue', 
        }


#get default weapons and armor
default_equipt = armors.get_default_armor() + weapons.get_default_weapon()

#prompts user for name and returns it. Ask prompt as parameter
def get_name(message):
     #create character by name
    name_prompt = True
    
    while name_prompt:
        #before call, print what the name is for.  
        name = input( message)
        name_confirm = input('Okay! is the name ' + name + ' correct? y/n: ')
        if(name_confirm == 'y'): name_prompt = False
        
        #incorrect name, loop until player says yes
        while name_confirm != 'y':
            name = input('Please enter a name: ')
            name_confirm = input('Okay! is the name ' + name + ' correct? y/n: ')
            #if name correct, exit loop and continue.
            if(name_confirm == 'y'): name_prompt = False
            
    return name

#create new char -- has prompts
def char_create(player):
    
    player.name = get_name('Welcome to the game! please enter a name to begin: ')
    
    print("\nTime to choose a class! Here are your options: ")                                             
    print("\n{:<10} {:<10} {:<10}".format('Choice', 'Name', 'Information'))
    for key, value in class_char_create.items():
        name, information = value
        print("{:<10} {:<10} {:25}".format(key, name, information))
    
    choice = input('\nWhat class would you like to be? ')
    
    while (int(choice) > 3):
        choice = input("\nPlease enter a valid option between 1 and 3: ")

    char_type(player,classes[int(choice)])
    
    print('Here are your stats: \n') 
    print("{:<10} {:<10}".format('Name', 'Value'))
    for stat, val in player.stats.items():
        print("{:<10} {:<10}".format(stat, val))
    print("\n")
    input()
    


#check for new skills on level up
def check_for_skills(player):
    if(player.char_type == "Warrior"):
        pass
    elif(player.char_type == "Wizard"):
        pass
    elif(player.char_type == "Rogue"):
        pass

#choose char types    
def char_type( player, class_type):
    player.char_type = class_type
    # Warior
    if class_type == "Warrior": 
        player.class_health_bonus = 50
        player.class_armor_bonus = 15
        player.class_mana_bonus = -50
        
    # Wizzard
    elif class_type == "Wizard":
        player.class_mana_bonus = 75
        player.class_stamina_bonus = -60
        
    # Rogue
    elif class_type == "Rogue":
        player.class_speed_bonus = 20
        player.class_stamina_bonus = 50
        player.class_health_bonus = -20
        
        
class_char_create = {
        1:['Warrior', "+ 50 HP, + 15 Armor, - 50 Mana"], 
        2:['Wizard', "+ 75 Mana, - 60 Stamina"], 
        3:['Rogue', "+ 20 Speed, + 50 Stamina, - 20 Health"]
        }


#holds all character info
class char_info():
    weapon = default_equipt[4]
    helmet = default_equipt[0]
    chest = default_equipt[1]
    legs = default_equipt[2]
    boots = default_equipt[3]
    
    
    class_crit_chance = 0
    class_crit_damage = 0
    class_health_bonus = 0
    class_mana_bonus = 0
    class_stamina_bonus = 0
    class_armor_bonus = 0
    class_speed_bonus = 0
    class_luck_bonus = 0
    class_regen_bonus = 0
    
    max_health = 100
    max_mana = 100
    max_stamina = 100
    critical_chance = weapon.critical_chance 
    critical_damage = weapon.critical_damage
    
    name = 'EMPTY'
    char_type = 'EMPTY'
    gold_balance = 0
    current_xp = 0
    xp_to_lvl_up = 20
    
    
    stats = {
        "Health" : 100 + class_health_bonus,
        "Mana": 100 + class_mana_bonus,
        "Stamina": 100 + class_stamina_bonus,
        "Armor": 0 + class_armor_bonus,
        "Speed": 100 + class_speed_bonus,
        "Level": 0,
        "Luck" : 0 + class_luck_bonus,
        "Regen": 5 + class_regen_bonus
    }



#main loop
def main():
    
    game_active = True
    prev_encounter = ""
    #player
    player = char_info()
    #get name of player
    char_create(player)
    player.name = player.name + " The " + player.char_type
    print('Welcome to ' + world_name + ', ' + player.name +'!')
    print("Press the return key to continue to your first day!")
    input()
    
    # now we need to have the main game loop
    counter = 1
    while game_active:
        if(player.stats["Health"] <= 0): game_active = False  # haha you're dead
        else:
            print("Round " + str(counter) + ": ")
            if(counter % 250 == 0 ): 
                print("You win!")
                game_active = False
                input()
            elif(counter % 10 == 0):
                print("Boss Fight")
                input()
            else: prev_encounter = encounters.choose_encounter(player, prev_encounter, counter)
            
            counter += 1           

main()