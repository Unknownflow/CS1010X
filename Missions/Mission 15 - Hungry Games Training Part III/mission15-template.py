#
# CS1010X --- Programming Methodology
#
# Mission 15 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games_classes import *
from engine import *
import simulation
import random

# Rename XX_AI to YourName_AI
class CLARENCE_AI(Tribute):
    def next_action(self):
        # Next action should return a tuple of what your next action should
        # be. For the full list of tuple that your AI can return, refer to
        # the pdf file
        
        if self.get_weapons():
            # if tribute has weapon, look for living things around him to kill
            for obj in self.objects_around():
                if isinstance(obj, LivingThing):
                    # if living thing is found, find weapon to use to kill it
                    for weapon in self.get_weapons():
                        if isinstance(weapon, RangedWeapon):
                            # if ranged weapon has 1 or more shots, it can be used
                            if weapon.shots_left() > 0:
                                return ("ATTACK", obj, weapon)
                        else:
                            return ("ATTACK", obj, weapon)
        
        objects = self.objects_around()
        for obj in objects:
            # look for Thing objects around tribute and add to actions
            if isinstance(obj, Thing):
                return ("TAKE", obj)
        
        inventory = self.get_inventory()
        for obj in inventory:
            if isinstance(obj, Ammo):
                # if obj is an Ammo object, find corresponding RangedWeapon object
                for obj2 in inventory:
                    if obj.weapon_type() == obj2.get_name():
                        # add Load RangedWeapon object with Ammo object 
                        return ("LOAD", obj2, obj)
            elif isinstance(obj, Food):
                # add eat Food object to action
                return ("EAT", obj)
            elif isinstance(obj, Medicine):
                # add eat Medicine object to action
                return ("EAT", obj)

        
        exits = self.get_exits()
        if exits:
            rand_idx = random.randrange(0, len(exits))
            return ("GO", exits[rand_idx])
        
        # If no possible actions, do nothing
        return None


# NOTE: DO NOT remove the 2 lines of code below.
#
# In particular, you will need to modify the `your_AI = CLARENCE_AI` line so that
# `CLARENCE_AI` is the name of your AI class.
# For instance, if your AI class is called `MyPrecious_AI`, then you have to
# modify that line to:
#
#     your_AI = MyPrecious_AI
#
# Failure to do so will result in the following exception on Coursemology when
# you run the test cases:
#
#     Traceback (most recent call last):
#       in <module>
#     NameError: name 'your_AI' is not defined
#
# You have been warned!
time_limit = 50 # Modify if your AI needs more than 50 moves for task 2
your_AI = CLARENCE_AI # Modify if you changed the name of the AI class


##################
# Simulation Code
##################
##########
# Task 1 #
##########
# Goal:
# 1. Your AI should be able to pick up a Weapon / RangedWeapon
# 2. Your AI should be able to kill chicken
# 3. Your AI should be able to pick up chicken_meat after killing chicken

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI
#simulation.task1(XX_AI("XX AI", 100), gui=True)


##########
# Task 2 #
##########
## 1. Your AI should be able to pick up a Weapon / RangedWeapon
## 2. Your AI should be able to move around and explore
## 3. Your AI should be able to find harmless Tribute and kill him

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI

time_limit = 20    # You may change the time limit if your AI is taking too long
#simulation.task2(XX_AI("XX AI", 100), time_limit, gui=True)



#################
# Optional Task
#################
## You can create your own map and see how your AI behaves!

# Define the parameters of the map
def config():
    ## The game should have a 3x3 map
    game_map = GameMap(3)

    ## You can change the numbers to create different kinds of maps for
    ## the optional task.
    game_config = GameConfig()
    game_config.set_item_count(Weapon, 3)
    game_config.set_item_count(Animal, 10)
    game_config.set_item_count(RangedWeapon, 5)
    game_config.set_item_count(Food, 5)
    game_config.set_item_count(Medicine, 5)

    game = GameEngine(game_map, game_config)

    # Add some dummy tributes
    ryan = Tribute("Ryan", 100)
    waihon = Tribute("Wai Hon", 100)
    soedar = Tribute("Soedar", 100)

    game.add_tribute(ryan)
    game.add_tribute(waihon)
    game.add_tribute(soedar)

    # Yes, your AI can fight with himself
    #ai_clone = XX_AI("AI Clone", 100)
    #game.add_tribute(ai_clone)

    return game

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI
#simulation.optional_task(XX_AI("XX AI", 100), config, gui=True)
