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
        player.stats["Health"] += round(player.stats["Health"] * (player.stats["Regen"] /100))
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
    opp_dmg -= round(opp_dmg * (1/100 * 1/3 * (player.stats["Armor"] - opponent.armor_pen))) 
                
    #set min damage to 1
    if(opp_dmg <= 0): opp_dmg = 1
    player.stats["Health"] -= opp_dmg
    
    if(opp_crit):
        print(opponent.name + " attacked with a critical hit for " + str(opp_dmg) + ". "+player.name+"'s health: " + str(player.stats["Health"]))
    else:
        print(opponent.name + " attacked for " + str(opp_dmg) + ". " + player.name + "'s health: " + str(player.stats["Health"]))
                
def player_attack(player, opponent):
    
    valid_attack_choice = False
    while(not valid_attack_choice):
        
        print("{:<3}{:<10}".format("#", "Skill"))
        for i in  range(len(player.skills)): #-1 for indexing
            print("{:<3}{:<10}".format(str(i+1), player.skills[i].name.capitalize()))
        
        valid_input = False
        while(not valid_input):
            attack_choice = input("What would you like to do?: ")
                
            if(attack_choice.isdigit()): 
                valid_input = True
            else: 
                valid_input = False 
                print("Please enter a number. \n")
                
        if((3 >= int(attack_choice)-1) >= 0 ):
            
            #get skill
            skill = player.skills[int(attack_choice)-1]
            
            if((player.stats["Mana"] > skill.mana_cost) and   # if you have enought resources
                (player.stats["Stamina"] > skill.stamina_cost) and  # and if not on cooldown
                (skill.cooldown_counter == 0 )):
        
                #get skill
                skill.cooldown_counter = skill.cooldown
                
                #physical damage calculations
                if(skill.type == "physical"):
            
                    player_dmg, player_crit, player_double_crit = player_damage(player, skill)
                                    # 1/100 to get a percentage, so attack is reduced by (armor - pen /4)%
                    player_dmg -= round(player_dmg * (1/100 * 1/3 * (opponent.armor - player.weapon.armor_pen)))
                    
                                
                    #set min damage to 1
                    if(player_dmg <= 0): player_dmg = 1
                    opponent.health -= player_dmg
                    
                    #doublecrit, crit, normal
                    if(player_double_crit):
                        print(player.name + " attacked with " + skill.name.capitalize() + " and DOUBLE critical hit for " + str(player_dmg) + ". " + opponent.name + "'s health: " + str(opponent.health))
                    elif(player_crit):
                        print(player.name + " attacked with " + skill.name.capitalize() + " and critical hit for " + str(player_dmg) + ". " + opponent.name + "'s health: " + str(opponent.health)) 
                    else:
                        print(player.name + " attacked with " + skill.name.capitalize() + " for " + str(player_dmg) + ". " + opponent.name + "'s health: " + str(opponent.health))    
                    
                #magical damage calculations 
                elif(skill.type == "magic"):
                    
                    #Haha magic is a joke
                    pass
                valid_attack_choice = True
            else:
                print("\nYou do not have enough resources for this ability.")
                print("You have: Stamina: " + str(player.skills["Stamina"]) + ". Mana: " + str(player.skills["Mana"]) + ". Cooldown: " + str(skill.cooldown_counter ))
                print("Need: Stamina: " + str(skill.stamina) + ". Mana: " + str(skill.mana) + ". Cooldown: 0\n")
                valid_attack_choice = False
        
        else:
            print("Please enter a valid option. ")
            valid_attack_choice = False
            
                
                
             
        
    for i in range(len(player.skills)):
        if( player.skills[i].cooldown_counter != 0):
            player.skills[i].cooldown_counter -= 1
    
def player_damage(player, skill):  
    damage = random.randrange(player.weapon.damage -2,  player.weapon.damage + 2)
    damage = round(damage * skill.damage_scaling)
    
    critical = False
    double_Crit = False
    if(random.randrange(0,100) <= player.critical_chance):
        damage = round( damage * player.critical_damage)
        critical = True
        
        if(random.randrange(0,100) <= (player.critical_chance - 100)):
            damage = round( damage * player.critical_damage)
            double_Crit = True
    
    
    
    return damage, critical, double_Crit

def opponent_damage(opponent):
    damage = random.randrange(opponent.damage -2 , opponent.damage + 2)
    critical = False
    if(random.randrange(0,100) <= opponent.critical_chance):
        damage = round( damage * opponent.critical_damage )  
        critical = True 
    
    return damage, critical

