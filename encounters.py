import random
import weapons
import armors
import enemies
import combat
import player_info
items = ["weapon", "armor"]

def choose_rarity(player):
    rarity = random.randrange(0,100) + player.stats["Luck"]
    if(rarity < 70):loot_rarity = "common"
    elif(rarity < 85): loot_rarity = "uncommon"
    elif(rarity < 95): loot_rarity = "rare"
    elif(rarity < 99): loot_rarity = "legendary"
    elif(rarity > 99): loot_rarity = "mythic" 
    
    return loot_rarity
    
    

#choose an encounter from list    
def choose_encounter(player, prev_encounter, round):
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

    #free item! congrats
    elif (encounter == 'Item'):
        print("Item Encounter")
        
        #choose item and rarity
        loot_rarity = choose_rarity(player)
        loot_type = random.choice(items)
        
        #if weapon, get weapon. if armor, get armor. pretty easy
        if(loot_type == "weapon"): item = weapons.get_weapon(player, loot_rarity)
        elif(loot_type == "armor"): item = armors.get_armor(player, loot_rarity)

        # output armor or weapon w stats and ask to equip or not
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
                elif (item.piece == "chest"):
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
            
        # give user a sec to take in info and continue
        input()

    elif (encounter == 'Enemy'):
        enemy_defeated = False
        print("Enemy Encounter")
        opponent = enemies.get_enemy(player)
        enemy_defeated = combat.battle(player, opponent)
        
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
        