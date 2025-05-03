"""
The problem is to create a game using Object Oriented Programming, 
with the theme of role playing game. This is a rogue like RPG game, 
where the character will face off against randomly generated foes, 
and the goal is to survive as long as possible. The game features 
main character (the user) with visible health bar, attack damage that 
taken from the weapon given to the user, and vice versa for the foes. 
In addition, the main mechanism of attacking is rolling the dice, which 
the user and the foe will roll the dice and multiply their attack damages. 
The game user's interface includes an opening sequence where user can 
input their name, statistics screen that shows attributes of the user and 
the foe, fighting sequence, and ending sequence. This also output a txt file 
that saves user's game's score.
     *Run both files cps109_a1.py and Enemy.py
     *All files must be in the same directory
"""
import os
import random
import time



class character:
    def __init__(self, name: str, hp: float):
    #create attributes for instances that will be created
        self.name = name
        self.health = hp
        self.max_health = hp
        self.items = fist
    
    
    def dice_roll(self):
    #Method: roll a dice, get random integer from 1 - 6, each has a multiplication
    #that will be multiply towards the attack damage
        dice_num = random.randint(1, 6)
        
        for i in ". . .":
            print(i, end = ' ', flush = True)
            time.sleep(0.1)
        print(f"{self.name} has rolled the number {dice_num}")
        if dice_num == 1:
            return 0.25
        elif dice_num == 2:
            return 0.5
        elif dice_num == 3:
            return 1
        elif dice_num == 4:
            return 1.25
        elif dice_num == 5:
            return 1.5
        elif dice_num == 6:
            return 2
        
    def attack(self, target):
    #Method: attack action.
    #The instance that initiate the method will attack another instance
    #Attack sequence also uses roll the dice method
        damage = ((self.items.damage * self.dice_roll()) - target.items.defend)
        target.health -= max(damage,0)
        target.health = max(target.health, 0)
        time.sleep(0.2)
        return (f"{self.name} has inflicted {max(damage,0)} damage using {self.items.name}\n")
    
    def health_bar(self):
    #Method: Displaying the healthbar for an instance
        bars = 20
        remaining_hp = int(self.health/(self.max_health/bars))
        hp_lost = bars - remaining_hp
        remaining_hp_display = "[]" * remaining_hp
        hp_lost_display = "__" * hp_lost
        return "<" + remaining_hp_display + hp_lost_display +">" + f"   {self.health} hp"
    
    def stats(self, target):
    #Method: Displaying the main attributes of both instances
        print("{:=^40}".format(" STATISTICS "))
        print(f"\nName: {self.name}")
        print(f"Health: {self.health}")
        print(f"Attack damage: {self.items.damage}")
        print(f"Weapon: {self.items.name}")
        print("{:-^40}".format(" VS "))
        print(f"Name: {target.name}")
        print(f"Health: {target.health}")
        print(f"Attack damage: {target.items.damage}")
        print(f"Weapon: {target.items.name}\n")
        print("{:=^40}".format("="))
        print(input("\nPlease press Enter to continue."))
        os.system('clear')
        
        
class items:
    def __init__(self, name: str, i_type: str, dmg: int, defend: int, hp: int, value: int):
    #Attributes for new objects
    #Weapons or items with have this attributes
        self.name = name
        self.item_type = i_type
        self.damage = dmg
        self.defend = defend
        self.add_health = hp
        self.value = value


class main_character(character):
    #subclass of class character, this is the user, with attributes from
    #main class, and addtitional attributes that differentiate user from enemy 
    def __init__(self, name: str, hp: float):
    #getting attributes from main class
        super().__init__(name = name, hp = hp)
        self.default_weapon = self.items
    
    def equip_weapon(self,weapon):
    #Method: equiping an item. 
        self.items = weapon
        print(f"\n{self.name} has equipped {self.items.name}\n")
        
    '''
    def drop_weapon(self):
        self.items = self.default_weapon
        print(f"{self.name} has unequipped {self.default_weapon}")
    '''
    def healing(self):
    #Method: the user will given a prompt to heal after a round
    # This will add health towards the user
        print("\nYou has received a potion.")
        print("\nWould you like to use it?")
        
        answer = input("\nYES [Y] /  NO [N]:  ").lower()
        while answer not in ['yes','y','no','n'] :
            answer = input("Invalid input, please try again\nYES [Y] /  NO [N]:  ").lower()
            
        if answer == 'yes' or answer == 'y':
            self.health += 50
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"\nYour health is now {user.health} hp.")
            for i in ". . . . .":
                print(i, end = ' ', flush = True)
                time.sleep(0.45)    
        elif answer == 'no' or answer == 'n':
            print('\nYou did not use the potion.')
            print('You received a buff in damage. (+5 base damage)')
            print('You received a buff in health. (+5 max health)')
            self.items.damage += 5
            self.max_health += 5
            for i in ". . . . .":
                print(i, end = ' ', flush = True)
                time.sleep(0.45)
            
        else:
            print("Invalid input")
#default weapon            
fist = items("Fist", "weapon", 2, 0,0,1)              

class enemy(character):
    #subclass of class character. This is the enemy, with attributes from 
    #main class, and one more attribute "weapon" so that it
    #enemy could equips weapon and fight back(lol)
    def __init__(self, name: str, hp: float, weapon):
        super().__init__(name, hp) #inherit from character class
        self.items = weapon #this attribute will be imported from another file
    

def intro(): #Intro sequence to the game
    print("\n========================================================")
    print("||        WELCOME TO THE NEVER ENDING DUNGEON!        ||")
    print("========================================================")
    
    print("\nThe Game: You will randomly encountered different foes and the will try to end you. In order to get pass them, you will have to roll the dice, which increases your damageoutputs, or lowers to nothing. The enemy will do the sameand both will attack at the same time.")
    print("\nThe Goal: Stay alive as long as possible")
    print("\nBonus: After each round, you will receive a potion that heals you for 50hp. Refusing to use it will increase your damage and max health by +5 permanently. Risk it and win it!")
    print(input("\nPlease press Enter to continue"))
    
    
def fight_sequence(): 
    #Fight sequence of the game, this is where the user and the enemy fight
    #This include importing random enemy and weapons from another python file,
    #This also includes methods of character, displaying health and prompts.
    from Enemy import enemy_weapon #Import weapon for enemy
    from Enemy import import_enemy #Import random enemy
    foe = import_enemy(enemy_weapon)
    os.system('clear')
    user.equip_weapon(long_sword)
    print(f"You have encountered {foe.name}!\n")
    user.stats(foe)
    print (f"\nHealth of {user.name}")
    print (f"{user.health_bar()}")
    print (f"Health of {foe.name}")
    print (f"{foe.health_bar()}")
    print(input("\nPlease press Enter to roll the dice."))
    
    while foe.health >0: #Loop until the user defeats the enemy
        os.system('clear')
        print(user.attack(foe)) #Attack sequence, which includes rolling the dice
        time.sleep(0.5)
        print(foe.attack(user))
        time.sleep(0.5)
        print (f"Health of {user.name}")
        print (f"{user.health_bar()}")
        print (f"Health of {foe.name}")
        print (f"{foe.health_bar()}")
        if user.health == 0: #when the user is defeated, game over, loop ends.
            print("{:=^40}".format("GAME OVER"))
            print("\nYou have been defeated!")
            print(input("\nPlease press Enter to continue"))
            break
        elif foe.health == 0:
            print(f"\nYou had defeated {foe.name}.")
            user.healing() #Initialize healing method from character
        else:
            print(input("\nPlease press Enter to roll the dice."))
            
        
def end_game():
    #A function that asks the user to end the game after 10 rounds or continue.
    os.system('clear')
    print("Would you like to continue?")
    answer = input("\nYES [Y] /  NO [N]:  ").lower()
    while answer not in ['yes','y','no','n'] :
        answer = input("Invalid input, please try again\nYES [Y] /  NO [N]:  ").lower()
        
    if answer == 'yes' or answer == 'y':
        os.system('clear')
        print('The game continues!')
        False
            
    elif answer == 'no' or answer == 'n':
        os.system('clear')
        print("The Game has ended!")
def credit():
    #final display after the game is finished, also includes the rounds played
    os.system('clear')
    print("{:=^40}".format("="))
    print('{:^40s}'.format('Thank you for playing!'))
    print("{:=^40}".format("="))
    if count_round == 1:    
        print(f'\nYou have completed {count_round} round\n')
    else:
        print(f'\nYou have completed {count_round} rounds\n')

def export_highscore(): #Output game's scores
    print("Would you like to save your scores?")
    answer = input("\nYES [Y] /  NO [N]:  ").lower()
    while answer not in ['yes','y','no','n'] :
        answer = input("Invalid input, please try again\nYES [Y] /  NO [N]:  ").lower()
   
    if answer == 'yes' or answer == 'y':
        file = open('HighScores.txt','a')
        file.write(f"Name:{user.name}, {user.items.damage} dmg, {count_round} rounds")
        file.close
        for i in ". . . . .":
            print(i, end = ' ', flush = True)
            time.sleep(0.35)
        print('Your scores have been saved\n')
        
            
    elif answer == 'no' or answer == 'n':
        print("The game's scores have not been saved")

if __name__ == "__main__":
    #This will prevent any other code above to run if its not the main file that runs the code.
    #Also prevents codes that import this main file to run at the same time.
    
    # This is the whole game sequence, starting with the user equiping
    #a given weapon, then game starts in a loop till the user loses or 
    #choose to quit.
    count_round = 0
    long_sword = items("Long Sword", "weapon", 15, 0, 0, 7)
    os.system('clear')
    intro()
    a = input("Please enter your name: ")
    user = main_character(name= a,hp=100)
    time.sleep(0.3)
    while user.health > 0:
        if count_round%10 == 0 and count_round != 0: 
            end_game()
        else:
            fight_sequence()
            count_round +=1
    credit()
    export_highscore()
    
