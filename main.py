import tkinter as tk
from tkinter import messagebox



#GLOBAL VARS
world_name = 'Placeholder '
classes = {
        1:'warrior', 
        2:'wizzard', 
        3:'rogue'
        }
FONT = 'Arial'



class GUI_control:
    def __init__(self):
        self.root = tk.Tk()
        #opening box dimensions
        self.root.geometry("1280x720")
        #title of box
        self.root.title("RPG WIP")
        
        #Label at top
        self.label = tk.Label(self.root, text = world_name, font = (FONT, 18))
        self.label.pack()
        
        self.display = tk.Text(self.root)
        self.display.pack()
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.columnconfigure(0, weight = 1)
        self.button_frame.columnconfigure(1, weight = 1)
        self.button_frame.columnconfigure(2, weight = 1)
        
        
        #news == north, east, west, south
        #inventory
        self.inventory_btn = tk.Button(self.button_frame, text = 'Inventory', font = (FONT, 16), command = self.show_inventory) 
        self.inventory_btn.grid(row = 0, column = 0, sticky = "news")
        #abilities
        self.ability_btn = tk.Button(self.button_frame, text = 'Abilities', font = (FONT, 16), command = self.show_abilities) 
        self.ability_btn.grid(row = 0, column = 1, sticky = "news")
        #statistics
        self.statistics_btn = tk.Button(self.button_frame, text = 'Statistics', font = (FONT, 16), command = self.show_statistics)  
        self.statistics_btn.grid(row = 1, column = 0, sticky = "news")
        #next
        self.next_btn = tk.Button(self.button_frame, text = 'Next', font = (FONT, 16), command = self.next) 
        self.next_btn.grid(row = 2, column = 2, sticky = "news")
        #back
        self.back_btn = tk.Button(self.button_frame, text = 'Back', font = (FONT, 16), command = self.back) 
        self.back_btn.grid(row = 2, column = 0, sticky = "news")
        
        self.button_frame.pack(fill = 'x', side = 'bottom', padx= 20, pady = 20)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        #self.root.mainloop()
        
    def show_inventory(self):
        self.display.delete("1.0", "end")
        self.display.insert(tk.END, 'Inventory')      
    
    def show_abilities(self):
        self.display.delete("1.0", "end")
        self.display.insert(tk.END, 'Abilities')
    
    def show_statistics(self):
        self.display.delete("1.0", "end")
        self.display.insert(tk.END, 'Statistics')
        
    def next(self):
        self.display.delete("1.0", "end")
        
        pass
    def back(self):
        self.display.delete("1.0", "end")
        
        pass
    def on_closing(self):
        if messagebox.askyesno(title = "Quit?", message = "Do you really want to quit?"):
            self.root.destroy()
        
#prompts user for name and returns it. Ask prompt as parameter
def get_name(message):
     #create character by name
    name_prompt = True
    
    while name_prompt:
        #before call, print what the name is for. 
        name = input(message)
        name_confirm = input('Okay! is the name ' + name + ' correct? y/n: ')
        if(name_confirm == 'y'): name_prompt = False
        
        #incorrect name, loop until player says yes
        while name_confirm != 'y':
            name = input('Please enter a name: ')
            name_confirm = input('Okay! is the name ' + name + ' correct? y/n: ')
            #if name correct, exit loop and continue.
            if(name_confirm == 'y'): name_prompt = False
            
    return name

#create new char -- has prompts
def char_create(player):
    player.name = get_name('Welcome to the game! please enter a name to begin: ')
                                                 
    print(classes)
    choice = input('What class are you? (1,2,3): ' )
    char_type(player,classes[int(choice)])
    
    print('Here are your stats: ') 
    print (player.stats)
    
#choose char types    
def char_type(char_info, class_type):
    # Warior
    if class_type == 'warrior': 
        char_info.stats['health'] = char_info.stats['health'] + 50
        char_info.stats['armor'] = char_info.stats['armor'] + 15
        
    # Wizzard
    elif class_type == 'wizzard':
        char_info.stats['mana'] = char_info.stats['mana'] + 75
        
        
    # Rogue
    elif class_type == 'rogue':
        char_info.stats['speed'] = char_info.stats['speed'] + 15
        char_info.stats['stamina'] = char_info.stats['stamina'] + 50
          

#holds all character info
class char_info():
    stats = {
        "health" : 100,
        "mana": 100,
        "stamina": 100,
        "armor": 0,
        "speed": 100,
        "level": 0 
    }
    
    name = 'EMPTY'
    char_type = 'EMPTY'

    
#main loop
def main():
    gui = GUI_control()
    
    gui.display.insert(tk.END,"Hello")
    #player
    player = char_info()
    #get name of player
    char_create(player)
    print('Welcome to ' + world_name + ', ' + player.name +'!')
   

main()
