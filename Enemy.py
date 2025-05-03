
import random

'''
Here is the list of weapons and enemies that will be randomly chosen
'''

def enemy_weapon():
    from cps109_a1 import items
    all_items = [
         items("Iron Sword", "weapon", 8,0,0,10),
         items("Iron Spear", "weapon", 9,0,0,11),
         items("Iron Dagger", "weapon", 7,0,0,9),
         items("Iron Axe", "weapon", 10,0,0,13),
         items("Rusty Sword", "weapon", 4,0,0,4),
         items("Long Sword", "weapon", 15,0,0,15),
         items("Iron Sword", "weapon", 8,0,0,10),
         items("Iron Spear", "weapon", 9,0,0,11),
         items("Iron Dagger", "weapon", 7,0,0,9),
         items("Iron Axe", "weapon", 11,0,0,13),
         items("Rusty Sword", "weapon", 5,0,0,4),
         items("Long Sword", "weapon", 16,0,0,15),
         items("Iron Sword", "weapon", 9,0,0,10),
         items("Iron Spear", "weapon", 10,0,0,11),
         items("Iron Dagger", "weapon", 6,0,0,9),
         items("Iron Axe", "weapon", 10,0,0,13),
         items("Rusty Sword", "weapon", 4,0,0,4),
         items("Long Sword", "weapon", 15,0,0,15),
         items("Dragon Slayer","weapon",50,0,0,50),
         items("Mace","weapon",12,0,0,12),
         items("Mace","weapon",12,0,0,12),
         items("Mace","weapon",12,0,0,12)
    ]
    return random.choice(all_items)
    

def import_enemy(enemy_weapon):
    from cps109_a1 import enemy
    all_enemy = [
        enemy('Zombie' , 50 , enemy_weapon()),
        enemy('Zombie' , 45 , enemy_weapon()),
        enemy('Zombie' , 55 , enemy_weapon()),
        enemy('Skeleton' ,30 , enemy_weapon()),
        enemy('Skeleton' ,35 , enemy_weapon()),
        enemy('Skeleton' ,25 , enemy_weapon()),
        enemy('Wolf', 15, enemy_weapon()),
        enemy('Wolf', 16, enemy_weapon()),
        enemy('Wolf', 17, enemy_weapon()),
        enemy('Zombie' , 50 , enemy_weapon()),
        enemy('Zombie' , 45 , enemy_weapon()),
        enemy('Zombie' , 55 , enemy_weapon()),
        enemy('Skeleton' ,30 , enemy_weapon()),
        enemy('Skeleton' ,35 , enemy_weapon()),
        enemy('Skeleton' ,25 , enemy_weapon()),
        enemy('Wolf', 15, enemy_weapon()),
        enemy('Wolf', 16, enemy_weapon()),
        enemy('Wolf', 17, enemy_weapon()),
        enemy('Werewolf', 70 , enemy_weapon()),
        enemy('Werewolf', 75 , enemy_weapon()),
        enemy('Werewolf', 65 , enemy_weapon()),
        enemy('Zombie on Zaza', 70, enemy_weapon()),
        enemy('Extra Calcium Skeleton', 60, enemy_weapon()),
        enemy('Weak Werewolf' , 35, enemy_weapon()),
        enemy('Cow Man', 45, enemy_weapon()),
        enemy('Man Cow', 54, enemy_weapon()),
        enemy('Man Man', 55, enemy_weapon()),
        enemy('Cow Cow', 44, enemy_weapon()),
        enemy('Mugger', 35, enemy_weapon()),
        enemy('Mugger', 36, enemy_weapon()),
        enemy('Mugger', 37, enemy_weapon()),
        enemy('Goblin', 25, enemy_weapon()),
        enemy('Goblin', 20, enemy_weapon()),
        enemy('Goblin', 23, enemy_weapon()),
        enemy('Mugger', 35, enemy_weapon()),
        enemy('Mugger', 36, enemy_weapon()),
        enemy('Mugger', 37, enemy_weapon()),
        enemy('Goblin', 25, enemy_weapon()),
        enemy('Goblin', 20, enemy_weapon()),
        enemy('Goblin', 23, enemy_weapon()),
        enemy('Golden Goblin', 80, enemy_weapon()),
        enemy('Serpent', 20, enemy_weapon()),
        enemy('Serpent', 22, enemy_weapon()),
        enemy('Serpent', 24, enemy_weapon()),
        enemy('Super Serpent', 40, enemy_weapon()),
        enemy('Orc', 82, enemy_weapon()),
        enemy('Orc', 80, enemy_weapon()),
        enemy('Orc', 78, enemy_weapon()),
        enemy('Over-sized Orc', 160, enemy_weapon()),
        enemy('Path Stopper', 200, enemy_weapon()),
        enemy('Knight', 100, enemy_weapon()),
        enemy('Knight', 110, enemy_weapon()),
        enemy('Knight', 90, enemy_weapon()),
        enemy('Dice Master', 999, enemy_weapon()),
        enemy('Golem', 200, enemy_weapon()),
        enemy('Giant Golem', 300, enemy_weapon()),
        enemy('Raat',10, enemy_weapon()),
        enemy('Rat',9, enemy_weapon()),
        enemy('Rott',8, enemy_weapon()),
        enemy('Reet',7, enemy_weapon()),
        enemy('Rut',6, enemy_weapon()),
        enemy('Normal Man', 20, enemy_weapon()),
        enemy('King Burger', 350, enemy_weapon()),
        enemy('Queen Dairy', 350, enemy_weapon()),
        enemy('@!$!#%@%#$^$!', 9999, enemy_weapon())
 
    ]
    return random.choice(all_enemy)