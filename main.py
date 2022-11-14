import weapons
from weapons import weapon 
import armors
from armors import armor
import encounters
import player_info

#GLOBAL VARS
world_name = 'Placeholder'
prev_encounter = ""

    
#main loop
def main():
    
    game_active = True
    prev_encounter = ""
    #player
    player = player_info.char_info()
    #get name of player
    player_info.char_create(player)
    player.name = player.name + " The " + player.class_type
    print('Welcome to ' + world_name + ', ' + player.name +'!')
    print("Press the return key to continue to your first day!")
    input()
    
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
                encounters.boss_encounter(player, counter)
                input()
            elif(counter % 9 == 0):
                encounters.shop_encounter(player, counter)
            else: prev_encounter = encounters.choose_encounter(player, prev_encounter, counter)
            
            counter += 1           

main()