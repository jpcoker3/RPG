from copy import copy
import random

class skill:
    def __init__(self, name:str, damage_scaling:int, ap_scaling:int,mana_cost:int, stamina_cost:int, cooldown:int, summary:str, type:str):
        self.name = name
        self.damage_scaling = damage_scaling
        self.ap_scaling = ap_scaling
        self.mana_cost = mana_cost
        self.stamina_cost = stamina_cost
        self.cooldown = cooldown
        self.summary = summary
        self.type = type
    cooldown_counter = 0
         

#template = skill(name="", damage_scaling=0, ap_scaling=0, mana_cost=0, stamina_cost=0,cooldown=0, summary="", type="" )
lunge = skill("lunge",damage_scaling=1.2, ap_scaling=0, mana_cost=0,stamina_cost=15, cooldown=3, type="physical", summary="A short dash followed by a jab") 
basic_attack = skill(name="Basic Attack", damage_scaling=1.0, ap_scaling= 0, mana_cost=0, stamina_cost=0, cooldown=0, summary="Basic Attack", type="physical")

common_skills = [
    lunge  
]

uncommon_skills = [
    
]

def get_skill(player):
    if(player.stats["Level"] <= 7):
        skill = random.choice(common_skills)
        ask_player_skill(player, skill)
    elif(player.stats["Level"] <= 13):
        skill = random.choice(uncommon_skills)
        ask_player_skill(player, skill)
    else:
        pass

    
    
#prompt player to add skill
def ask_player_skill(player, skill):
    
    #output ability and stats
    print("You have unlocked the ablility: " + skill.name.capitalize() )
    print("Summary: " + skill.summary)
    print("{:<15}{:<7}".format("Stat", "Value"))
    if(skill.damage_scaling != 0): print("{:<15}{:<7}".format("Damage Scaling", skill.damage_scaling))
    if(skill.ap_scaling != 0): print("{:<15}{:<7}".format("Ability Power Scaling", skill.ap_scaling))
    if(skill.mana_cost != 0): print("{:<15}{:<7}".format("Mana Cost", skill.mana_cost))
    if(skill.stamina_cost != 0): print("{:<15}{:<7}".format("Stamina Cost", skill.stamina_cost))
    if(skill.cooldown != 0): print("{:<15}{:<7}".format("Cooldown", skill.cooldown))
    
    
    
    choice = input("\nWould you like to equip this abiliity? y/n: ")
    valid = False
    while(not valid):
        if(choice == "y"):
            valid = True
            #if you have 4 skills already
            if(len(player.skills) == 4):
                choice_replace = input("You have the maximum amount of abilites. Would you like to replace one?: ")
                
                valid_replace = False
                while(not valid_replace):
                    if(choice_replace == "y"):
                        #output abilities, choose one to replace
                        
                        print("{:<6}{:<8}{:<20}".format("Choice","Name", "Summary" ))
                        print("{:<6}{:<8}{:<20}".format("1.",player.skills[0].name, player.skills[0].summary ))
                        print("{:<6}{:<8}{:<20}".format("2", player.skills[1].name, player.skills[1].summary ))
                        print("{:<6}{:<8}{:<20}".format("3.",player.skills[2].name, player.skills[2].summary ))
                        print("{:<6}{:<8}{:<20}".format("4.",player.skills[3].name, player.skills[3].summary ))
                        
                        skill_to_replace = input("Which would you like to replace? (1-4): ")
                        skill_to_replace -= 1  # index starts at 0. 
                        
                        #easier to say its been replaced before actually replacing it
                        print(player.skills[skill_to_replace].name + " was successfully replaced with " + skill.name) + ". "
                        player.skills.pop(skill_to_replace)
                        player.skills.append(skill)
                        
                        
                        valid = True
                    elif(choice_replace == "n"):
                        print("Skill was discarded")
                        valid = True
                        return 
            else:
                
                #just add the ability
                player.skills.append(copy(skill))
                print(skill.name.capitalize() + " was successfully added.")
                return
            
         #player doesnt want the skill   
        elif(choice == "n"):
            valid = True
            print("Skill was discaded")
            return
    
