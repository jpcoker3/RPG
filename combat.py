import random

def battle(player, opponent):
   
    if(opponent.enemy_type == "enemy"):   print("Player Health: "+ str(player.stats["Health"]) + " Enemy Health: " + str(opponent.health) )
    else: print("Player Health: "+ str(player.stats["Health"]) + " Boss Health: " + str(opponent.health) )
    while((player.stats["Health"] > 0) and (opponent.health > 0)):
        not_dead = True
        player_speed = player.stats["Speed"]
        opponent_speed = opponent.speed
        #check speed, player may be able to attack twice or more before enemy attacks
        if(player_speed > opponent_speed):
            while(not_dead and (player_speed > opponent_speed)):
                player_attack(player, opponent)
                player_speed -= opponent_speed
                if(opponent.health < 0): not_dead = False
                #make sure opponent isnt dead yet
            if(opponent.health > 0):
                opponent_attack(player, opponent)
            else:
                not_dead = False
            next = input() 
        #and vice versa, opponent may be able to attack twice or more before player attacks
        elif(player_speed < opponent_speed):
            while (not_dead and (player_speed < opponent_speed)): 
                
                opponent_attack(player, opponent)
                opponent_speed -= player.stats["Speed"]
                
            #make sure opponent isnt dead yet
            if(player.stats["Health"] > 0):
                player_attack(player, opponent)
            else:
                not_dead = False
                
            next = input()   
            
            
    if((player.stats["Health"] > 0) and (opponent.health <= 0)):
        print("Congratulations " + player.name +"! You have defeated " + opponent.name + "!")

        #regenerate health
        player.stats["Health"] += player.stats["Regen"]
        if(player.stats["Health"] > player.max_health): 
            player.stats["Health"] = player.max_health
        #output regened health
        print("Regenerated " + str(player.stats["Regen"]) + ". Current Health: " + str(player.stats["Health"]))
        return True
    
    else:
        print("You have died by the hands of " + opponent.name + ". Thus ends the story of " + player.name)
        return False
    
def opponent_attack(player, opponent):
    opp_dmg , opp_crit= opponent_damage(opponent)
                # 1/100 to get like a percentage, so attack is reduced by (armor - pen /4)%
    opp_dmg -= round(opp_dmg * (1/100 * 1/4 * (player.stats["Armor"] - opponent.armor_pen))) 
                
    #set min damage to 1
    if(opp_dmg <= 0): opp_dmg = 1
    player.stats["Health"] -= opp_dmg
    
    if(opp_crit):
        print(opponent.name + " attacked with a critical hit for " + str(opp_dmg) + ". "+player.name+"'s health: " + str(player.stats["Health"]))
    else:
        print(opponent.name + " attacked for " + str(opp_dmg) + ". " + player.name + "'s health: " + str(player.stats["Health"]))
                
def player_attack(player, opponent):
    player_dmg, player_crit = player_damage(player)
                    # 1/100 to get like a percentage, so attack is reduced by (armor - pen /4)%
    player_dmg -= round(player_dmg * (1/100 * 1/4 * (opponent.armor - player.weapon.armor_pen)))
                
    #set min damage to 1
    if(player_dmg <= 0): player_dmg = 1
    opponent.health -= player_dmg
    if(player_crit):
        print(player.name + " attacked with a critical hit for " + str(player_dmg) + ". " + opponent.name + "'s health: " + str(opponent.health)) 
    else:
        print(player.name + " attacked for " + str(player_dmg) + ". " + opponent.name + "'s health: " + str(opponent.health)) 
    
def player_damage(player):  
    damage = random.randrange(player.weapon.damage -2,  player.weapon.damage + 2)
    critical = False
    if(random.randrange(0,100) <= player.critical_chance):
        damage = round( damage * player.critical_damage)
        critical = True
    
    return damage, critical

def opponent_damage(opponent):
    damage = random.randrange(opponent.damage -2 , opponent.damage + 2)
    critical = False
    if(random.randrange(0,100) <= opponent.critical_chance):
        damage = round( damage * opponent.critical_damage )  
        critical = True 
    
    return damage, critical


