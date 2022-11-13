import random
import player_info

def battle(player, opponent):
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
            input()
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
            input()   
    if((player.stats["Health"] > 0) and (opponent.health <= 0)):
        print("Congratulations " + player.name +"! You have defeated " + opponent.name + "!")
        return True
    else:
        print("You have died by the hands of " + opponent.name + ". Thus ends the story of " + player.name)
        return False
    
    
def player_damage(player):  
    damage = random.randrange(player.weapon.damage, player.weapon.damage * player.stats["Level"])
    
    if(random.randrange(0,100) <= player.weapon.critical_chance):
        damage = damage * player.weapon.critical_damage
    
    return damage 

def opponent_damage(opponent):
    damage = random.randrange(opponent.damage, opponent.damage * opponent.level)
    
    if(random.randrange(0,100) <= opponent.critical_chance):
        damage = damage * opponent.critical_damage    
    
    return damage