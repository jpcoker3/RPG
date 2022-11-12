import random
import weapons
from weapons import weapon 
import armors
from armors import armor
import enemies
from enemies import enemy

#GLOBAL VARS
world_name = 'Placeholder'
prev_encounter = ""
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
    
default_equipt = armors.get_default_armor() + weapons.get_default_weapon()


equiptment_list = weapon_list + armor_list

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
        1:['Warrior', "+ 50 HP, + 15 Armor, - 50 Mana"], 
        2:['Wizard', "+ 75 Mana, - 60 Stamina"], 
        3:['Rogue', "+ 15 Speed, + 50 Stamina, - 20 Health"]
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
    
#for any XP increase, handles lvl ups and such
def recieve_xp(player, xp):
    player.current_xp += xp
    while(player.current_xp >= player.xp_to_lvl_up):
        player.stats["Level"] += 1
        print("Level increased to " + str(player.stats["Level"])+"!")
        player.current_xp = player.current_xp - player.xp_to_lvl_up
        player.xp_to_lvl_up = player.xp_to_lvl_up * (player.stats["Level"] * 0.85)

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
        player.stats["Health"] += 50
        player.max_health +=50
        player.stats["Armor"] += 15
        player.stats["Mana"] -= 50
        player.max_mana -= 50
        
    # Wizzard
    elif class_type == "Wizard":
        player.stats["Mana"] += 75
        player.max_mana += 75
        player.stats["Stamina"] -= 60
        player.max_mana -= 60
        
    # Rogue
    elif class_type == "Rogue":
        player.stats["Speed"] += 15
        player.stats["Stamina"] += 50
        player.max_mana += 50
        player.stats["Health"] -= 20
        player.max_health -= 20

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
    max_health = 100
    max_mana = 100
    max_stamina = 100
    name = 'EMPTY'
    char_type = 'EMPTY'
    gold_balance = 0
    current_xp = 0
    xp_to_lvl_up = 20
    
    weapon = default_equipt[4]
    helmet = default_equipt[0]
    chest = default_equipt[1]
    legs = default_equipt[2]
    boots = default_equipt[3]
    
def combat(player, opponent):
    print("Player health: "+ str(player.stats["Health"]) + " Enemy health: " + str(opponent.health) )
    while((player.stats["Health"] > 0) and (opponent.health > 0)):
        player_speed = player.stats["Speed"]
        opponent_speed = opponent.speed
        #check speed, player may be able to attack twice or more before enemy attacks
        if(player_speed > opponent_speed):
            while (player_speed > opponent_speed): 
                opponent.health -= player.weapon.damage
                player_speed -= opponent_speed
                print(opponent.name + " was hit for " + str(player.weapon.damage) + ". Enemy health == " + str(opponent.health)) 
            #make sure opponent isnt dead yet
            if(opponent.health > 0):
                player.stats["Health"] -= opponent.damage
                print(player.name + " was hit for " + str(opponent.damage) + ". Player health == " + str(player.stats["Health"]))
        #and vice versa, opponent may be able to attack twice or more before player attacks
        elif(player_speed < opponent_speed):
            while (player_speed < opponent_speed): 
                player.stats["Health"] -= opponent.damage
                opponent_speed -= player.stats["Speed"]
                print(player.name + " was hit for " + str(opponent.damage) + ". Player health == " + str(player.stats["Health"]))
            #make sure opponent isnt dead yet
            if(player.stats["Health"] > 0):
                opponent.health -= player.weapon.damage
                print(opponent.name + " was hit for " + str(player.weapon.damage) + ". Enemy health == " + str(opponent.health)) 
                
    if((player.stats["Health"] > 0) and (opponent.health <= 0)):
        print("Congratulations " + player.name +"! You have defeated " + opponent.name + "!")
        return True
    else:
        print("You have died by the hands of " + opponent.name + ". Thus ends the story of " + player.name)
        return False
     
   
def encounter(player, prev_encounter, round):
    options = ['Nothing', 'Item', 'Shop', 'Enemy', 'Enemy', 'Enemy']
    
    if(round == 1):
        encounter = 'Item'
    else:
        encounter = random.choice(options)
        #make sure its not the same encounter every time
        while ((encounter == prev_encounter) and (prev_encounter != 'Enemy')):
            encounter = random.choice(options)
         
    if(encounter == 'Nothing'):
        print("take a moment to rest .... +10 Health")
        player.stats["Health"] += 10 #heal for 10
        if(player.stats["Health"] > player.max_health): player.stats["Health"] = player.max_health # if healed for more than max, set to max. (cap health)
        print("Current Health: " + str(player.stats["Health"]) + ". Max Health is: " + str(player.max_health) + ".")
        input()
         
    elif (encounter == 'Item'):
        print("Item Encounter")
        item = random.choice(equiptment_list)
        print("\nYou opened a chest and found " + item.name + "!\n")
        if(item.type == "armor"):
            print("{:<20}{:<10}".format("Level:", item.level))
            if(item.health_bonus != 0): print("{:<20}{:<10}".format("Health Bonus:", item.health_bonus))
            if(item.speed_bonus != 0): print("{:<20}{:<10}".format("Speed Bonus:", item.speed_bonus))
            if(item.stamina_bonus != 0): print("{:<20}{:<10}".format("Stamina Bonus:", item.stamina_bonus))
            if(item.armor_bonus != 0): print("{:<20}{:<10}".format("Armor Bonus:", item.armor_bonus))
            if(item.mana_bonus != 0): print("{:<20}{:<10}".format("Mana Bonus:", item.mana_bonus))
            
            equip_item = input("Would you like to equip this item? y/n: ")
            if(equip_item == "y"):
                if (item.piece == "helmet"):
                    player.helmet = item
                elif (item.piece == " chest"):
                    player.chest = item
                elif(item.piece == "legs"):
                    player.legs == item
                elif( item.piece == "boots"):
                    player.boots = item
                print("You have equipped " + item.name)
            else:
                print("The item was discarded")
            
            
        elif(item.type == "weapon"):
            print("{:<20}{:<10}".format("Level:", item.level))
            if(item.damage != 0): print("{:<20}{:<10}".format("Damage:", item.damage))
            if(item.critical_chance != 0): print("{:<20}{:<10}".format("Critical Chance:", item.critical_chance))
            if(item.critical_damage != 0): print("{:<20}{:<10}".format("Critical Damage:", item.critical_damage))
            
            equip_item = input("Would you like to equip this item? y/n: ")
            if(equip_item == 'y'):
                player.weapon = item
                print("You have equipped " + item.name)
            elif(equip_item == 'n'):
                print("The item was discarded")
            
            
        input()

    elif (encounter == 'Enemy'):
        enemy_defeated = False
        print("Enemy Encounter")
        opponent = enemies.get_enemy(player)
        enemy_defeated = combat(player, opponent)
        
        if(enemy_defeated == True):
            xp = random.randrange(player.stats["Level"]+5, 2*(player.stats["Level"]+5))
            gold = random.randrange(player.stats["Level"]+1, 5*(player.stats["Level"]+1))

            print("Enemy defeated! Obtained " + str(gold) + " gold and " + str(xp) + "xp!")
            player.gold_balance += gold
            recieve_xp(player, xp)
        input()
    
    elif(encounter == 'Shop'):
        print("Shop time")
        input()
        
    else:
        print("Well something messed up")
        
    return encounter
        
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
            else: prev_encounter = encounter(player, prev_encounter, counter)
            
            counter += 1
            

main()