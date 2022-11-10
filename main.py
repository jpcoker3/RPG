import random
import weapons
from weapons import weapon 
import armors
from armors import armor

#GLOBAL VARS
world_name = 'Placeholder'
classes = {
        1:'Warrior', 
        2:'Wizard', 
        3:'Rogue', 
        }

#Get weapons and armor from files
weapon_list = []
for weapon in weapons.get_weapons():
    weapon_list.append(weapon)
#print(weapon_list[0].name + str(weapon_list[0].damage))
    
armor_list = []
for armor in armors.get_armors():
    armor_list.append(armor)

 
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
    class_char_create = {
        1:['Warrior', "+ 50 HP, +15 Armor"], 
        2:['Wizard', "+ 75 Mana"], 
        3:['Rogue', "+ 15 Speed, + 50 Stamina"]
        }
    player.name = get_name('Welcome to the game! please enter a name to begin: ')
    
    print("\nTime to choose a class! Here are your options: ")                                             
    print("\n{:<10} {:<10} {:<10}".format('Choice', 'Name', 'Information'))
    for key, value in class_char_create.items():
        name, information = value
        print("{:<10} {:<10} {:25}".format(key, name, information))
    
    choice = input('\nWhat class would you like to be? ')
    
    while (int(choice) > 3):
        choice = input("\nPlease enter a valid option between 1 and 3")

    char_type(player,classes[int(choice)])
    
    print('Here are your stats: \n') 
    print("{:<10} {:<10}".format('Name', 'Value'))
    for stat, val in player.stats.items():
        print("{:<10} {:<10}".format(stat, val))
    print("\n")
    
#choose char types    
def char_type( player, class_type):
    player.char_type = class_type
    # Warior
    if class_type == "Warrior": 
        player.stats["Health"] += 50
        player.stats["Armor"] += 15
        
    # Wizzard
    elif class_type == "Wizard":
        player.stats["Mana"] += 75
        
    # Rogue
    elif class_type == "Rogue":
        player.stats["Speed"] += 15
        player.stats["Stamina"] += 50


#holds all character info
class char_info():
    stats = {
        "Health" : 100,
        "Mana": 100,
        "Stamina": 100,
        "Armor": 0,
        "Speed": 100,
        "Level": 0 
    }
    name = 'EMPTY'
    char_type = 'EMPTY'
    gold_balance = 0
    
    inventory = {
        
    }
   
def encounter(player):
    options = ['Nothing', 'Item', 'Enemy']
    encounter = random.choices(options, weights = (20, 20, 60), k = 3)
    if(encounter == 'Nothing'):
        print(" take a moment to rest .... +10 Health")

        input()
         
    elif (encounter == 'Item'):
        print("Item Encounter")
        input()

    elif (encounter == 'Enemy'):
        enemy_defeated = False
        print("Enemy Encounter")
        
        
        if(enemy_defeated == False):enemy_defeated = True
        if(enemy_defeated == True):
            gold = random.randrange(player.stats["Level"]+1, 5*(player.stats["Level"]+1))

            print("Enemy defeated! Obtained " + str(gold) + " gold!")
            player.gold_balance += gold
            
        input()
        
        
    else:
        print("i guess you are unlucky")
        player.stats["Health"] = 0
        counter += 1000
        
        
#main loop
def main():
    
    
    
    game_active = True
    #player
    player = char_info()
    #get name of player
    char_create(player)
    player.name = player.name + " The " + player.char_type
    print('Welcome to ' + world_name + ', ' + player.name +'!')
    
    # now we need to have the main game loop
    counter = 1
    while game_active:
        if(player.stats["Health"] <= 0): game_active = False  # haha you're dead
        
        print("Round " + str(counter) + ": ")
        if(counter % 250 == 0 ): 
            print("You win!")
            game_active = False
            input()
        elif(counter % 10 == 0):
            print("Boss Fight")
            input()
        else: encounter(player)
        
        counter += 1
        

   

main()