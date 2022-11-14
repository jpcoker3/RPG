import random

def battle(player, opponent):
    print("Player health: "+ str(player.stats["Health"]) + " Enemy health: " + str(opponent.health) )
    while((player.stats["Health"] > 0) and (opponent.health > 0)):
        player_speed = player.stats["Speed"]
        opponent_speed = opponent.speed
        #check speed, player may be able to attack twice or more before enemy attacks
        if(player_speed > opponent_speed):
            while (player_speed > opponent_speed): 
                
                player_dmg, player_crit = player_damage(player)
                                                # 1/100 to get like a percentage, so attack is reduced by (armor/4)%
                player_dmg -= round(player_dmg * (1/100 * 1/4 * (opponent.armor - player.weapon.armor_pen)))
                
                #set in damage to 1
                if(player_dmg <= 0): player_dmg = 1
                opponent.health -= player_dmg
                player_speed -= opponent_speed
                
                if(player_crit):
                    print(opponent.name + " was hit with a critical hit for " + str(player_dmg) + "! Enemy health == " + str(opponent.health)) 
                else:
                    print(opponent.name + " was hit for " + str(player_dmg) + ". Enemy health == " + str(opponent.health)) 
            #make sure opponent isnt dead yet
            if(opponent.health > 0):
                opp_dmg, opp_crit = opponent_damage(opponent)
                opp_dmg -= round(opp_dmg * (1/100 * 1/4 * (player.stats["Armor"]- opponent.armor_pen))) 
                
                #set in damage to 1
                if(opp_dmg <= 0): opp_dmg = 1
                player.stats["Health"] -= opp_dmg
                if(opp_crit):
                    print(player.name + " was hit with a critical hit for " + str(opp_dmg) + "! Player health == " + str(player.stats["Health"]))
                else:
                    print(player.name + " was hit for " + str(opp_dmg) + ". Player health == " + str(player.stats["Health"]))
            input()
        #and vice versa, opponent may be able to attack twice or more before player attacks
        elif(player_speed < opponent_speed):
            while (player_speed < opponent_speed): 
                
                opp_dmg , opp_crit= opponent_damage(opponent)
                opp_dmg -= round(opp_dmg * (1/100 * 1/4 * (player.stats["Armor"] - opponent.armor_pen))) 
                
                #set in damage to 1
                if(opp_dmg <= 0): opp_dmg = 1
                player.stats["Health"] -= opp_dmg
                
                opponent_speed -= player.stats["Speed"]
                if(opp_crit):
                    print(player.name + " was hit with a criticalhit for " + str(opp_dmg) + ". Player health == " + str(player.stats["Health"]))
                else:
                    print(player.name + " was hit for " + str(opp_dmg) + ". Player health == " + str(player.stats["Health"]))
            #make sure opponent isnt dead yet
            if(player.stats["Health"] > 0):
                player_dmg, player_crit = player_damage(player)
                player_dmg -= round(player_dmg * (1/100 * 1/4 * (opponent.armor - player.weapon.armor_pen)))
                
                #set min damage to 1
                if(player_dmg <= 0): player_dmg = 1
                opponent.health -= player_dmg
                if(player_crit):
                    print(opponent.name + " was hit with a critical hit for " + str(player_dmg) + "! Enemy health == " + str(opponent.health)) 
                else:
                    print(opponent.name + " was hit for " + str(player_dmg) + ". Enemy health == " + str(opponent.health)) 
            input()   
            
            
    if((player.stats["Health"] > 0) and (opponent.health <= 0)):
        print("Congratulations " + player.name +"! You have defeated " + opponent.name + "!")

        #regenerate health
        player.stats["Health"] += player.stats["Regen"]
        if(player.stats["Health"] > player.max_health): 
            player.stats["Health"] = player.max_health
        #output regened health
        print("Regenerated " + str(player.stats["Regen"]) + ".")
        return True
    
    else:
        print("You have died by the hands of " + opponent.name + ". Thus ends the story of " + player.name)
        return False
    
    
def player_damage(player):  
    damage = random.randrange(player.weapon.damage - 3,  1 +player.weapon.damage * (player.stats["Level"] + 1))
    critical = False
    if(random.randrange(0,100) <= player.weapon.critical_chance):
        damage = round( damage * player.weapon.critical_damage)
        critical = True
    
    return damage, critical

def opponent_damage(opponent):
    damage = random.randrange(opponent.damage -3 , 1 + opponent.damage * (opponent.level + 1))
    critical = False
    if(random.randrange(0,100) <= opponent.critical_chance):
        damage = round( damage * opponent.critical_damage )  
        critical = True 
    
    return damage, critical


