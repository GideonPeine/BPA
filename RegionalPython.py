#128234

import random as rand

# Starting attributes
name = ""
weapon = ""
health = rand.randint(7,10) * 10
gold = 0
strength = rand.randint(12,17)
level = 1
run =True


'''
HELPER STRINGS -- Feel free to copy these lines to aid in your printouts:


A monster is attacking you!
Enter:  '1' to use your ___
        '2' to run away
Choice: ___
You defeated the monster and found ___!
That was rough! You lost ___ health.
Luckily you managed to get past the monster!
Press Enter to continue
___ gold
a health potion. You restored ___ health
Hello, ___
In this dungeon, you will fight three monsters.
If you survive to the end, treasure awaits!
You have your trusty ___, I see.
Good. You will need it.
Press Enter when you are ready to begin...
You made it to the treasure! You found ___ gold!
You didn't find the treasure, but you survived to fight again another day...
You fought as best you could, but didn't make it. 
The treasure waits for the next adventurer...
'''

# Write your functions here


def start_game():
    ''' initalizes the game
    takes in global variables
    inputs name and weapon, calls function to display
    '''
    
    #initalize global variables SC13
    global name
    global weapon
    global health
    global gold
    global strength
    global level
    global run
    
    print("Welcome to the dungeon!")
    enter_name = input("What is your name, adventurer? ")
    enter_weapon = input("What is your weapon of choice? ")
    print("\n")
    
    print("Hello, ", enter_name,
            ".In this dungeon, you will fight three monsters.",
            "If you survive to the end, treasure awaits!",
            "You have your trusty ", enter_weapon ,", I see.",
            "Good. You will need it.")
    
    name = enter_name
    weapon = enter_weapon
    
    del enter_name
    del enter_weapon
    
    display_character(name, level, gold, weapon, health, strength)
    input("Press Enter to Continue")
    
    for days in range(3):
        level=days+1
        global run #update info on run
        if run:
            encounter(days)
            input("Press Enter to Continue")
    if run:
        game_over((days+2)) #SC7
    # Finish this function here
    



def display_character(name, level, gold, weapon, health, strength):
    print("\n") #space out each sequence for better reading
    
    #next lines display information of character #SC1
    print("Name: ", name, "\t", "Level: ", level)
    print("Gold: ", gold, "\t", "Weapon: ", weapon)
    print("Health: ", health, "\t", "Strength: ", strength)
    
    
    
def found_loot():
    print("\n")
    loot_determine=rand.randint(0,10)
    
    #SC3 & SC4
    if loot_determine <3:
        global health
        health_add=(rand.randint(1,3))*10
        print("You found a health potion, which restores ", health_add, "Health!")
        health+=health_add
        
    else:
        global gold
        gold_add=rand.randint(25,150)
        print("You found ", gold_add, "Gold!")
        gold+=gold_add
        

def encounter(days):
    
    global name #SC13
    global weapon
    global health
    global gold
    global strength
    global level
    global run
    
    print("\n")
    print("A monster is attacking you!")
    print("Press 1 to: use your", weapon)
    print("Press 2 to: run away")
    user_choice=10000
    while user_choice>2 or user_choice <1: #SC8
        user_choice=(input("Enter Choice: "))
        try:
            user_choice=int(user_choice)
        except Exception:
            user_choice=10000
    if user_choice ==1:
        
        monster_strength=rand.randint(10,20) #SC9
        
        if monster_strength <= strength:
            print("You beat the monster!")
            found_loot()
            
        else:
            damage_taken=(monster_strength-strength)*10
            health-=damage_taken
            print("That was rough! you lost ", damage_taken, "Health")
            if health<0:
                game_over(days+2)
    else:
        game_over(days+2)
    if not health<0:
        display_character(name, level, gold, weapon, health, strength)
    elif user_choice ==2:
        game_over(days+2)

def game_over(days):
    
    print("\n")
    
    global name #SC13
    global weapon
    global health
    global gold
    global strength
    global level
    global run
    
    run=False
    
    if days>3: #SC11
        print("You made it to the treasure!")
        gold+=rand.randint(500,5000) #SC12
        display_character(name, level, gold, weapon, health, strength)
    elif health>0:
        print("You didn't find the treasure, but you survived to fight another day")
    else:
        print("You fought as the best you could, but didn't make it." ,
              "The treasure waits for the next adventurer . . .")
    if health<0:
        health=0
        
            
            
            



start_game()