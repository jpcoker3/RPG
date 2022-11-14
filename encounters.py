import random
import weapons
import armors
import enemies
import combat
import player_info
items = ["weapon", "armor"]

def choose_rarity(player):
    rarity = random.randrange(player.stats["Luck"],100)
    if(rarity < 70):loot_rarity = "common"
    elif(rarity < 85): loot_rarity = "uncommon"
    elif(rarity < 95): loot_rarity = "rare"
    elif(rarity < 99): loot_rarity = "legendary"
    elif(rarity > 99): loot_rarity = "mythic" 
    
    return loot_rarity
    

#choose an encounter from list    
def choose_encounter(player, prev_encounter, game_round):
    options = ['Camp', 'Item', 'Enemy', 'Enemy', 'Enemy'] 
    
    if(game_round == 1):
        encounter = 'Item'
    else:
        encounter = random.choice(options)
        #make sure its not the same encounter every time
        while ((encounter == prev_encounter) and (prev_encounter != 'Enemy')):
            encounter = random.choice(options)
         
    if(encounter == 'Camp'):
        
        health_to_heal = round((player.max_health)/ 10)
        print("You found a camp! You decide take a moment to rest .... ")
        print("Gained " + str(health_to_heal) + " Health")
        player.stats["Health"] += health_to_heal #heal for 10%
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
        print("You opened a chest and found ....")
        
        ask_player_item(player, item)
        # give user a sec to take in info and continue
        input()

    elif (encounter == 'Enemy'):
        enemy_defeated = False
        print("Enemy Encounter")
        opponent = enemies.get_enemy(player)
        enemy_defeated = combat.battle(player, opponent)
        
        if(enemy_defeated == True):
            xp = random.randrange(player.stats["Level"]+5, 3*(player.stats["Level"]+5))
            xp += xp*player.stats["Luck"]
            
            gold = random.randrange(player.stats["Level"]+5, 5*(player.stats["Level"]+5))
            gold += gold * player.stats["Luck"]
            

            print("Enemy defeated! Obtained " + str(gold) + " gold and " + str(xp) + "xp!")
            player.gold_balance += gold
            player_info.recieve_xp(player, xp)
        input()
        
    else:
        print("Well something messed up")
        
    return encounter


def ask_player_item(player, item):
    print("Name: " + item.name)
    if(item.type == "armor"):
            print("{:<20}{:<10}".format("Level: ", item.level))
            print("{:<20}{:<10}".format("Rarity: ", item.rarity))
            if(item.health_bonus != 0): print("{:<20}{:<10}".format("Health Bonus: ", item.health_bonus))
            if(item.speed_bonus != 0): print("{:<20}{:<10}".format("Speed Bonus: ", item.speed_bonus))
            if(item.stamina_bonus != 0): print("{:<20}{:<10}".format("Stamina Bonus: ", item.stamina_bonus))
            if(item.armor_bonus != 0): print("{:<20}{:<10}".format("Armor Bonus: ", item.armor_bonus))
            if(item.mana_bonus != 0): print("{:<20}{:<10}".format("Mana Bonus: ", item.mana_bonus))
            if(item.regen_bonus != 0): print("{:<20}{:<10}".format("Regen Bonus: ", item.regen_bonus))
            
            if (item.piece == "helmet"):
                print("\nCurrently Equipped: " + player.helmet.name)
                print("{:<20}{:<10}".format("Level:", player.helmet.level))
                print("{:<20}{:<10}".format("Rarity: ", player.helmet.rarity))
                if(player.helmet.health_bonus != 0): print("{:<20}{:<10}".format("Health Bonus:", player.helmet.health_bonus))
                if(player.helmet.speed_bonus != 0): print("{:<20}{:<10}".format("Speed Bonus:", player.helmet.speed_bonus))
                if(player.helmet.stamina_bonus != 0): print("{:<20}{:<10}".format("Stamina Bonus:", player.helmet.stamina_bonus))
                if(player.helmet.armor_bonus != 0): print("{:<20}{:<10}".format("Armor Bonus:", player.helmet.armor_bonus))
                if(player.helmet.mana_bonus != 0): print("{:<20}{:<10}".format("Mana Bonus:", player.helmet.mana_bonus))
                if(player.helmet.regen_bonus != 0): print("{:<20}{:<10}".format("Regen Bonus: ", player.helmet.regen_bonus))
            elif (item.piece == "chest"):
                print("\nCurrently Equipped: " + player.chest.name)
                print("{:<20}{:<10}".format("Level:", player.chest.level))
                print("{:<20}{:<10}".format("Rarity: ", player.chest.rarity))
                if(player.chest.health_bonus != 0): print("{:<20}{:<10}".format("Health Bonus:", player.chest.health_bonus))
                if(player.chest.speed_bonus != 0): print("{:<20}{:<10}".format("Speed Bonus:", player.chest.speed_bonus))
                if(player.chest.stamina_bonus != 0): print("{:<20}{:<10}".format("Stamina Bonus:", player.chest.stamina_bonus))
                if(player.chest.armor_bonus != 0): print("{:<20}{:<10}".format("Armor Bonus:", player.chest.armor_bonus))
                if(player.chest.mana_bonus != 0): print("{:<20}{:<10}".format("Mana Bonus:", player.chest.mana_bonus))
                if(player.chest.regen_bonus != 0): print("{:<20}{:<10}".format("Regen Bonus: ", player.chest.regen_bonus))
            elif(item.piece == "legs"):
                print("\nCurrently Equipped: " + player.legs.name)
                print("{:<20}{:<10}".format("Level:", player.legs.level))
                print("{:<20}{:<10}".format("Rarity: ", player.legs.rarity))
                if(player.legs.health_bonus != 0): print("{:<20}{:<10}".format("Health Bonus:", player.legs.health_bonus))
                if(player.legs.speed_bonus != 0): print("{:<20}{:<10}".format("Speed Bonus:", player.legs.speed_bonus))
                if(player.legs.stamina_bonus != 0): print("{:<20}{:<10}".format("Stamina Bonus:", player.legs.stamina_bonus))
                if(player.legs.armor_bonus != 0): print("{:<20}{:<10}".format("Armor Bonus:", player.legs.armor_bonus))
                if(player.legs.mana_bonus != 0): print("{:<20}{:<10}".format("Mana Bonus:", player.legs.mana_bonus))
                if(player.legs.regen_bonus != 0): print("{:<20}{:<10}".format("Regen Bonus: ", player.legs.regen_bonus))
            elif( item.piece == "boots"):
                print("\nCurrently Equipped: " + player.boots.name)
                print("{:<20}{:<10}".format("Level:", player.boots.level))
                print("{:<20}{:<10}".format("Rarity: ", player.boots.rarity))
                if(player.boots.health_bonus != 0): print("{:<20}{:<10}".format("Health Bonus:", player.boots.health_bonus))
                if(player.boots.speed_bonus != 0): print("{:<20}{:<10}".format("Speed Bonus:", player.boots.speed_bonus))
                if(player.boots.stamina_bonus != 0): print("{:<20}{:<10}".format("Stamina Bonus:", player.boots.stamina_bonus))
                if(player.boots.armor_bonus != 0): print("{:<20}{:<10}".format("Armor Bonus:", player.boots.armor_bonus))
                if(player.boots.mana_bonus != 0): print("{:<20}{:<10}".format("Mana Bonus:", player.boots.mana_bonus))
                if(player.boots.regen_bonus != 0): print("{:<20}{:<10}".format("Regen Bonus: ", player.boots.regen_bonus))
           
            
            equip_item = input("Would you like to equip this item? y/n: ")
            if(equip_item == "y"):
                new_armor(player, item)
                
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
        print("{:<25}{:<10}".format("Level:", item.level))
        print("{:<25}{:<10}".format("Rarity:", item.rarity))
        if(item.damage != 0): print("{:<25}{:<10}".format("Damage:", item.damage))
        if(item.critical_chance != 0): print("{:<25}{:<10}".format("Critical Chance:", item.critical_chance))
        if(item.critical_damage != 0): print("{:<25}{:<10}".format("critical_damage:", item.critical_damage))
        if(item.armor_pen != 0): print("{:<25}{:<10}".format("Armor Penetration:", item.armor_pen))
        
            
            
        print("\n Currently equipped: " + player.weapon.name + ": ")
        print("{:<25}{:<10}".format("Level:", player.weapon.level))
        print("{:<25}{:<10}".format("Rarity:", player.weapon.rarity))
        if(player.weapon.damage != 0): print("{:<25}{:<10}".format("Damage:", player.weapon.damage))
        if(player.weapon.critical_chance != 0): print("{:<25}{:<10}".format("Critical Chance:", player.weapon.critical_chance))
        if(player.weapon.armor_pen != 0): print("{:<25}{:<10}".format("Armor Penetration:", player.weapon.armor_pen))
            
        equip_item = input("Would you like to equip this item? y/n: ")
        if(equip_item == 'y'):
            player.weapon = item
            print("You have equipped " + item.name)
        elif(equip_item == 'n'):
            print("The item was discarded")
            
        
def boss_encounter(player, game_round):
    boss = enemies.get_boss(game_round)
    
    combat.battle(player, boss)
    return

def shop_encounter(player, game_round):
    
    heal_cost = round(game_round + pow(player.stats["Level"], 2))
    item_cost = round(1.5* game_round + pow(player.stats["Level"],2) /2)
    
    print("You have encountered a Mysterious stranger selling goods and services for gold.\n")
    
    shop_item_rarity = choose_rarity(player)
    shopping = True
    #generate offers. 
    while(shopping):
        print("You have :" + str(player.gold_balance) + " Gold")
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
            else:
                print("You do not have enough money to do this.")   
        elif(choice == "2"):
            if(player.gold_balance >= item_cost):
                player.gold_balance -= item_cost
                item = armors.get_armor(player, shop_item_rarity)
                ask_player_item(player, item)
            else:
                print("You do not have enough money to do this.")
        elif(choice == "3"):
            if(player.gold_balance >= item_cost):
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
        
    elif(item.piece == "legs"):
        player.max_health -= player.legs.health_bonus
        player.stats["Health"] -= player.legs.health_bonus
        
        player.max_mana -= player.legs.mana_bonus
        player.stats["Mana"] -= player.legs.mana_bonus
        
        player.max_stamina -= player.legs.stamina_bonus
        player.stats["Stamina"] -= player.legs.stamina_bonus
        
        player.stats["Armor"] -= player.legs.armor_bonus
        player.stats["Speed"] -= player.legs.speed_bonus
        player.stats["Luck"] -= player.legs.luck_bonus
        player.stats["Regen"] -= player.legs.regen_bonus
    
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
        
 
 
 