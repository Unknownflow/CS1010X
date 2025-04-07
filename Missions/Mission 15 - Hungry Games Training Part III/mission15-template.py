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

# Rename CLARENCE_AI to YourName_AI
class CLARENCE_AI(Tribute):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.prev_direction = None

    def next_action(self):
        # Next action should return a tuple of what your next action should
        # be. For the full list of tuple that your AI can return, refer to
        # the pdf file
        
        # store living things and things into an array
        livingThings = []
        things = []
        for obj in self.objects_around():
            if isinstance(obj, LivingThing):
                livingThings.append(obj)
            elif isinstance(obj, Thing):
                things.append(obj)

        # store ammo, food and medicine into an array
        ammos = []
        foods = []
        medicines = []
        for obj in self.get_inventory():
            if isinstance(obj, Ammo):
                ammos.append(obj)
            elif isinstance(obj, Medicine):
                medicines.append(obj)
            elif isinstance(obj, Food):
                foods.append(obj)
        
        sorted(foods, key = lambda x: x.food_value, reverse=True)
        sorted(medicines, key = lambda x: x.medicine_value, reverse=True)

        
        rangedWeapons = []
        weapons = []
        for obj in self.get_weapons():
            if isinstance(obj, RangedWeapon):
                 rangedWeapons.append(obj)
            elif isinstance(obj, Weapon):
                 weapons.append(obj)
        # sort weapons by average damage by desc order, first will be the weapon with higehst avg dmg
        sorted(rangedWeapons, key = lambda x: (x.min_damage() + x.max_damage()) / 2, reverse=True)
        sorted(weapons, key = lambda x: (x.min_damage() + x.max_damage()) / 2, reverse=True)


        # if there is living things, use weapon to attack a random living thing
        if livingThings:
            rand_idx = random.randrange(0, len(livingThings))
            if rangedWeapons:
                for rangedWeapon in rangedWeapons:
                    # only attack with ranged weapon if there are 1 or more shots
                    if rangedWeapon.shots_left() != 0:
                        # attack with ranged weapon with highest avg dmg
                        return ("ATTACK", livingThings[rand_idx], rangedWeapon)                        
            if weapons:
                # attack with weapon with highest avg dmg
                return ("ATTACK", livingThings[rand_idx], weapons[0])
        
        if things:
            # take a random thing if there is one nearby
            rand_idx = random.randrange(0, len(things))
            return ("TAKE", things[rand_idx])
        
        for ammo in ammos:
            for rangedWeapon in rangedWeapons:
                # find correct ammo to load the ammo into the ranged weapon 
                if ammo.weapon_type() == rangedWeapon.get_name():
                    return ("LOAD", rangedWeapon, ammo)

        if foods:
            return ("EAT", foods[0])
      
        if medicines:
            return ("EAT", medicines[0])

        exits = self.get_exits()
        if exits:
            # if it has not moved off from starting pos
            if self.prev_direction == None:
                rand_idx = random.randrange(0, len(exits))
                self.prev_direction = exits[rand_idx]
                return ("GO", exits[rand_idx])

            found = False
            # loop until direction which is not opposite is found
            while not found:
                rand_idx = random.randrange(0, len(exits))
                direction = exits[rand_idx] 
                print(direction, self.prev_direction)
                if direction != opposite_direction(self.prev_direction):
                    found = True
                    self.prev_direction = direction
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

# Replace CLARENCE_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI
# simulation.task1(CLARENCE_AI("CLARENCE AI", 100), gui=True)


##########
# Task 2 #
##########
## 1. Your AI should be able to pick up a Weapon / RangedWeapon
## 2. Your AI should be able to move around and explore
## 3. Your AI should be able to find harmless Tribute and kill him

# Replace CLARENCE_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI

time_limit = 20    # You may change the time limit if your AI is taking too long
# simulation.task2(CLARENCE_AI("XX AI", 100), time_limit, gui=True)



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
    #ai_clone = CLARENCE_AI("AI Clone", 100)
    #game.add_tribute(ai_clone)

    return game

# Replace CLARENCE_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI
simulation.optional_task(CLARENCE_AI("XX AI", 100), config, gui=True)
