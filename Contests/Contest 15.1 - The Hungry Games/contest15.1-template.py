#
# CS1010X --- Programming Methodology
#
# Contest 15.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games_classes import *
from contest_simulation import *
import random


class Player(Tribute):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.prev_direction = None
        self.global_directions = [
            'NORTH', 'EAST', 'UP', 'SOUTH', 'WEST', 'DOWN']

    # Helper functions
    def opposite_direction(self, direction):
        index = ['NORTH', 'EAST', 'UP', 'SOUTH',
                 'WEST', 'DOWN'].index(direction)
        index = (index+3) % 6
        return self.global_directions[index]

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

        # sort foods by food value in desc order
        # sort medicine by medicine value in desc order
        foods = sorted(foods, key=lambda x: x.food_value, reverse=True)
        medicines = sorted(
            medicines, key=lambda x: x.medicine_value, reverse=True)

        rangedWeapons = []
        weapons = []
        for obj in self.get_weapons():
            if isinstance(obj, RangedWeapon):
                rangedWeapons.append(obj)
            elif isinstance(obj, Weapon):
                weapons.append(obj)
        # sort weapons by average damage by desc order, first will be the weapon with higehst avg dmg
        rangedWeapons = sorted(rangedWeapons, key=lambda x: (
            x.min_damage() + x.max_damage()) / 2, reverse=True)
        weapons = sorted(weapons, key=lambda x: (
            x.min_damage() + x.max_damage()) / 2, reverse=True)

        # if there is living things, use weapon to attack a random living thing
        if livingThings:
            rand_idx = random.randrange(0, len(livingThings))
            if rangedWeapons:
                for rangedWeapon in rangedWeapons:
                    # only attack with ranged weapon if there are 1 or more shots
                    if rangedWeapon.shots_left() != 0:
                        # attack with ranged weapon with highest avg dmg if dmg is higher than weapon dmg
                        if weapons and weapons[0].min_damage() < rangedWeapon.min_damage():
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

        if foods and self.get_hunger() > 50:
            return ("EAT", foods[0])

        if medicines and self.get_health() > 100:
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
                if direction != self.opposite_direction(self.prev_direction):
                    found = True
                    self.prev_direction = direction
                    return ("GO", exits[rand_idx])

        # If no possible actions, do nothing
        return None


#######################################
# Testing Code
#######################################

# We only execute code inside the if statement if this file is
# not being imported into another file
if __name__ == '__main__':
    def qualifer_map(size, wrap):
        game_config = GameConfig()
        game_config.set_item_count(Weapon, 10)
        game_config.set_item_count(RangedWeapon, 10)
        game_config.set_item_count(Food, 10)
        game_config.set_item_count(Medicine, 10)
        game_config.set_item_count(Animal, 10)
        game_config.steps = 1000

        def spawn_wild_animals(game):
            for i in range(3):
                animal = DefaultItemFactory.create(WildAnimal)
                game.add_object(animal[0])
                GAME_LOGGER.add_event("SPAWNED", animal[0])
        game_config.add_periodic_event(
            20, spawn_wild_animals, "Spawn Wild Animals")

        return (GameMap(size, wrap=wrap), game_config)

    # Create 6 AI Clones
    tributes = []
    for i in range(6):
        # An AI is represented by a tuple, with the Class as the first element,
        # and the name of the AI as the second
        ai = (Player, "AI" + str(i))
        tributes.append(ai)

    # Qualifier Rounds
    # Uncomments to run more rounds, or modify the rounds list
    # to include more rounds into the simulation
    # (Note: More rounds = longer simulation!)
    rounds = [qualifer_map(4, False),
              # qualifer_map(4, False),
              # qualifer_map(4, False),
              qualifer_map(4, True),
              # qualifer_map(4, True),
              # qualifer_map(4, True),
              ]

    match = Match(tributes, rounds)
    print("Simulating matches... might take a while")

    # Simulate without the graphics
    match.text_simulate_all()

    # Simulate a specific round with the graphics
    # Due to limitation in the graphics framework,
    # can only simulate one round at a time
    # Round id starts from 0
    # match.gui_simulate_round(0)
