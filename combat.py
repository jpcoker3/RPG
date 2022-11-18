import random

def battle(player, opponent):
   
    if(opponent.enemy_type == "enemy"):   print("Player Health: "+ str(player.stats["Health"]) + " Enemy Health: " + str(opponent.health) )
    else:
        print("\n-----------BOSS FIGHT-----------\n")
        print(f"Player Health: {str(player.stats['Health'])}. {opponent.name} Health: {str(opponent.health)}" )
    while((player.stats["Health"] > 0) and (opponent.health > 0)):
        #print("\n") # spacing
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
        
            #Stamina Regen calculations. Only prints if amount regenerated > 0
        stam_regen_value =  player.stamina_regen
        
        stamina_total = stam_regen_value + player.stats["Stamina"]
        
        if(stamina_total > player.max_stamina):
            temp = stamina_total - player.max_stamina
            stam_regen_value -= temp
            if(stam_regen_value < 0): stam_regen_value = 0
            
        player.stats["Stamina"] += stam_regen_value

        #output regened health
        if(stam_regen_value > 0):
            print(f"Regenerated {str(stam_regen_value)} Stamina. Current Stamina: {str(player.stats['Stamina'])}")
        
        
        #Mana Regen calculations. Only prints if amount regenerated > 0
        mana_regen_value = player.mana_regen
        
        mana_total = mana_regen_value + player.stats["Mana"]
        if(mana_total > player.max_mana):
            temp = mana_total - player.max_mana
            mana_regen_value -= temp
            if(mana_regen_value < 0): mana_regen_value = 0
        player.stats["Stamina"] += mana_regen_value

        #output regened 
        if(mana_regen_value > 0):
            print(f"Regenerated {str(mana_regen_value)} Mana. Current Mana: {str(player.stats['Mana'])}")        
        
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
                
        
        
        #Stamina Regen calculations. Only prints if amount regenerated > 0
        stam_regen_value =  player.stamina_regen
        
        stamina_total = stam_regen_value + player.stats["Stamina"]
        
        if(stamina_total > player.max_stamina):
            temp = stamina_total - player.max_stamina
            stam_regen_value -= temp
            if(stam_regen_value < 0): stam_regen_value = 0
            
        player.stats["Stamina"] += stam_regen_value

        #output regened health
        if(stam_regen_value > 0):
            print(f"Regenerated {str(stam_regen_value)} Stamina. Current Stamina: {str(player.stats['Stamina'])}")
        
        
        #Mana Regen calculations. Only prints if amount regenerated > 0
        mana_regen_value = player.mana_regen
        
        mana_total = mana_regen_value + player.stats["Mana"]
        if(mana_total > player.max_mana):
            temp = mana_total - player.max_mana
            mana_regen_value -= temp
            if(mana_regen_value < 0): mana_regen_value = 0
        player.stats["Stamina"] += mana_regen_value

        #output regened 
        if(mana_regen_value > 0):
            print(f"Regenerated {str(mana_regen_value)} Mana. Current Mana: {str(player.stats['Mana'])}")

    
            
    if((player.stats["Health"] > 0) and (opponent.health <= 0)):
        print("Congratulations " + player.name +"! You have defeated " + opponent.name + "!")
        
        print("\n") # spacing
    
        #basically, calculate how much to heal ( if any)
        heal_value = player.stats["Regen"]
        
        heal_total = heal_value + player.stats["Health"]
        if(heal_total > player.max_health):
            temp = heal_total - player.max_health
            heal_value -= temp
            if(heal_value < 0): heal_value = 0
        player.stats["Health"] += heal_value

        #output regened health
        print("Regenerated " + str(heal_value) + ". Current Health: " + str(player.stats["Health"]))
        
        
        #need to reset skill cooldowns
        for i in range(len(player.skills)):
            player.skills[i].cooldown_counter = 0
        
        
        
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
        print(f"{opponent.name} attacked with a critical hit for {str(opp_dmg)}. {player.name}'s health: {str(player.stats['Health'])}")
    else:
        print(f"{opponent.name} attacked for {str(opp_dmg)}. {player.name}'s health: {str(player.stats['Health'])}")
                
def player_attack(player, opponent):
    
    valid_attack_choice = False
    while(not valid_attack_choice):
        print("\n") # spacing
        print("{:<3}{:<10}".format("#", "Skill"))
        for i in  range(len(player.skills)): #-1 for indexing
            print("{:<3}{:<10}".format(str(i+1), player.skills[i].name.capitalize()))
        print("\n")
        
        
        valid_input = False
        while(not valid_input):
            attack_choice = input("What would you like to do?: ")
                
            if(attack_choice.isdigit() and (int(attack_choice) < 5)): 
                valid_input = True
                
            else: 
                valid_input = False 
                print("Please enter a number. \n")
                
        if((int(attack_choice)-1) <= len(player.skills) ):
            
            
            #get skill
            skill = player.skills[int(attack_choice)-1]
            
            if((player.stats["Mana"] >= skill.mana_cost) and   # if you have enought resources
                (player.stats["Stamina"] >= skill.stamina_cost) and  # and if not on cooldown
                (skill.cooldown_counter == 0 )):

               
                #get skill
                skill.cooldown_counter = skill.cooldown
                player.stats["Mana"] -= skill.mana_cost
                player.stats["Stamina"] -= skill.stamina_cost
                
        
                
#DO STUFF DEPENDING ON TYPE OF SKILL
                #physical damage calculations
                if((skill.type == "melee") or (skill.type == "ranged")):
                    
                    player_dmg, player_crit, player_double_crit = player_damage(player, skill)
                                    # 1/100 to get a percentage, so attack is reduced by (armor - pen /4)%
                    player_dmg -= round(player_dmg * (1/100 * 1/3 * (opponent.armor - player.weapon.armor_pen)))
                    
                                
                    #set min damage to 1
                    if(player_dmg <= 0): player_dmg = 1
                    opponent.health -= player_dmg
                    
                    #doublecrit, crit, normal
                    if(player_double_crit):
                        print(f"{player.name} attacked with {skill.name.capitalize()} and DOUBLE critical hit for {str(player_dmg)}. {opponent.name}'s health: {str(opponent.health)}")
                    elif(player_crit):
                        print(f"{player.name} attacked with {skill.name.capitalize()} and critical hit for {str(player_dmg)}. {opponent.name}'s health: {str(opponent.health)}") 
                    else:
                        print(f"{player.name} attacked with {skill.name.capitalize()} for {str(player_dmg)}. {opponent.name}'s health: {str(opponent.health)}")    
                    
                    valid_attack_choice = True
                #magical damage calculations 
                elif(skill.type == "magic"):
                    player_dmg, player_crit, player_double_crit = player_damage(player, skill)
                                    # 1/100 to get a percentage, so attack is reduced by (armor - pen /4)%
                   # player_dmg -= round(player_dmg * (1/100 * 1/3 * (opponent.armor - player.weapon.armor_pen))) # no armor pen
                    
                                
                    #set min damage to 1
                    if(player_dmg <= 0): player_dmg = 1
                    opponent.health -= player_dmg
                    
                    #doublecrit, crit, normal
                    if(player_double_crit):
                        print(f"{player.name} attacked with {skill.name.capitalize()} and DOUBLE critical hit for {str(player_dmg)}. {opponent.name}'s health: {str(opponent.health)}")
                    elif(player_crit):
                        print(f"{player.name} attacked with {skill.name.capitalize()} and critical hit for {str(player_dmg)}. {opponent.name}'s health: {str(opponent.health)}") 
                    else:
                        print(f"{player.name} attacked with {skill.name.capitalize()} for {str(player_dmg)}. {opponent.name}'s health: {str(opponent.health)}")      
                    
                    valid_attack_choice = True
                
                
                #Heal Skills
                elif(skill.type == "heal"):                                          #heal percent
                    heal_value = round(player.max_health * (skill.heal / 100))
                    
                    
                    #basically, calculate how much to heal ( if any)
                    heal_total = heal_value + player.stats["Health"]
                    if(heal_total > player.max_health):
                        temp = heal_total - player.max_health
                        heal_value -= temp
                        if(heal_value < 0): heal_value = 0
                  

                    print(f"Used {skill.name} and healed for: {str(heal_value)}")
                        
                    player.stats["Health"] += heal_value
                    
                    valid_attack_choice = True
                    
                
            else:
                print("\nYou do not have enough resources for this ability.")
                
                if(player.stats["Mana"] < skill.mana_cost):
                    print(f"This skill requires {str(skill.mana_cost)} Mana. You have {str(player.stats['Mana'])} Mana. ")
            
                if(player.stats["Stamina"] < skill.stamina_cost):
                    print(f"This skill requires {str(skill.stamina_cost)} Stamina. You have {str(player.stats['Stamina'])} Stamina. ")
                if(skill.cooldown_counter != 0 ):
                    print(f"Skill on cooldown for {skill.cooldown_counter} turns.")
                    
                valid_attack_choice = False
        
        else:
            print("Please enter a valid option. ")
            valid_attack_choice = False
            
                
    #reduce cooldown
    for i in range(len(player.skills)):
        if( player.skills[i].cooldown_counter != 0):
            player.skills[i].cooldown_counter -= 1
            

    
def player_damage(player, skill):  
    
    #physical or magical
    if((skill.type == "melee") or (skill.type == "ranged")):
        damage = random.randrange(round(player.weapon.ad - player.weapon.ad/10),  round(player.weapon.ad + player.weapon.ad /10))
        damage = round(damage * skill.ad_scaling)
    elif(skill.type == "magic"):
        damage = random.randrange(round(player.weapon.ap - player.weapon.ap /10),  round(player.weapon.ap + player.weapon.ap/10) + 1)
        damage = round(damage * skill.ap_scaling)
    
        
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

