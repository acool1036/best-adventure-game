#This will provide text colors
from colorama import Fore, Back, Style

#This will allow us to create enemys with random traits
import random

#This will allow us to clear the terminal when desired
import os

#Declaring Variables for Global Use
#User Statistics Variables
global level
global levels
global charisma
global intelligence
global strength
global health_points
charisma = 0
intelligence = 0
strength = 0
health_points = 100
levels = [1,2,3,4,5,6,7,8,9,10]
level = 1

#Powerups/Inventory Variables
global t_charisma
global t_strength
global t_intelligence
global instantWin
t_charisma = 0
t_strength = 0
t_intelligence = 0
instantWin = 0

print(Fore.RED + "Welcome to Text Battle Simulator")

# Function to setup charater's values
def char_setup():
    #telling the interpreter i want to use the global variable
    global charisma
    global intelligence
    global strength
    global health_points
    
    
    #Begin Setup
    # This Variable is the maximum total points per trait
    trait_points = 200
    print(Fore.WHITE + "You will now select your trait values\nList of Traits:\nCharisma\nStrength\nIntelligence")
    
    # Adding a Charisma Value
    print(str(trait_points) + " Trait Points Remaining\n")
    charisma = int(input(Fore.CYAN + "Enter a charisma value between 1 and 100: " + Fore.WHITE))
    
    if (charisma < 101 and charisma >= 0 and trait_points >= charisma):
        trait_points = trait_points-charisma
    else:
        charisma = 0 
    
   # Adding a Strength Value
    print(str(trait_points) + " Trait Points Remaining\n")
    strength = int(input(Fore.CYAN + "Enter a Strength value between 1 and 100: " + Fore.WHITE))
    
    if (strength < 101 and strength >= 0 and trait_points >= strength):
        trait_points = trait_points-strength
    else:
        strength - 0
    #Adding an Intelligence Value
    print(str(trait_points) + " Trait Points Remaining\n")
    intelligence = int(input(Fore.CYAN + "Enter an Intelligence value between 1 and 100: " + Fore.WHITE))
    
    if (intelligence < 101 and intelligence >= 0 and trait_points >= intelligence):
        trait_points = trait_points-intelligence
        health_points = 100
    else:
        intelligence = 0
    #Clearing the Terminal
   

#This will create an enemy when called, levels increase minimum threshold by 5%
#Possible values are 1-10
def create_enemy():
    #this makes the variables useable in the battle() function
    global enemy_charisma
    global enemy_inteligence
    global enemy_strength
    global level
    #this variable runs the while loop
    enemy_total = 0

   # This maxes out the minimum threshold to 50
    if (level >=10):
        while (enemy_total == 0 or enemy_total > 200):
            enemy_charisma = random.randint(50, 115)
            enemy_strength = random.randint(50, 115)
            enemy_inteligence = random.randint(50, 115) 
            enemy_total = enemy_charisma + enemy_inteligence + enemy_strength

    #this while loop will generate an enemy with maximum health points of 200
    #(like the character) it will keep trying untill it meets the criteria
    else:
        while (enemy_total == 0 or enemy_total > 200):
            enemy_charisma = random.randint(level*5, 110)
            enemy_strength = random.randint(level*5, 110)
            enemy_inteligence = random.randint(level*5, 110) 
            enemy_total = enemy_charisma + enemy_inteligence + enemy_strength  
        
#This runs the battle simulation
def battle():

    #Telling the interpreter I want to use the global variables
    global t_charisma
    global t_strength
    global t_intelligence
    global instantWin
    global enemy_charisma
    global enemy_inteligence
    global enemy_strength
    global charisma
    global intelligence
    global strength
    global health_points
    global levels
    global level
    
    #Check for chest
    chest()
    #Print Traits and ask for powerup
    print("Start level " + str(level))
    print(Fore.RED + "Trait Values:" + Fore.GREEN + "\n Charisma: " +str(charisma) + "\n Stength: " + str(strength) + "\n Intelligence: " + str(intelligence))
    create_enemy()
    use_powerup = input(Fore.CYAN + "Would you like to use a powerup? [y/n]: " + Fore.WHITE)
    #Powerup Logic
    if (use_powerup == "y" or use_powerup == "Y"):
        print(Fore.RED + "Powerups:" + Fore.GREEN + "\n 1. Temp Charisma    | Owned: " + str(t_charisma) + "\n 2. Temp Strength    | Owned: " + str(t_strength) + "\n 3. Temp Inteligence | Owned: " + str(t_intelligence) + "\n 4. Instant Win      | Owned: " + str(instantWin))
        used_powerup = int(input(Fore.CYAN + "Wich would you like to use?: " + Fore.WHITE))
        if (used_powerup == 1 and t_charisma >= 1):
            t_charisma = t_charisma - 1
            print(Fore.RED + "Temp Charisma is Activated")
        elif (used_powerup == 2 and t_strength >= 1):
            t_strength = t_strength - 1
            print(Fore.RED + "Temp Strength is Activated")
        elif (used_powerup == 3 and t_intelligence >= 1):
            t_intelligence = t_intelligence - 1
            print(Fore.RED + "Temp Inteligence is Activated")
        elif (used_powerup == 4 and instantWin >= 1):
            instantWin = instantWin - 1
            print(Fore.RED + "Instant Win is Activated")
    else:
        print(Fore.RED + "No Powerup Used")
        used_powerup = 0
    #Battle Input
    print(Fore.RED + "Select Trait To Use:" + Fore.GREEN + "\n 1. Charisma: " +str(charisma) + "\n 2. Stength: " + str(strength) + "\n 3. Intelligence: " + str(intelligence))   
    used_trait = input(Fore.CYAN + "Which trait would you like to use? " + Fore.WHITE)
   #Following this is all game logic
    # Use Auto Win Cheat Code
    if (used_trait == "opSkip" or used_powerup == 4):
        print("You Won! \U0001F389 , You used InstantWin")
        health_points = health_points + 100
        print("You now have " +str(health_points) + "Health Points")
        levels[level-1] = "Won"
    #Charisma Elif
    elif (used_trait == "1"):
        
        if (used_powerup == 1):
            if (charisma + 10 > enemy_charisma):
                print(Fore.GREEN + "You Won! \U0001F389 , You used Used Charisma \n Your Charisma: " + str(charisma) + "\n Enemy's Charisma: " + str(enemy_charisma))
                health_points = health_points + (charisma - enemy_charisma)
                print(Fore.RED + "You now have " + str(health_points) + " Health Points")
                levels[level-1] = "Won"
            elif (charisma + 10 < enemy_charisma):
                print(Fore.GREEN + "You Lost! \u2639 , You used Used Charisma \n Your Charisma: " + str(charisma) + "\n Enemy's Charisma: " + str(enemy_charisma))
                health_points = health_points - (enemy_charisma - charisma)
                print(Fore.RED + "You now have " + str(health_points) + " Health Points")
                levels[level-1] = "Lost"
        elif (used_powerup != 1):
            if (charisma > enemy_charisma):
                print(Fore.GREEN + "You Won! \U0001F389 , You used Used Charisma \n Your Charisma: " + str(charisma) + "\n Enemy's Charisma: " + str(enemy_charisma))
                health_points = health_points + (charisma - enemy_charisma)
                print(Fore.RED + "You now have " + str(health_points) + " Health Points")
                levels[level-1] = "Won"
            elif (charisma < enemy_charisma):
                print(Fore.GREEN + "You Lost! \u2639 , You used Used Charisma \n Your Charisma: " + str(charisma) + "\n Enemy's Charisma: " + str(enemy_charisma))
                health_points = health_points - (enemy_charisma - charisma)
                print(Fore.RED + "You now have " + str(health_points) + " Health Points")
                levels[level-1] = "Lost"
    #Strength Elif
    elif (used_trait == "2"):
        
        #if you used Temp Strength
        if (used_powerup == 2):
            if (strength + 10 > enemy_strength):
                print(Fore.GREEN + "You Won! \U0001F389 , You used Used Strength \n Your Strength: " + str(strength) + "\n Enemy's Strength: " + str(enemy_strength))
                health_points = health_points + (strength + 10 - enemy_strength)
                print(Fore.RED + "You now have " + str(health_points) + " Health Points")
                levels[level-1] = "Won"
            elif (strength + 10 < enemy_strength):
                print(Fore.GREEN + "You Lost! \u2639 , You used Used Strength \n Your Strength: " + str(strength) + 10 + "\n Enemy's Strength: " + str(enemy_strength))
                health_points = health_points - (enemy_strength - strength)
                print(Fore.RED + "You now have " + str(health_points) + " Health Points")
                levels[level-1] = "Lost"
        #if you didnt use temp strength
        if (used_powerup != 2):
            if (strength > enemy_strength):
                print(Fore.GREEN + "You Won! \U0001F389 , You used Used Strength \n Your Strength: " + str(strength) + "\n Enemy's Strength: " + str(enemy_strength))
                health_points = health_points + (strength - enemy_strength)
                print(Fore.RED + "You now have " + str(health_points) + " Health Points")
                levels[level-1] = "Won"
            elif (strength < enemy_strength):
                print(Fore.GREEN + "You Lost! \u2639 , You used Used Strength \n Your Strength: " + str(strength)+ "\n Enemy's Strength: " + str(enemy_strength))
                health_points = health_points - (enemy_strength - strength)
                print(Fore.RED + "You now have " + str(health_points) + " Health Points")
                levels[level-1] = "Lost"
   #Intelligence Elif
    elif (used_trait == "3"):
        #if you used Temp Intelligence
        
        if (used_powerup == 3):
            if (intelligence + 10 > enemy_inteligence):
                print(Fore.GREEN + "You Won! \U0001F389 , You used Used Intelligence \n Your Inteligence: " + str(intelligence) + "\n Enemy's Intelligence: " + str(enemy_inteligence))
                health_points = health_points + (intelligence + 10 - enemy_inteligence)
                print(Fore.RED + "You now have " + str(health_points) + " Health Points")
                levels[level-1] = "Won"
            elif (intelligence + 10 < enemy_inteligence):
                print(Fore.GREEN + "You Lost! \u2639 , You used Used Intelligence \n Your Intelligence: " + str(intelligence) + 10 + "\n Enemy's Intelligence: " + str(enemy_inteligence))
                health_points = health_points - (enemy_inteligence - intelligence)
                print(Fore.RED + "You now have " + str(health_points) + " Health Points")
                levels[level-1] = "Lost"
        #if you didnt use temp Intelligence
        if (used_powerup != 3):
            if (intelligence> enemy_inteligence):
                print(Fore.GREEN + "You Won! \U0001F389 , You used Used Intelligence \n Your Intelligence: " + str(intelligence) + "\n Enemy's Intelligence: " + str(enemy_inteligence))
                health_points = health_points + (intelligence - enemy_inteligence)
                print(Fore.RED + "You now have " + str(health_points) + " Health Points")
                levels[level-1] = "Won"
            elif (intelligence < enemy_inteligence):
                print(Fore.GREEN + "You Lost! \u2639 , You used Used Intelligence \n Your Intelligence: " + str(intelligence)+ "\n Enemy's Intelligence: " + str(enemy_inteligence))
                health_points = health_points - (enemy_inteligence - intelligence)
                print(Fore.RED + "You now have " + str(health_points) + " Health Points")
                levels[level-1] = "Lost"
    print(Fore.GREEN + "Level Completed")
    input(Fore.CYAN + "Press Enter To Continue")
    level = level + 1
#This Runs the Shop
def shop():
    #The Shop Edits these
    global t_charisma
    global t_intelligence
    global t_strength
    global health_points
    global instantWin
    #Display shop
    print(Fore.RED + "Welcome To The Shop:")
    print(Fore.GREEN + " 1. Buy\n 2. Empty Inventory\n 3. Leave")
    shopact = input(Fore.CYAN + "What would you like to do? " + Fore.WHITE)
    if (shopact == "1"):
        print(Fore.RED + "Powerup | Cost | Description | Owned")
        print(Fore.GREEN+ " 1. Temp Charisma | 50 HP | +10 Charisma for 1 Battle | Owned: " + str(t_charisma))
        print(Fore.GREEN+ " 2. Temp Strength | 50 HP | +10 Strength for 1 Battle | Owned: " + str(t_strength))
        print(Fore.GREEN+ " 3. Temp Intelligence | 50 HP | +10 Intelligence for 1 Battle | Owned: " + str(t_intelligence))
        print(Fore.GREEN+ " 4. Instant Win | 750 HP | Instant Win 1 Battle | Owned: " + str(instantWin))
        print(Fore.MAGENTA+ "Type [q] to exit")
        #Local variable takes user to each case
        whatbuy = int(input(Fore.CYAN + "What Would you like to buy?"))
        #Item Buying Logic
        if (whatbuy == 1 and health_points > 50):
            health_points = health_points - 50
            t_charisma = t_charisma + 1
            print(Fore.RED + "Temp Charisma Bought")
            print("You now have " + str(health_points) + " Health Points And" + str(t_charisma) + " Temp Charisma(s)")
        elif (whatbuy == "2" and health_points > 50):
            health_points = health_points - 50
            t_strength = t_strength + 1
            print(Fore.RED + "Temp Strength Bought")
            print("You now have " + str(health_points) + " Health Points And" + str(t_strength) + " Temp Strength(s)")
        elif (whatbuy == "3" and health_points > 50):
            health_points = health_points - 50
            t_intelligence = t_intelligence + 1
            print(Fore.RED + "Temp Intelligence Bought")
            print("You now have " + str(health_points) + " Health Points And" + str(t_intelligence) + " Temp Intelligence(s)")
        elif (whatbuy == "4" and health_points > 750):
            health_points = health_points - 750
            instantWin = instantWin + 1
            print(Fore.RED + "Instant Win Bought")
            print("You now have " + str(health_points) + " Health Points And" + str(instantWin) + " Instant Win(s)")
        elif (whatbuy == "q" or whatbuy == "Q"):
            exit = input(Fore.CYAN + "Exit Shop? [y/n]" + Fore.WHITE)
            if (exit == "Y" or exit == "y"):
                menu()
            elif (exit == "N" or exit == "n"):
                shop()
        else:
            shop()
    #Erasing Inventory Option
    elif (shopact == "2"):
        empty = input(Fore.CYAN + "Are you sure you want to empty your inventory? [y/n]")
        if (empty == "y" or empty == "Y"):
            t_charisma = 0
            t_intelligence = 0
            t_strength = 0
            instantWin = 0
            print("Inventory Cleared Sucessfully")
            exit = input(Fore.CYAN + "Exit Shop? [y/n]" + Fore.WHITE)
            if (exit == "Y" or exit == "y"):
                menu()
            elif (exit == "N" or exit == "n"):
                shop()
    #exit shop
    elif (shopact == "3"):
        print("Exiting Shop")
    else:
        shop()
#Game Help Funtion
def game_help():
    #Prints Game Info
    print(Fore.RED + "Text Battle Simulator Help" + Fore.GREEN + "\nCharts Will Be Shown In Green" + Fore.RED + "\nTitles Will Be Shown In Red" )
    input(Fore.CYAN + "Inputs Will Be Shown In Cyan. Press Enter to go back to the menu ")
    
def chest():
    global level
    global t_charisma
    global t_strength
    global t_intelligence
    global health_points
    global instantWin
    openchest = False
    if ((level % 5 == 0 or level == 1) ):
        print(Fore.RED + "You Have Found a Chest")
        openchest = input(Fore.CYAN + "Would you like to open it? [y/n] " + Fore.WHITE)
        print(Fore.RED)
        if (openchest == "Y" or openchest == "y"):
            gift = random.randint(1,6) 
            if (gift == 1) :
                t_charisma = t_charisma + 1
                print("The Chest granted you Temp Charisma!")
            
            elif (gift == 2):
                t_strength = t_strength + 1
                print("The Chest granted you Temp Strength!")
            
            elif (gift == 3):
                t_intelligence = t_intelligence + 1
                print("The Chest granted you Temp Intelligence!")
            elif (gift == 4):
                instantWin = instantWin + 1
                print("The Chest granted you Instant Win")
            elif (gift == 5):
                plus_hp = random.randint(50,2000)
                health_points = health_points + plus_hp
                print("The Chest granted you +" + str(plus_hp) + "Health Points!")
            else:
                print("The Chest granted you nothing.")
    else:
        return 0



#Reset Character Function
def reset():
    #Uses these so it can reset
    global level
    global levels
    global charisma
    global intelligence
    global strength
    global health_points
    global t_charisma
    global t_intelligence
    global t_strength
    global health_points
    global instantWin
    #Reset Prompt
    reset = input(Fore.CYAN + "Are You Sure You Want To Reset? [y/n]" + Fore.WHITE)
    if (reset == "y" or reset == "Y"):
         level = 1
         levels = [0,0,0,0,0,0,0,0,0,0]
         charisma = 0
         intelligence = 0
         strength = 0
         health_points = 100
         t_charisma = 0
         t_intelligence = 0
         t_strength = 0
         instantWin = 0
         print("Progress Reset")
         input("Pres Enter To Continue")
         char_setup()
    elif (reset == "n" or reset == "N"):
        return 0

#Ingame Menu
def menu():
    # level is called for the start level option
    global level
    
    #Display main menu
    print(Fore.RED + "Options:")
    print(Fore.GREEN + " 1. Start Level " + str(level) + "\n 2. Shop \n 3. Help \n 4. Reset Progress")
    menu_select = input(Fore.CYAN + "What would you like to do? " + Fore.WHITE)
    #Main Menu Logic
    if (menu_select == "1"):
        battle()
    elif (menu_select == "2"):
        shop()
    elif (menu_select == "3"):
        game_help()
    elif (menu_select == "4"):
        reset()

#Campaign Game Mode
def campaign():
    #Begin Main App
    char_setup()
    # 10 Levels in Campaign Mode
    while (level <= 10):
        menu()
    #Print Win Statistics
    print(Fore.RED + "Game Completed:")
    print(Fore.GREEN + "Level 1" + str(levels[0]))
    print(Fore.GREEN + "Level 2" + str(levels[1]))
    print(Fore.GREEN + "Level 3" + str(levels[2]))
    print(Fore.GREEN + "Level 4" + str(levels[3]))
    print(Fore.GREEN + "Level 5" + str(levels[4]))
    print(Fore.GREEN + "Level 6" + str(levels[5]))
    print(Fore.GREEN + "Level 7" + str(levels[6]))
    print(Fore.GREEN + "Level 8" + str(levels[7]))
    print(Fore.GREEN + "Level 9" + str(levels[8]))
    print(Fore.GREEN + "Level 10" + str(levels[9]))

#Freeplay Game Mode
def freeplay():
     #Begin Main App
    char_setup()
    while 1:
        menu()
#Actual Game Code
#Clear the terminal
os.system('clear')
#Main Menu
print(Fore.RED + "Select Game Mode")
print(Fore.GREEN + " 1. Free Play\n 2. Campaign")
gamemode = input(Fore.CYAN + "Which game mode would you like to play? " + Fore.WHITE)
if (gamemode == "1"):
    freeplay()
elif (gamemode == "2"):
    campaign()
