import encounters
import player_info
from copy import copy
from colors import *
import pygame, sys
from button import Button
import random



#GLOBAL VARS
world_name = 'Placeholder'
final_boss = "FINAL_BOSS_NAME"
prev_encounter = ""
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
run = True
FPS = 60





clock = pygame.time.Clock()


pygame.init()

SURFACE = pygame.HWSURFACE|pygame.DOUBLEBUF#|pygame.RESIZABLE
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), SURFACE)    #|pygame.RESIZABLE)   #set resolution to be displayed
pygame.display.set_caption(world_name)

MAIN_MENU_BACKGROUND = pygame.image.load("assets/main_menu_background.png")
MAIN_MENU_BACKGROUND = pygame.transform.smoothscale(MAIN_MENU_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.flip()



#game backgrounds
GAME_BG1 = pygame.image.load("assets/battle_backgrounds/battleback1.png")
GAME_BG2 = pygame.image.load("assets/battle_backgrounds/battleback2.png")
GAME_BG3 = pygame.image.load("assets/battle_backgrounds/battleback3.png")
GAME_BG4 = pygame.image.load("assets/battle_backgrounds/battleback4.png")
GAME_BG5 = pygame.image.load("assets/battle_backgrounds/battleback5.png")
GAME_BG6 = pygame.image.load("assets/battle_backgrounds/battleback6.png")
GAME_BG7 = pygame.image.load("assets/battle_backgrounds/battleback7.png")
GAME_BG8 = pygame.image.load("assets/battle_backgrounds/battleback8.png")
GAME_BG9 = pygame.image.load("assets/battle_backgrounds/battleback9.png")
GAME_BG10 = pygame.image.load("assets/battle_backgrounds/battleback10.png")

BATTLE_BGS = [
    GAME_BG1,
    GAME_BG2,
    GAME_BG3,
    GAME_BG4,
    GAME_BG5,
    GAME_BG6,
    GAME_BG7,
    GAME_BG8,
    GAME_BG9,
    GAME_BG10
]
GAME_BACKGROUND = GAME_BG1

ENEMY_1 = pygame.image.load("assets/enemies/enemy_1.png")
ENEMY_2 = pygame.image.load("assets/enemies/enemy_2.png")
ENEMY_3 = pygame.image.load("assets/enemies/enemy_3.png")
ENEMY_4 = pygame.image.load("assets/enemies/enemy_4.png")
ENEMY_5 = pygame.image.load("assets/enemies/enemy_5.png")
ENEMY_6 = pygame.image.load("assets/enemies/enemy_6.png")
ENEMY_7 = pygame.image.load("assets/enemies/enemy_7.png")

ENEMY_IMG = [
    ENEMY_1,
    ENEMY_2,
    ENEMY_3,
    ENEMY_4,
    ENEMY_5,
    ENEMY_6,
    ENEMY_7
]


BOSS_1 = pygame.image.load("assets/bosses/boss_1.png")
BOSS_2 = pygame.image.load("assets/bosses/boss_2.png")

BOSS_IMG = [
    BOSS_1,
    BOSS_2
]

def get_font(size): #return font size
    return pygame.font.SysFont('Calibri', size)

def fade_out():#TEXT, RECT,start_width ,start_height ):
    global SCREEN, SCREEN_HEIGHT,SCREEN_WIDTH
    
    fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fade.fill(BLACK) #fade to black
    for alpha in range (0, 255,1): #from transparent to opaque
        fade.set_alpha(alpha)
        SCREEN.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)
    pygame.time.delay(1000)
        
def fade_in_txt(TEXT, RECT,start_width ,start_height ):
    global SCREEN, SCREEN_HEIGHT,SCREEN_WIDTH
    
    fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fade.fill(BLACK) #fade to black
    for alpha in range (255, 0,-1): #from transparent to opaque
        fade.set_alpha(alpha)
        
        SCREEN.blit(TEXT, RECT)
        SCREEN.blit(fade, (start_width,start_height))
        pygame.display.update()
        pygame.time.delay(4)
    pygame.time.delay(1000)
        
def fade_in_img(image):
    global SCREEN, SCREEN_HEIGHT,SCREEN_WIDTH
    
    fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fade.fill(BLACK) #fade to black
    for alpha in range (255, 0,-1): #from transparent to opaque
        fade.set_alpha(alpha)
        img = pygame.transform.smoothscale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        SCREEN.blit(img, (0,0))
        SCREEN.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(1)

def main_menu():
    pygame.display.set_caption("Menu")
    global SCREEN_WIDTH, SCREEN_HEIGHT, FPS
    
    
    while True:
        
        
        SCREEN.fill(BLACK)
        SCREEN.blit(MAIN_MENU_BACKGROUND, (0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
       

        MENU_TEXT = get_font(100).render("MAIN MENU", True,WHITE)
        MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/7))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/2, 2*SCREEN_HEIGHT/5), 
                            text_input="PLAY", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/2, 3*SCREEN_HEIGHT/5),
                            text_input="OPTIONS", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/2, 4*SCREEN_HEIGHT/5),
                            text_input="QUIT", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")

        SCREEN.blit(MENU_TEXT, MENU_RECT)
    

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick_busy_loop( FPS )
        
def pause_menu():
    global SCREEN, SCREEN_HEIGHT,SCREEN_WIDTH, FPS, MAIN_MENU_BACKGROUND
    
    while True:
        PAUSE_MOUSE_POS = pygame.mouse.get_pos() # mouse posn
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill(BLACK)
        overlay.set_alpha(100)
        
        INVENTORY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(overlay, (0,0))
        
        
        PAUSE_TEXT = get_font(100).render("GAME PAUSED", True,WHITE)
        PAUSE_RECT = PAUSE_TEXT.get_rect(center=(SCREEN_WIDTH/2, 2*SCREEN_HEIGHT/10))
        SCREEN.blit(PAUSE_TEXT, PAUSE_RECT)
        
        
        PAUSE_RESUME = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/2,   4*SCREEN_HEIGHT/10), # bottom right 10th of the screen
                            text_input="Resume", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        
        PAUSE_OPTIONS = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/2,  5* SCREEN_HEIGHT/10), 
                            text_input="Options", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        
        MAIN_MENU_OPTIONS = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/2,  6* SCREEN_HEIGHT/10), 
                            text_input="Main Menu", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        
        EXIT_GAME_OPTIONS = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/2,  7* SCREEN_HEIGHT/10), 
                            text_input="Exit Game", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        
        
        
        
        for button in [PAUSE_OPTIONS, PAUSE_RESUME, MAIN_MENU_OPTIONS,EXIT_GAME_OPTIONS]:
                button.changeColor(PAUSE_MOUSE_POS)
                button.update(SCREEN)
                
                
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE_RESUME.checkForInput(PAUSE_MOUSE_POS):
                    return
                
                if PAUSE_OPTIONS.checkForInput(PAUSE_MOUSE_POS):
                    options()
                    
                
                if MAIN_MENU_OPTIONS.checkForInput(PAUSE_MOUSE_POS):
                    main_menu()
                if EXIT_GAME_OPTIONS.checkForInput(PAUSE_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  
                    
                    
        pygame.display.update()
        clock.tick_busy_loop( FPS ) # set to 60 fps  

def intro():
    global SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN, FPS
    SCREEN.fill(BLACK)
    still_in_intro = True   # make True, True for real run
    i=0
    
    while(True):
        INTRO_MOUSE_POS = pygame.mouse.get_pos() # mouse posn
 
        while still_in_intro:
            INTRO_TEXT = get_font(110).render(f"WAKE UP", True, WHITE)
            INTRO_TEXT_RECT = INTRO_TEXT.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/7))
            SCREEN.blit(INTRO_TEXT, INTRO_TEXT_RECT)
            
            INTRO_TEXT2 = get_font(60).render(f"You must defeat {final_boss} in order to free the world", True, WHITE)
            INTRO_TEXT_RECT2 = INTRO_TEXT2.get_rect(center=(SCREEN_WIDTH/2, 2*SCREEN_HEIGHT/7))
            
            INTRO_TEXT3 = get_font(60).render(f"You cannot fail. You are the Chosen One.", True, WHITE)
            INTRO_TEXT_RECT3 = INTRO_TEXT3.get_rect(center=(SCREEN_WIDTH/2, 3*SCREEN_HEIGHT/7))
            
            INTRO_TEXT4 = get_font(60).render(f"... And the last line of defense", True, WHITE)
            INTRO_TEXT_RECT4 = INTRO_TEXT4.get_rect(center=(SCREEN_WIDTH/2, 4*SCREEN_HEIGHT/7))
            
            INTRO_TEXT5 = get_font(60).render(f"Anyway, Good Luck. You'll need it. ", True, WHITE)
            INTRO_TEXT_RECT5 = INTRO_TEXT5.get_rect(center=(SCREEN_WIDTH/2, 5*SCREEN_HEIGHT/7))
            
            INTRO_TEXT6 = get_font(40).render("The voices fades", True, WHITE)
            INTRO_TEXT_RECT6 = INTRO_TEXT6.get_rect(center=(round(SCREEN_WIDTH/2), 6*SCREEN_HEIGHT/7))
            
            text_list=[INTRO_TEXT,INTRO_TEXT2,INTRO_TEXT3, INTRO_TEXT4,INTRO_TEXT5, INTRO_TEXT6]
            rect_list=[INTRO_TEXT_RECT,INTRO_TEXT_RECT2,INTRO_TEXT_RECT3, INTRO_TEXT_RECT4,INTRO_TEXT_RECT5,INTRO_TEXT_RECT6]
        
            
            
            if (i != len(text_list)):  # if all of the intro has been played
                height = rect_list[i].top
                fade_in_txt(text_list[i], rect_list[i],start_height=height, start_width=0) #show
                #fade_out(text_list[i], rect_list[i], start_height=height, start_width=0) #fade 
                
                i+=1 #increment
            else:
                
                still_in_intro = False

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return  
                
        NEXT_BUTTON = Button(image=pygame.image.load("assets/button.png"), pos=(9*SCREEN_WIDTH/10, 9*SCREEN_HEIGHT/10), 
                            text_input="NEXT", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        
        for button in [NEXT_BUTTON]:  # update button color based on where mouse is
            button.changeColor(INTRO_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEXT_BUTTON.checkForInput(INTRO_MOUSE_POS): 
                    fade_out()
                    return
                
            
                                     
                
                
        pygame.display.update()
        clock.tick_busy_loop( FPS )

def inventory():
    global SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN, GAME_BACKGROUND
    
    while True:
        SCREEN.fill(BLACK)
        GAME_BACKGROUND = pygame.transform.smoothscale(GAME_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT)) # scale to screen
        GAME_BACKGROUND.set_alpha(100)
        INVENTORY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(GAME_BACKGROUND, (0,0))
    
    
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        pygame.display.update()
        clock.tick_busy_loop( FPS )

def boss_encounter(player, counter):
    global SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN, GAME_BACKGROUND
    BOSS_ICON = random.choice(BOSS_IMG)
    while True:
        GAME_BACKGROUND = pygame.transform.smoothscale(GAME_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT)) # scale to screen
        SCREEN.blit(GAME_BACKGROUND, (0,0))
        
       
        SCREEN.blit(BOSS_ICON, (SCREEN_WIDTH/2, SCREEN_HEIGHT))
        
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause_menu() 
                        
        pygame.display.update()
        clock.tick_busy_loop( FPS )
    
def main_game_loop(player):
    global SCREEN_WIDTH, SCREEN_HEIGHT, FPS, SCREEN, GAME_BACKGROUND, prev_encounter
    counter = 1
    
    while True:
        
        GAME_BACKGROUND = random.choice(BATTLE_BGS)
        SCREEN.fill(BLACK)
        fade_in_img(GAME_BACKGROUND)
        
        while True:
            INV_ICON = pygame.image.load("assets/inventory_icon.png")
            INV_ICON = pygame.transform.smoothscale(INV_ICON, (SCREEN_WIDTH/16, SCREEN_HEIGHT/9))
            GAME_BACKGROUND = pygame.transform.smoothscale(GAME_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT)) # scale to screen
            MAIN_LOOP_MOUSE_POS = pygame.mouse.get_pos()
            SCREEN.blit(GAME_BACKGROUND, (0,0))
            
            COUNTER_TXT = get_font(100).render(f"Round: {str(counter)}", True,WHITE)  #display counter
            COUNTER_RECT = COUNTER_TXT.get_rect(center=(SCREEN_WIDTH/2, 1*SCREEN_HEIGHT/10))
            SCREEN.blit(COUNTER_TXT, COUNTER_RECT)
            
            if(counter % 250 == 0 ):  #You Win
                return
            elif(counter % 1 == 0):  #Boss encounter
                boss_encounter(player, counter)
                #encounters.boss_encounter(player, counter)
            elif(counter % 9 == 0): #Shop Encounter
                encounters.shop_encounter(player, counter)
            else: prev_encounter = encounters.choose_encounter(player, prev_encounter, counter) #random encounter
                    
            counter += 1           
            
            
            
            INVENTORY_BUTTON = Button(image=INV_ICON, pos=(round(SCREEN_WIDTH/12), round(SCREEN_HEIGHT/12)), 
                            text_input=" ", font=get_font(30), base_color="Black", hovering_color="Dark Blue")
            
            
            for button in [INVENTORY_BUTTON]:  # update button color based on where mouse is
                button.changeColor(MAIN_LOOP_MOUSE_POS)
                button.update(SCREEN)
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause_menu() 
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if INVENTORY_BUTTON.checkForInput(MAIN_LOOP_MOUSE_POS):
                        inventory()
                

            pygame.display.update()
            clock.tick_busy_loop( FPS )
            
def char_create_ui():
    global SCREEN_HEIGHT, SCREEN, SCREEN_WIDTH,MAIN_MENU_BACKGROUND
    CLASS_SELECT = "peasant"
    
    while True:
        SCREEN.fill(BLACK)
        MAIN_MENU_BACKGROUND = pygame.transform.smoothscale(MAIN_MENU_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
        SCREEN.blit(MAIN_MENU_BACKGROUND, (0,0))
        CHAR_CREATE_MOUSE_POS = pygame.mouse.get_pos()
        
        CHAR_CREATE_TEXT = get_font(100).render("Character Creation", True, WHITE)
        CHAR_CREATE_TEXT_RECT = CHAR_CREATE_TEXT.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/10))
        SCREEN.blit(CHAR_CREATE_TEXT, CHAR_CREATE_TEXT_RECT)
        
        DEFAULT_BUTTON_IMAGE = pygame.image.load("assets/button.png")
        CHAR_SELECT_BUTTON_IMAGE = pygame.transform.scale(DEFAULT_BUTTON_IMAGE, (1.5*DEFAULT_BUTTON_IMAGE.get_width(), .8*DEFAULT_BUTTON_IMAGE.get_height()) )
        
        SUMMARY_COLOR = WHITE  #for quick editing later
        
        

        #PEASANT
        if(CLASS_SELECT == "peasant"):
            PEASANT_BUTTON = Button(CHAR_SELECT_BUTTON_IMAGE, pos=(SCREEN_WIDTH/5, 2*SCREEN_HEIGHT/10), 
                                text_input="Peasant", font=get_font(40), base_color="Dark Blue", hovering_color="Dark Blue")
        else:
            PEASANT_BUTTON = Button(CHAR_SELECT_BUTTON_IMAGE, pos=(SCREEN_WIDTH/5, 2*SCREEN_HEIGHT/10), 
                                text_input="Peasant", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        PEASANT_SUMMARY = get_font(40).render(player_info.peasant.summary, True, SUMMARY_COLOR)
        PEASANT_TEXT_RECT = PEASANT_SUMMARY.get_rect(midleft=(SCREEN_WIDTH/3, 2*SCREEN_HEIGHT/10))
        SCREEN.blit(PEASANT_SUMMARY, PEASANT_TEXT_RECT)
        
        #IDIOT
        if(CLASS_SELECT == "idiot"):
            IDIOT_BUTTON = Button(CHAR_SELECT_BUTTON_IMAGE, pos=(SCREEN_WIDTH/5, 3*SCREEN_HEIGHT/10),
                                text_input="Idiot", font=get_font(40), base_color="Dark Blue", hovering_color="Dark Blue")
        else:
            IDIOT_BUTTON = Button(CHAR_SELECT_BUTTON_IMAGE, pos=(SCREEN_WIDTH/5, 3*SCREEN_HEIGHT/10),
                                text_input="Idiot", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        IDIOT_SUMMARY = get_font(40).render(player_info.idiot.summary, True, SUMMARY_COLOR)
        IDIOT_TEXT_RECT = IDIOT_SUMMARY.get_rect(midleft=(SCREEN_WIDTH/3, 3*SCREEN_HEIGHT/10))
        SCREEN.blit(IDIOT_SUMMARY, IDIOT_TEXT_RECT)
        
        #WARRIOR
        if(CLASS_SELECT == "warrior"):
            WARRIOR_BUTTON = Button(CHAR_SELECT_BUTTON_IMAGE, pos=(SCREEN_WIDTH/5, 4*SCREEN_HEIGHT/10),
                                text_input="Warrior", font=get_font(40), base_color="Dark Blue", hovering_color="Dark Blue")
        else:
            WARRIOR_BUTTON = Button(CHAR_SELECT_BUTTON_IMAGE, pos=(SCREEN_WIDTH/5, 4*SCREEN_HEIGHT/10),
                                text_input="Warrior", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        WARRIOR_SUMMARY = get_font(40).render(player_info.warrior.summary, True, SUMMARY_COLOR)
        WARRIOR_TEXT_RECT = WARRIOR_SUMMARY.get_rect(midleft=(SCREEN_WIDTH/3, 4*SCREEN_HEIGHT/10))
        SCREEN.blit(WARRIOR_SUMMARY, WARRIOR_TEXT_RECT)
        
        #GAMBLER
        if(CLASS_SELECT == "gambler"):
            GAMBLER_BUTTON = Button(CHAR_SELECT_BUTTON_IMAGE, pos=(SCREEN_WIDTH/5, 5*SCREEN_HEIGHT/10),
                                text_input="Gambler", font=get_font(40), base_color="Dark Blue", hovering_color="Dark Blue")
        else:
            GAMBLER_BUTTON = Button(CHAR_SELECT_BUTTON_IMAGE, pos=(SCREEN_WIDTH/5, 5*SCREEN_HEIGHT/10),
                            text_input="Gambler", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        GAMBLER_SUMMARY = get_font(40).render(player_info.gambler.summary, True, SUMMARY_COLOR)
        GAMBLER_TEXT_RECT = GAMBLER_SUMMARY.get_rect(midleft=(SCREEN_WIDTH/3, 5*SCREEN_HEIGHT/10))
        SCREEN.blit(GAMBLER_SUMMARY, GAMBLER_TEXT_RECT)
        
        #RANGER
        if(CLASS_SELECT == "ranger"):
            RANGER_BUTTON = Button(CHAR_SELECT_BUTTON_IMAGE, pos=(SCREEN_WIDTH/5, 6*SCREEN_HEIGHT/10),
                                text_input="Ranger", font=get_font(40), base_color="Dark Blue", hovering_color="Dark Blue")
        else:
            RANGER_BUTTON = Button(CHAR_SELECT_BUTTON_IMAGE, pos=(SCREEN_WIDTH/5, 6*SCREEN_HEIGHT/10),
                                text_input="Ranger", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
            
        RANGER_SUMMARY = get_font(40).render(player_info.ranger.summary, True, SUMMARY_COLOR)
        RANGER_TEXT_RECT = RANGER_SUMMARY.get_rect(midleft=(SCREEN_WIDTH/3, 6*SCREEN_HEIGHT/10))
        SCREEN.blit(RANGER_SUMMARY, RANGER_TEXT_RECT)
        
        #DEFENDER
        if(CLASS_SELECT == "defender"):
            DEFENDER_BUTTON = Button(CHAR_SELECT_BUTTON_IMAGE, pos=(SCREEN_WIDTH/5, 7*SCREEN_HEIGHT/10),
                              text_input="Defender", font=get_font(40), base_color="Dark Blue", hovering_color="Dark Blue")
        else:
            DEFENDER_BUTTON = Button(CHAR_SELECT_BUTTON_IMAGE, pos=(SCREEN_WIDTH/5, 7*SCREEN_HEIGHT/10),
                                text_input="Defender", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        DEFENDER_SUMMARY = get_font(40).render(player_info.defender.summary, True, SUMMARY_COLOR)
        DEFENDER_TEXT_RECT = DEFENDER_SUMMARY.get_rect(midleft=(SCREEN_WIDTH/3, 7*SCREEN_HEIGHT/10))
        SCREEN.blit(DEFENDER_SUMMARY, DEFENDER_TEXT_RECT)
        
        #WIZZARD
        if(CLASS_SELECT == "wizzard"):
            WIZZARD_BUTTON = Button(CHAR_SELECT_BUTTON_IMAGE, pos=(SCREEN_WIDTH/5, 8*SCREEN_HEIGHT/10),
                            text_input="Wizzard", font=get_font(40), base_color="Dark Blue", hovering_color="Dark Blue")
        else:
            WIZZARD_BUTTON = Button(CHAR_SELECT_BUTTON_IMAGE, pos=(SCREEN_WIDTH/5, 8*SCREEN_HEIGHT/10),
                            text_input="Wizzard", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        WIZZARD_SUMMARY = get_font(40).render(player_info.wizzard.summary, True, SUMMARY_COLOR)
        WIZZARD_TEXT_RECT = WIZZARD_SUMMARY.get_rect(midleft=(SCREEN_WIDTH/3, 8*SCREEN_HEIGHT/10))
        SCREEN.blit(WIZZARD_SUMMARY, WIZZARD_TEXT_RECT)
        
        #confirm button
        CONFIRM_BUTTON = Button(DEFAULT_BUTTON_IMAGE, pos=(9*SCREEN_WIDTH/10, 9*SCREEN_HEIGHT/10),
                            text_input="Confirm", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        
        #selection text
        CLASS_SELECT_TEXT = get_font(40).render("Selected: " + CLASS_SELECT.capitalize(), True, SUMMARY_COLOR)
        CLASS_SELECT_TEXT_RECT = CLASS_SELECT_TEXT.get_rect(center=(9*SCREEN_WIDTH/10, 8*SCREEN_HEIGHT/10))
        SCREEN.blit(CLASS_SELECT_TEXT, CLASS_SELECT_TEXT_RECT)
        
        for button in [PEASANT_BUTTON, IDIOT_BUTTON, WARRIOR_BUTTON,GAMBLER_BUTTON,RANGER_BUTTON,DEFENDER_BUTTON, WIZZARD_BUTTON,CONFIRM_BUTTON ]: # add all the buttons to the screen
            button.changeColor(CHAR_CREATE_MOUSE_POS)
            button.update(SCREEN)    
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PEASANT_BUTTON.checkForInput(CHAR_CREATE_MOUSE_POS):
                    CLASS_SELECT = "peasant"
                if IDIOT_BUTTON.checkForInput(CHAR_CREATE_MOUSE_POS):
                    CLASS_SELECT = "idiot"
                if WARRIOR_BUTTON.checkForInput(CHAR_CREATE_MOUSE_POS):
                    CLASS_SELECT = "warrior"
                if GAMBLER_BUTTON.checkForInput(CHAR_CREATE_MOUSE_POS):
                    CLASS_SELECT = "gambler"
                if RANGER_BUTTON.checkForInput(CHAR_CREATE_MOUSE_POS):
                    CLASS_SELECT = "ranger"
                if DEFENDER_BUTTON.checkForInput(CHAR_CREATE_MOUSE_POS):
                    CLASS_SELECT = "defender"
                if WIZZARD_BUTTON.checkForInput(CHAR_CREATE_MOUSE_POS):
                    CLASS_SELECT = "wizzard"
                if CONFIRM_BUTTON.checkForInput(CHAR_CREATE_MOUSE_POS):
                    return CLASS_SELECT
               
        pygame.display.update()
        clock.tick_busy_loop( FPS )

def play():
    running = True
    global SCREEN_WIDTH, SCREEN_HEIGHT, FPS
    
    
    while running:
        SCREEN.fill(BLACK)
        intro()
        
        play_again = True
        while (play_again):
            game_active = True
            #player
            character = player_info.char_info()
            player = copy(character)
            class_choice = char_create_ui()
            #get name of player
            player_info.char_create(player, class_choice)
            player.name = f"{player.name} The {player.class_type}"
        
        
        # now we need to have the main game loop 
            while game_active:
                if(player.stats["Health"] <= 0):
                    
                    game_active = False  # haha you're dead    
                    #death scene
                else:
                    main_game_loop(player)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_menu()
                    
                    
    pygame.display.update()
    clock.tick_busy_loop( FPS )             
                 
def change_resolution():
    running = True
    global SCREEN_WIDTH, SCREEN_HEIGHT, FPS, SCREEN,MAIN_MENU_BACKGROUND
    while running:
        
        SCREEN.fill("black")  # fill black first bc it works better
        
        SCREEN.blit(MAIN_MENU_BACKGROUND, (0,0)) #blit means "draw" AKA add to screen
        
        RESOLUTION_MOUSE_POS = pygame.mouse.get_pos() # mouse posn
        
        
        RESOLUTION_TEXT = get_font(100).render("RESOLUTION", True,WHITE)
        RESOLUTION_RECT = RESOLUTION_TEXT.get_rect(center=(SCREEN.get_width()/2, SCREEN.get_height()/7))
        SCREEN.blit(RESOLUTION_TEXT,RESOLUTION_RECT)
        
        
        RESOLUTION_BACK = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/10, SCREEN_HEIGHT - SCREEN_HEIGHT/10), # bottom left 10th of the screen
                            text_input="BACK", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        RESOLUTION_ULTRAWIDE_1080 = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/2, 2*SCREEN_HEIGHT/6), #middle 2/5ths of screen
                            text_input="2560x1080", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        RESOLUTION_1080 = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/2, 3*SCREEN_HEIGHT/6), #middle 2/5ths of screen
                            text_input="1920x1080", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        RESOLUTION_720 = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/2, 4*SCREEN_HEIGHT/6), #middle 2/5ths of screen
                            text_input="1280x720", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        
        
        
        for button in [RESOLUTION_BACK,RESOLUTION_ULTRAWIDE_1080, RESOLUTION_1080,RESOLUTION_720]:  # update button color based on where mouse is
            button.changeColor(RESOLUTION_MOUSE_POS)
            button.update(SCREEN)
        
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESOLUTION_BACK.checkForInput(RESOLUTION_MOUSE_POS):
                    return
                if RESOLUTION_ULTRAWIDE_1080.checkForInput(RESOLUTION_MOUSE_POS):
                    SCREEN_WIDTH = 2560
                    SCREEN_HEIGHT = 1080
                    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                    MAIN_MENU_BACKGROUND = pygame.transform.smoothscale(MAIN_MENU_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
                    pygame.display.flip()
                if RESOLUTION_1080.checkForInput(RESOLUTION_MOUSE_POS):
                    SCREEN_WIDTH = 1920
                    SCREEN_HEIGHT = 1080
                    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                    MAIN_MENU_BACKGROUND = pygame.transform.smoothscale(MAIN_MENU_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
                    pygame.display.flip()
                if RESOLUTION_720.checkForInput(RESOLUTION_MOUSE_POS):
                    SCREEN_WIDTH = 1280
                    SCREEN_HEIGHT = 720
                    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                    MAIN_MENU_BACKGROUND = pygame.transform.smoothscale(MAIN_MENU_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
                    pygame.display.flip()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 
                    
                    
        pygame.display.update()
        clock.tick_busy_loop( FPS ) # set to 60 fps
     
def change_video():
    global SCREEN_WIDTH, SCREEN_HEIGHT, FPS, SCREEN,MAIN_MENU_BACKGROUND
    while True:
        
        SCREEN.fill("black")  # fill black first bc it works better
        
        SCREEN.blit(MAIN_MENU_BACKGROUND, (0,0)) #blit means "draw" AKA add to screen
        
        RESOLUTION_MOUSE_POS = pygame.mouse.get_pos() # mouse posn
        
        
        VIDEO_TEXT = get_font(100).render("Video Options", True,WHITE)
        VIDEO_TEXT_RECT = VIDEO_TEXT.get_rect(center=(SCREEN.get_width()/2, 3*SCREEN.get_height()/10))
        SCREEN.blit(VIDEO_TEXT,VIDEO_TEXT_RECT)
        
        
        VIDEO_BACK = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/10, SCREEN_HEIGHT - SCREEN_HEIGHT/10), # bottom left 10th of the screen
                            text_input="BACK", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        if(FPS == 120):
            FPS_120 = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/2, 5*SCREEN_HEIGHT/10), #middle 2/5ths of screen
                                text_input="120 FPS", font=get_font(40), base_color=RED, hovering_color="Dark Blue")
        else:
            FPS_120 = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/2, 5*SCREEN_HEIGHT/10), #middle 2/5ths of screen
                                text_input="120 FPS", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        if(FPS == 60):
            FPS_60 = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/2, 6*SCREEN_HEIGHT/10), #middle 2/5ths of screen
                                text_input="60 FPS", font=get_font(40), base_color=RED, hovering_color="Dark Blue")
        else:
            FPS_60 = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/2, 6*SCREEN_HEIGHT/10), #middle 2/5ths of screen
                            text_input="60 FPS", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        if(FPS == 30):
            FPS_30 = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/2, 7*SCREEN_HEIGHT/10), #middle 2/5ths of screen
                            text_input="30 FPS", font=get_font(40), base_color=RED, hovering_color="Dark Blue")
        else:
            FPS_30 = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/2, 7*SCREEN_HEIGHT/10), #middle 2/5ths of screen
                            text_input="30 FPS", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        if(FPS == 15):
            FPS_15 = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/2, 8*SCREEN_HEIGHT/10), #middle 2/5ths of screen
                                text_input="15 FPS", font=get_font(40), base_color=RED, hovering_color="Dark Blue")
        else:
            FPS_15 = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/2, 8*SCREEN_HEIGHT/10), #middle 2/5ths of screen
                            text_input="15 FPS", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        
        
        
        for button in [VIDEO_BACK,FPS_120, FPS_60,FPS_30,FPS_15]:  # update button color based on where mouse is
            button.changeColor(RESOLUTION_MOUSE_POS)
            button.update(SCREEN)
        
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if VIDEO_BACK.checkForInput(RESOLUTION_MOUSE_POS):
                    return
                if FPS_120.checkForInput(RESOLUTION_MOUSE_POS):
                    FPS = 120
                if FPS_60.checkForInput(RESOLUTION_MOUSE_POS):
                    FPS = 60
                if FPS_30.checkForInput(RESOLUTION_MOUSE_POS):
                    FPS = 30
                if FPS_15.checkForInput(RESOLUTION_MOUSE_POS):
                    FPS = 15
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 
                    
                    
        pygame.display.update()
        clock.tick_busy_loop( FPS ) # set to 60 fps
           
def options():
    running = True
    
    while running:
        global SCREEN_WIDTH, SCREEN_HEIGHT, FPS,MAIN_MENU_BACKGROUND
        
        SCREEN.fill(BLACK)  # fill black first bc it works better
        MAIN_MENU_BACKGROUND = pygame.transform.smoothscale(MAIN_MENU_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
        SCREEN.blit(MAIN_MENU_BACKGROUND, (0,0)) #blit means "draw" AKA add to screen
        
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos() # mouse posn
        
        
        OPTIONS_TEXT = get_font(100).render("OPTIONS", True,WHITE)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/7))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        
        
        OPTIONS_BACK = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/10, SCREEN_HEIGHT - SCREEN_HEIGHT/10), # bottom right 10th of the screen
                            text_input="BACK", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        OPTIONS_VIDEO = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/2, 3*SCREEN_HEIGHT/5), #middle 2/5ths of screen
                            text_input="VIDEO OPTIONS", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        
        OPTIONS_RESOLUTION = Button(image=pygame.image.load("assets/button.png"), pos=(SCREEN_WIDTH/2, 2*SCREEN_HEIGHT/5), #middle 2/5ths of screen
                            text_input="RESOLUTION", font=get_font(40), base_color=WHITE, hovering_color="Dark Blue")
        
        
        for button in [OPTIONS_BACK, OPTIONS_RESOLUTION, OPTIONS_VIDEO]:  # update button color based on where mouse is
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)
        
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    return 
                
                if OPTIONS_RESOLUTION.checkForInput(OPTIONS_MOUSE_POS):
                    change_resolution()
                if OPTIONS_VIDEO.checkForInput(OPTIONS_MOUSE_POS):
                    change_video()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  
                    
                    
        pygame.display.update()
        clock.tick_busy_loop( FPS ) # set to 60 fps
    
while run: # while game is running
    #global SCREEN_WIDTH, SCREEN_HEIGHT
    for event in pygame.event.get():  #Check events
        if event.type == pygame.QUIT:  #if quit, shut down game and exit from system
            run = False
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.VIDEORESIZE: #If the window is resized, get new size.
            SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            MAIN_MENU_BACKGROUND = pygame.transform.smoothscale(MAIN_MENU_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.flip()
        #     #none of this works
            
        #     MAIN_MENU_BACKGROUND = pygame.transform.smoothscale(MAIN_MENU_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
        #     SCREEN.blit(MAIN_MENU_BACKGROUND, (0,0))
        #     pygame.display.flip()

            
    main_menu()

#make main menu screen

