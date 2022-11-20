import random
import weapons
import armors
import enemies
import combat
import player_info
from copy import copy
import random


items = ["weapon", "armor"]

def choose_rarity(player):
    #level locked rarity
    if(player.stats["Level"] < 5):
        rarity = random.randrange(player.stats["Luck"],84)
    elif(player.stats["Level"] < 10):
        rarity = random.randrange(player.stats["Luck"],94)
    else:
        rarity = random.randrange(player.stats["Luck"],100)
        
    if(rarity <= 70):loot_rarity = "common"
    elif(rarity <= 85): loot_rarity = "uncommon"
    elif(rarity <= 95): loot_rarity = "rare"
    elif(rarity <= 99.5): loot_rarity = "legendary"
    elif(rarity > 99.5): loot_rarity = "mythic" 
    
    return loot_rarity
    
    
def loot_item(player):
    #choose item and rarity
    loot_rarity = choose_rarity(player)
    loot_type = random.choice(items)
        
    #if weapon, get weapon. if armor, get armor. pretty easy
    if(loot_type == "weapon"): item = weapons.get_weapon(player, loot_rarity)
    elif(loot_type == "armor"): item = armors.get_armor(player, loot_rarity)
    
    return item


#choose an encounter from list    
def choose_encounter(player, prev_encounter, game_round):
    
    encounter_list = ['Camp', 'Item', 'Enemy'] 
    # get a weighted list of encounters to choose from -- easier to modify
    options = random.choices(encounter_list, weights=(20, 20, 50), k=100) 

    
    if(game_round == 1):
        encounter = 'Item'
    elif(game_round == 2):
        encounter = 'Enemy'
    elif(game_round == 3):
        encounter = 'Enemy'
    elif(game_round == 4):
        encounter = 'Camp'
    elif(game_round == 5):
        encounter = 'Enemy'
    elif(game_round == 6):
        encounter = 'Item'
    elif(game_round == 7):
        encounter = 'Camp'
    elif(game_round == 8):
        encounter = 'Enemy'
    else:
        encounter = random.choice(options)
        #make sure its not the same encounter every time
        while ((encounter == prev_encounter) and (prev_encounter != 'Enemy')):
            encounter = random.choice(options)
         
    if(encounter == 'Camp'):
        print("You found a camp! You decide take a moment to rest .... ")
        
        heal_value = round(3 * (player.max_health)/ 10)
        
        #basically, calculate how much to heal ( if any)
        heal_total = heal_value + player.stats["Health"]
        if(heal_total > player.max_health):
            temp = heal_total - player.max_health
            heal_value -= temp
            if(heal_value < 0): heal_value =0
            
            
        print("Gained " + str(heal_value) + " Health")
        player.stats["Health"] += heal_value #heal for 10%
        if(player.stats["Health"] > player.max_health): player.stats["Health"] = player.max_health # if healed for more than max, set to max. (cap health)
        print("Current Health: " + str(player.stats["Health"]) + ". Max Health is: " + str(player.max_health) + ".")
        next = input("\nPress anything to continue: ") 

    #free item! congrats
    elif (encounter == 'Item'):
        print("Item Encounter")
        
        item = loot_item(player)

        # output armor or weapon w stats and ask to equip or not
        
        gold = random.randrange(player.stats["Level"]+ 10, 2*(player.stats["Level"])+10)
        gold += round(gold * (player.stats["Luck"] / 100))
        player.gold_balance += gold 
        
        print("You found a chest ....")
        print("Found: " + str(gold) + " gold in the chest. Current gold: " + str(player.gold_balance) )
        
        ask_player_item(player, item)
        

 
        
        # give user a sec to take in info and continue
        next = input("\nPress anything to continue: ") 

    elif (encounter == 'Enemy'):
        enemy_defeated = False
        print("Enemy Encounter")
        opponent = enemies.get_enemy(player)
        enemy_defeated = combat.battle(player, opponent)
        
        if(enemy_defeated == True):
            xp = random.randrange(player.stats["Level"] +8, 2*(player.stats["Level"])+9)
            xp += round(xp* (player.stats["Luck"] / 100))
            
            gold = random.randrange(player.stats["Level"]+5, 3*(player.stats["Level"])+5)
            gold += round(gold * (player.stats["Luck"] /100))
            

            print("Enemy defeated! Obtained " + str(gold) + " gold and " + str(xp) + "xp!")
            player.gold_balance += gold
            player_info.recieve_xp(player, xp)
        next = input("\nPress anything to continue: ") 
        
    else:
        print("Well something messed up")
        
    return encounter


def ask_player_item(player, item):
    print(f"\nItem found: {item.name}")
    if(item.type == "armor"):
            
            if (item.piece == "helmet"):
                print(f"Current Item: {player.helmet.name}\n")
                print("{:<20}{:<20}{:<20}".format(" ", "New Item", "Current Item"))
                print("{:<20}{:<20}{:<20}".format(" ", item.name, player.helmet.name))
                print("{:<20}{:<20}{:<20}".format("Level: ", item.level, player.helmet.level))
                print("{:<20}{:<20}{:<20}".format("Rarity: ", item.rarity, player.helmet.rarity))
                print("{:<20}{:<20}{:<20}".format("Health Bonus: ", item.health_bonus, player.helmet.health_bonus))
                print("{:<20}{:<20}{:<20}".format("Speed Bonus: ", item.speed_bonus, player.helmet.speed_bonus))
                print("{:<20}{:<20}{:<20}".format("Stamina Bonus: ", item.stamina_bonus, player.helmet.stamina_bonus))
                print("{:<20}{:<20}{:<20}".format("Armor Bonus: ", item.armor_bonus, player.helmet.armor_bonus))
                print("{:<20}{:<20}{:<20}".format("Mana Bonus: ", item.mana_bonus, player.helmet.mana_bonus))
                print("{:<20}{:<20}{:<20}".format("Regen Bonus: ", item.regen_bonus, player.helmet.regen_bonus))
                
                
            elif (item.piece == "chest"):
                print(f"Current Item: {player.chest.name}\n")
                print("{:<20}{:<20}{:<20}".format(" ", "New Item", "Current Item"))
                print("{:<20}{:<20}{:<20}".format(" ", item.name, player.chest.name))
                print("{:<20}{:<20}{:<20}".format("Level: ", item.level, player.chest.level))
                print("{:<20}{:<20}{:<20}".format("Rarity: ", item.rarity, player.chest.rarity))
                print("{:<20}{:<20}{:<20}".format("Health Bonus: ", item.health_bonus, player.chest.health_bonus))
                print("{:<20}{:<20}{:<20}".format("Speed Bonus: ", item.speed_bonus, player.chest.speed_bonus))
                print("{:<20}{:<20}{:<20}".format("Stamina Bonus: ", item.stamina_bonus, player.chest.stamina_bonus))
                print("{:<20}{:<20}{:<20}".format("Armor Bonus: ", item.armor_bonus, player.chest.armor_bonus))
                print("{:<20}{:<20}{:<20}".format("Mana Bonus: ", item.mana_bonus, player.chest.mana_bonus))
                print("{:<20}{:<20}{:<20}".format("Regen Bonus: ", item.regen_bonus, player.chest.regen_bonus))
                
            elif(item.piece == "pants"):
                print(f"Current Item: {player.pants.name}\n")
                print("{:<20}{:<20}{:<20}".format(" ", "New Item", "Current Item"))
                print("{:<20}{:<20}{:<20}".format(" ", item.name, player.pants.name))
                print("{:<20}{:<20}{:<20}".format("Level: ", item.level, player.pants.level))
                print("{:<20}{:<20}{:<20}".format("Rarity: ", item.rarity, player.pants.rarity))
                print("{:<20}{:<20}{:<20}".format("Health Bonus: ", item.health_bonus, player.pants.health_bonus))
                print("{:<20}{:<20}{:<20}".format("Speed Bonus: ", item.speed_bonus, player.pants.speed_bonus))
                print("{:<20}{:<20}{:<20}".format("Stamina Bonus: ", item.stamina_bonus, player.pants.stamina_bonus))
                print("{:<20}{:<20}{:<20}".format("Armor Bonus: ", item.armor_bonus, player.pants.armor_bonus))
                print("{:<20}{:<20}{:<20}".format("Mana Bonus: ", item.mana_bonus, player.pants.mana_bonus))
                print("{:<20}{:<20}{:<20}".format("Regen Bonus: ", item.regen_bonus, player.pants.regen_bonus))
                
            elif( item.piece == "boots"):
                print(f"Current Item: {player.boots.name}\n")
                print("{:<20}{:<20}{:<20}".format(" ", "New Item", "Current Item"))
                print("{:<20}{:<20}{:<20}".format(" ", item.name, player.boots.name))
                print("{:<20}{:<20}{:<20}".format("Level: ", item.level, player.boots.level))
                print("{:<20}{:<20}{:<20}".format("Rarity: ", item.rarity, player.boots.rarity))
                print("{:<20}{:<20}{:<20}".format("Health Bonus: ", item.health_bonus, player.boots.health_bonus))
                print("{:<20}{:<20}{:<20}".format("Speed Bonus: ", item.speed_bonus, player.boots.speed_bonus))
                print("{:<20}{:<20}{:<20}".format("Stamina Bonus: ", item.stamina_bonus, player.boots.stamina_bonus))
                print("{:<20}{:<20}{:<20}".format("Armor Bonus: ", item.armor_bonus, player.boots.armor_bonus))
                print("{:<20}{:<20}{:<20}".format("Mana Bonus: ", item.mana_bonus, player.boots.mana_bonus))
                print("{:<20}{:<20}{:<20}".format("Regen Bonus: ", item.regen_bonus, player.boots.regen_bonus))
           
            
            equip_item = input("\nWould you like to equip this item? y/n: ")
            if(equip_item == "y"):
                #item_to_be_equip = armors.armor("",0, 0, 0, 0, 0, 0,0,0, "", "") 
                item_to_be_equip = copy(item)
                
                new_armor(player, item_to_be_equip)
                
                if (item_to_be_equip.piece == "helmet"):
                    player.helmet = item_to_be_equip
                elif (item_to_be_equip.piece == "chest"):
                    player.chest = item_to_be_equip
                elif(item_to_be_equip.piece == "pants"):
                    player.pants = item_to_be_equip
                elif( item_to_be_equip.piece == "boots"):
                    player.boots = item_to_be_equip
                print("You have equipped " + item_to_be_equip.name)
                player_info.output_stats(player)
                
            else:
                print("The item was discarded")
            
    elif(item.type == "weapon"):
        
        print(f"Current Item: {player.weapon.name}\n")
        print("{:<20}{:<20}{:<20}".format(" ", "New Item", "Current Item"))
        print("{:<20}{:<20}{:<20}".format(" ", item.name, player.weapon.name))
        print("{:<20}{:<20}{:<20}".format("Level: ", item.level, player.weapon.level))
        print("{:<20}{:<20}{:<20}".format("Rarity: ", item.rarity, player.weapon.rarity))
        
        print("{:<20}{:<20}{:<20}".format("Physical Damage: ", item.ad, player.weapon.ad))
        print("{:<20}{:<20}{:<20}".format("Magical Damage: ", item.ap, player.weapon.ap))
        print("{:<20}{:<20}{:<20}".format("critical Chance: ", item.critical_chance, player.weapon.critical_chance))
        print("{:<20}{:<20}{:<20}".format("Critical Damage: ", round(item.critical_damage), round(player.weapon.critical_damage)))
        print("{:<20}{:<20}{:<20}".format("Armor Penetration: ", item.armor_pen, player.weapon.armor_pen))
        
            
        equip_item = input("\nWould you like to equip this item? y/n: ")
        if(equip_item == 'y'):
            item_to_be_equip = copy(item)
            player.critical_chance -= player.weapon.critical_chance
            player.critical_damage -= player.weapon.critical_damage
            
            player.weapon = item_to_be_equip
            
            player.critical_chance += player.weapon.critical_chance
            player.critical_damage += player.weapon.critical_damage
            
            print("You have equipped " + player.weapon.name)
            
            player_info.output_offense_stats(player)
        elif(equip_item == 'n'):
            print("The item was discarded")
            
        
def boss_encounter(player, game_round):
    boss = enemies.get_boss(game_round)
    
    outcome = combat.battle(player, boss)
    
    #if player won the battle
    if(outcome == True):
        item = loot_item(player)
        ask_player_item(player, item)
        
        xp = random.randrange(2* player.stats["Level"]+20, 4*(player.stats["Level"])+20)
        xp += round(xp* (player.stats["Luck"] / 100))
        
        gold = random.randrange(player.stats["Level"]+20, 3*(player.stats["Level"]+20))
        gold += round(gold * (player.stats["Luck"] /100))
        

        print("Enemy defeated! Obtained " + str(gold) + " gold and " + str(xp) + "xp!")
        player.gold_balance += gold
        player_info.recieve_xp(player, xp)
    
    return

def shop_encounter(player, game_round):
    
    heal_cost = round(game_round + pow(player.stats["Level"], 2))
    item_cost = round(1.5* game_round + pow(player.stats["Level"],2) /2)
    
    print("You have encountered a Mysterious stranger selling goods and services for gold.\n")
    
    
    shopping = True
    #generate offers. 
    while(shopping):
        print("\nYou have: " + str(player.gold_balance) + " Gold")
        print("Offers:")
        print("{:<30}{:<5}{:<4}".format("1. Heal for 30% Health ", "Cost:", heal_cost))
        print("{:<30}{:<5}{:<4}".format("2. Obtain Random Armor", "Cost:", item_cost))
        print("{:<30}{:<5}{:<4}".format("3. Obtain Random Weapon", "Cost:", item_cost))
        print("{:<30}".format("4. Exit"))
        choice = input("What would you like to do? : ")
        
        
        
        if(choice == "1"):
            if(player.gold_balance >= heal_cost):
                player.gold_balance -= heal_cost
                heal = round( player.max_health * .30)
                player.stats["Health"] += heal
                if(player.stats["Health"] > player.max_health):player.stats["Health"] = player.max_health
                
                print("You were healed for: " + str(heal) + " Health. Current Health is: " + str(player.stats["Health"]) + " / " + str(player.max_health))
            else:
                print("You do not have enough money to do this.")   
                
                
        elif(choice == "2"):
            if(player.gold_balance >= item_cost):
                shop_item_rarity = choose_rarity(player)
                player.gold_balance -= item_cost
                item = armors.get_armor(player, shop_item_rarity)
                ask_player_item(player, item)
            else:
                print("You do not have enough money to do this.")
                             
        elif(choice == "3"):
            if(player.gold_balance >= item_cost):
                shop_item_rarity = choose_rarity(player)
                player.gold_balance -= item_cost
                item = weapons.get_weapon(player, shop_item_rarity)
                ask_player_item(player, item)
            else:
                print("You do not have enough money to do this.")
        elif(choice == "4"):
            print("You leave the shop, the mysterious stranger gives you an odd look.\n")
            shopping = False
        
    return

    #do new armor math
def new_armor(player, item):
    sub_stats(player, item)
    add_stats(player, item)
    #subtract old armor piece stats
def sub_stats(player, item):
    if(item.piece == "helmet"):
        player.max_health -= player.helmet.health_bonus
        player.stats["Health"] -= player.helmet.health_bonus
        
        player.max_mana -= player.helmet.mana_bonus
        player.stats["Mana"] -= player.helmet.mana_bonus
        
        player.max_stamina -= player.helmet.stamina_bonus
        player.stats["Stamina"] -= player.helmet.stamina_bonus
        
        player.stats["Armor"] -= player.helmet.armor_bonus
        player.stats["Speed"] -= player.helmet.speed_bonus
        player.stats["Luck"] -= player.helmet.luck_bonus
        player.stats["Regen"] -= player.helmet.regen_bonus
        player.mana_regen -= player.helmet.mana_regen_bonus
        player.stamina_regen -= player.helmet.stamina_regen_bonus
        
    elif(item.piece == "chest"):
        player.max_health -= player.chest.health_bonus
        player.stats["Health"] -= player.chest.health_bonus
        
        player.max_mana -= player.chest.mana_bonus
        player.stats["Mana"] -= player.chest.mana_bonus
        
        player.max_stamina -= player.chest.stamina_bonus
        player.stats["Stamina"] -= player.chest.stamina_bonus
        
        player.stats["Armor"] -= player.chest.armor_bonus
        player.stats["Speed"] -= player.chest.speed_bonus
        player.stats["Luck"] -= player.chest.luck_bonus
        player.stats["Regen"] -= player.chest.regen_bonus
        player.mana_regen -= player.chest.mana_regen_bonus
        player.stamina_regen -= player.chest.stamina_regen_bonus
        
    elif(item.piece == "pants"):
        player.max_health -= player.pants.health_bonus
        player.stats["Health"] -= player.pants.health_bonus
        
        player.max_mana -= player.pants.mana_bonus
        player.stats["Mana"] -= player.pants.mana_bonus
        
        player.max_stamina -= player.pants.stamina_bonus
        player.stats["Stamina"] -= player.pants.stamina_bonus
        
        player.stats["Armor"] -= player.pants.armor_bonus
        player.stats["Speed"] -= player.pants.speed_bonus
        player.stats["Luck"] -= player.pants.luck_bonus
        player.stats["Regen"] -= player.pants.regen_bonus
        player.mana_regen -= player.pants.mana_regen_bonus
        player.stamina_regen -= player.pants.stamina_regen_bonus
    
    elif(item.piece == "boots"):
        player.max_health -= player.boots.health_bonus
        player.stats["Health"] -= player.boots.health_bonus
        
        player.max_mana -= player.boots.mana_bonus
        player.stats["Mana"] -= player.boots.mana_bonus
        
        player.max_stamina -= player.boots.stamina_bonus
        player.stats["Stamina"] -= player.boots.stamina_bonus
        
        player.stats["Armor"] -= player.boots.armor_bonus
        player.stats["Speed"] -= player.boots.speed_bonus
        player.stats["Luck"] -= player.boots.luck_bonus
        player.stats["Regen"] -= player.boots.regen_bonus
        player.mana_regen -= player.boots.mana_regen_bonus
        player.stamina_regen -= player.boots.stamina_regen_bonus
    #add new armor stats
    
def add_stats(player,item):
    player.max_health += item.health_bonus
    player.stats["Health"] += item.health_bonus
        
    player.max_mana += item.mana_bonus
    player.stats["Mana"] += item.mana_bonus
        
    player.max_stamina += item.stamina_bonus
    player.stats["Stamina"] += item.stamina_bonus
        
    player.stats["Armor"] += item.armor_bonus
    player.stats["Speed"] += item.speed_bonus
    player.stats["Luck"] += item.luck_bonus
    player.stats["Regen"] += item.regen_bonus
    
    player.mana_regen -= item.mana_regen_bonus
    player.stamina_regen -= item.stamina_regen_bonus
        
 
 
 