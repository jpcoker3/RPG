from copy import copy
import random


class skill:
    def __init__(self, name:str,  summary:str, type:str, rarity:str,  ad_scaling:int = 0, ap_scaling:int = 0, heal:int = 0, mana_cost:int = 0, stamina_cost:int = 0, cooldown:int = 0):
        self.name = name
        self.ad_scaling = ad_scaling
        self.ap_scaling = ap_scaling
        self.heal = heal
        self.mana_cost = mana_cost
        self.stamina_cost = stamina_cost
        self.cooldown = cooldown
        self.summary = summary
        self.type = type#melee, ranged, magic, heal
        self.rarity = rarity #common, uncommon, rare, legendary, mythic

    cooldown_counter = 0
         

#template = skill(name="", rarity = "", ad_scaling=0, ap_scaling=0, heal = 0, mana_cost=0, stamina_cost=0,cooldown=0, summary="", type="" )

#Types are: magic, physical, heal


basic_attack = skill(name="Basic Attack", rarity = "common", ad_scaling=1.0, summary="Basic Melee Attack", type="melee")

#phys
#melee
lunge = skill(name= "Lunge", rarity = "common", ad_scaling=1.2, stamina_cost=15, cooldown=3, summary="A short dash followed by a thrust", type="melee") 
blunt_smash = skill(name="Blunt Smash", rarity = "common", ad_scaling=1.4 , stamina_cost=30, cooldown=5, summary="Smash the enemies face in with the blunt side of your weapon", type="melee" )
kick= skill(name="Kick", rarity = "common", ad_scaling=1.2, stamina_cost=15, cooldown=3, summary="Kick the enemy ... kinda obvious", type="melee" )

#ranged
focus_shot = skill(name="Focus Shot", rarity = "common", ad_scaling=1.4, stamina_cost=20 ,cooldown=3, summary="A focused shot towards enemy weak point", type="ranged" )
volley = skill(name="Volley", rarity = "uncommon", ad_scaling=1.6, stamina_cost=40 ,cooldown=5, summary="Shoot a volley of arrows towards the enemy", type="ranged" )

#magic
sparks = skill(name="Sparks", rarity = "common",  ap_scaling=1.3, mana_cost=15,cooldown=2, summary="a small burst of flames", type="magic")
fireball = skill(name="Fireball", rarity = "uncommon", ap_scaling=1.5, mana_cost=20,cooldown=3, summary="It's a fireball.", type="magic" )
ice_bolt = skill(name="Ice Bolt", rarity = "uncommon", ap_scaling=1.5, mana_cost= 40, cooldown=3, summary="Shoot out a bolt of Ice", type="magic" )


#heal
weak_heal = skill(name="Weak Heal", rarity = "common",heal = 10, cooldown=2, summary="Heal for 10 percent max health", type="heal" )
melee_heal = skill(name="Basic Heal", rarity = "uncommon",heal = 16, stamina_cost=15, cooldown=3, summary="Heal for 16 percent max health", type="heal" )
range_heal = skill(name="Basic Heal", rarity = "uncommon",heal = 16, stamina_cost=15, cooldown=3, summary="Heal for 16 percent max health", type="heal" )
magic_heal = skill(name="Basic Heal", rarity = "uncommon", heal = 16, mana_cost=25,cooldown=2, summary="Heal for 16 percent max health", type="heal" )








non_specific_skills = [
    
    weak_heal
    
]


melee_skills = [
    lunge,
    blunt_smash,
    kick,
    melee_heal
]

ranged_skills = [
    focus_shot,
    volley,
    range_heal
    
    
]

magic_skills = [
    fireball,
    magic_heal,
    sparks,
    ice_bolt
]



def get_skill(player):
   # player.class_dmg_type
    
    if(player.stats["Level"] <= 100):
        skill = choose_skill(player)
            
        ask_player_skill(player, skill)
    
    else:
        return

def choose_rarity(player):
    #level locked rarity
    if(player.stats["Level"] < 5):
        rarity = random.randrange(player.stats["Luck"],84)
    elif(player.stats["Level"] < 10):
        rarity = random.randrange(player.stats["Luck"],94)
    else:
        rarity = random.randrange(player.stats["Luck"],100)
        
    if(rarity <= 70):loot_rarity = "common"
    elif(rarity <= 85): loot_rarity = "uncommon"
    elif(rarity <= 95): loot_rarity = "rare"
    elif(rarity <= 99.5): loot_rarity = "legendary"
    elif(rarity > 99.5): loot_rarity = "mythic" 
    
    return loot_rarity
    
#prompt player to add skill
def ask_player_skill(player, skill):
    
    #output ability and stats
    print("\nYou have unlocked the ablility: " + skill.name )
    print("Summary: " + skill.summary)
    print("{:<15}{:<7}".format("Stat", "Value"))
    print("{:<15}{:<7}".format("Rarity", skill.rarity.capitalize()))
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
                        print("{:<8}{:<15}{:<20}".format("1.",player.skills[0].name, player.skills[0].summary ))
                        print("{:<8}{:<15}{:<20}".format("2", player.skills[1].name, player.skills[1].summary ))
                        print("{:<8}{:<15}{:<20}".format("3.",player.skills[2].name, player.skills[2].summary ))
                        print("{:<8}{:<15}{:<20}".format("4.",player.skills[3].name, player.skills[3].summary ))
                        
                        skill_to_replace = input("Which would you like to replace? (1-4): ")
                        
                        #easier to say its been replaced before actually replacing it
                        print(player.skills[int(skill_to_replace) -1].name + " was successfully replaced with " + skill.name) + ". "
                        player.skills.pop(skill_to_replace)
                        player.skills.append(copy(skill))
                        
                        
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
    
def choose_skill(player):
    
    found_correct_item = False
    
    while(not found_correct_item):
        
        rarity = choose_rarity(player)

       
        if((player.class_dmg_type == "melee")):
            skill = random.choice(non_specific_skills + melee_skills)
            if(
                (skill.rarity == rarity) and 
                ((skill.type == player.class_dmg_type) or 
                skill.type == "heal")):
                
                skill_return = copy(skill)
                found_correct_item = True
            else:
                found_correct_item = False
        elif((player.class_dmg_type == "ranged")):
            skill = random.choice(non_specific_skills + ranged_skills)
            if(
                (skill.rarity == rarity) and 
                ((skill.type == player.class_dmg_type) or 
                skill.type == "heal")):
                
                skill_return = copy(skill)
                found_correct_item = True
            else:
                found_correct_item = False
        elif((player.class_dmg_type == "maagic")):
            skill = random.choice(non_specific_skills + magic_skills)
            if(
                (skill.rarity == rarity) and 
                ((skill.type == player.class_dmg_type) or 
                skill.type == "heal")):
                
                skill_return = copy(skill)
                found_correct_item = True
            else:
                found_correct_item = False
                
        
            
            
    return skill_return