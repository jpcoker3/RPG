from copy import copy
import random

class skill:
    def __init__(self, name:str,  summary:str, type:str,ad_scaling:int = 0, ap_scaling:int = 0, heal:int = 0, mana_cost:int = 0, stamina_cost:int = 0, cooldown:int = 0):
        self.name = name
        self.ad_scaling = ad_scaling
        self.ap_scaling = ap_scaling
        self.heal = heal
        self.mana_cost = mana_cost
        self.stamina_cost = stamina_cost
        self.cooldown = cooldown
        self.summary = summary
        self.type = type
    cooldown_counter = 0
         

#template = skill(name="", ad_scaling=0, ap_scaling=0, heal = 0, mana_cost=0, stamina_cost=0,cooldown=0, summary="", type="" )

#Types are: magic, physical, heal

#common
    #phys
lunge = skill("lunge",ad_scaling=1.2, stamina_cost=15, cooldown=3, summary="A short dash followed by a jab", type="physical") 

    #magic
sparks = skill(name="sparks", ap_scaling=1.3, mana_cost=15,cooldown=2, summary="a small burst of flames", type="magic")

    #heal
weak_heal = skill(name="Weak Heal",heal = 7, cooldown=0, summary="Heal for 7 percent max health", type="heal" )
warriors_heal = skill(name="Warriors Heal",heal = 12, stamina_cost=15, cooldown=3, summary="Heal for 12 percent max health", type="heal" )
mage_heal = skill(name="Mage's Heal", heal = 14, mana_cost=40,cooldown=2, summary="Heal for 14 percent max health, quick cooldown with high cost", type="heal" )



#uncommmon
    #phys
fireball = skill(name="fireball", ap_scaling=1.5, mana_cost=20,cooldown=3, summary="It's a fireball.", type="magic" )

    #magic


    #heal



#rare
    #phys

    #magic


    #heal


#legendary
    #phys

    #magic


    #heal


#mythic
    #phys

    #magic


    #heal



basic_attack = skill(name="Basic Attack", ad_scaling=1.0,  summary="Basic Attack", type="physical")

common_skills = [
    lunge,
    sparks,
    weak_heal
    
]

uncommon_skills = [
    fireball,
    warriors_heal,
    mage_heal
    
]

rare_skills = [
    
]

legendary_skills = [
    
]

mythic_skills = [
    
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
    print("\nYou have unlocked the ablility: " + skill.name.capitalize() )
    print("Summary: " + skill.summary)
    print("{:<15}{:<7}".format("Stat", "Value"))
    if(skill.ad_scaling != 0): print("{:<15}{:<7}".format("AD Scaling", skill.ad_scaling))
    if(skill.ap_scaling != 0): print("{:<15}{:<7}".format("AP Scaling", skill.ap_scaling))
    if(skill.heal != 0): print("{:<15}{:<7}".format("Heal %", skill.heal))
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
                choice_replace = input("You have the maximum amount of abilites. Would you like to replace one? (y/n): ")
                
                valid_replace = False
                while(not valid_replace):
                    if(choice_replace == "y"):
                        #output abilities, choose one to replace
                        print("\n")
                        
                        print("{:<8}{:<15}{:<20}".format("Choice","Name", "Summary" ))
                        print("{:<6}{:<15}{:<20}".format("1.",player.skills[0].name, player.skills[0].summary ))
                        print("{:<6}{:<15}{:<20}".format("2", player.skills[1].name, player.skills[1].summary ))
                        print("{:<6}{:<15}{:<20}".format("3.",player.skills[2].name, player.skills[2].summary ))
                        print("{:<6}{:<15}{:<20}".format("4.",player.skills[3].name, player.skills[3].summary ))
                        
                        temp = input("Which would you like to replace? (1-4): ")
                        skill_to_replace = int(temp)
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
    
