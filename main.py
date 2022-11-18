import encounters
import player_info
from copy import copy

#GLOBAL VARS
world_name = 'Placeholder'
prev_encounter = ""

    
#main loop
def main():
    
    play_again = True
    while (play_again):
        prev_encounter = ""
        
        game_active = True
        #player
        character = player_info.char_info()
        
        player = copy(character)
        
        #get name of player
        player_info.char_create(player)
        player.name = f"{player.name} The {player.class_type}"
        print(f"Welcome to {world_name}, {player.name}!")
        next = input("Press the return key to continue to your first day!")
    
    
    # now we need to have the main game loop
        counter = 1
        while game_active:
            if(player.stats["Health"] <= 0): game_active = False  # haha you're dead
            else:
                print(f"\nRound {str(counter)}: ")
                if(counter % 250 == 0 ): 
                    print("You win!")
                    game_active = False
                    next = input("\nPress anything to exit game ") 
                elif(counter % 10 == 0):
                    encounters.boss_encounter(player, counter)
                elif(counter % 9 == 0):
                    encounters.shop_encounter(player, counter)
                else: prev_encounter = encounters.choose_encounter(player, prev_encounter, counter)
                
                counter += 1           
                
        go_again = input("\nWould you like to play again? y/n: ")
        if(go_again == "y"):
            play_again = True
            game_active = True
            
        else: 
            play_again = False
            print("You may now exit the game.")
main()