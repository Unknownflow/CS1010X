#
# CS1010X --- Programming Methodology
#
# Mission 14 Template
#
# Note that written answers should be commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games import *
import random



#################################################################################
#
# CS1010X --- Programming Methodology
#
# Mission 13
#
# Note that written answers should be commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games import *

############
##  Task1 ##
############

class Weapon(Thing):

    ###########
    # Task 1a #
    ###########

    def __init__(self, name, min_dmg, max_dmg):
        super().__init__(name)
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg


    ###########
    # Task 1b #
    ###########

    def min_damage(self):
        return self.min_dmg

    def max_damage(self):
        return self.max_dmg

    ###########
    # Task 1c #
    ###########

    def damage(self):
        dmg_dealt = random.randint(self.min_damage(), self.max_damage())
        return dmg_dealt


def test_task1():
    print('=== Task 1 ===')
    sword = Weapon('sword', 3, 10)
    print(isinstance(sword, Weapon))    # True
    print(isinstance(sword, Thing))     # True

    print('=== Task 1b ===')
    print(sword.min_damage())           # 3
    print(sword.max_damage())           # 10

    print('=== Task 1c ===')
    print(sword.damage())               # Random value between 3 to 10

# uncomment to test task1
# test_task1()


############
##  Task2 ##
############

class Ammo(Thing):

    ###########
    # Task 2a #
    ###########
    def __init__(self, name, weapon, quantity):
        super().__init__(name)
        self.weapon = weapon
        self.quantity = quantity


    ###########
    # Task 2b #
    ###########
    def get_quantity(self):
        return self.quantity


    ###########
    # Task 2c #
    ###########
    def weapon_type(self):
        weapon = self.weapon
        name = weapon.get_name()
        return name


    ###########
    # Task 2d #
    ###########
    def remove_all(self):
        self.quantity = 0

    pass # remove this

def test_task2():
    print('=== Task 2 ===')
    bow = Weapon('bow', 10, 20)
    arrows = Ammo('arrow', bow, 5)
    print(arrows.get_quantity())        # 5
    print(arrows.weapon_type())         # bow
    arrows.remove_all()
    print(arrows.get_quantity())        # 0

# uncomment to test task2
# test_task2()


############
##  Task3 ##
############

class RangedWeapon(Weapon):

    ###########
    # Task 3a #
    ###########
    def __init__(self, name, min_dmg, max_dmg):
        super().__init__(name, min_dmg, max_dmg)
        self.shots = 0


    ###########
    # Task 3b #
    ###########
    def shots_left(self):
        return self.shots


    ###########
    # Task 3c #
    ###########
    def load(self, ammo):
        weapon_type = ammo.weapon_type()
        ammo_qty = ammo.get_quantity()
        if weapon_type == self.get_name():
            self.shots += ammo_qty
            ammo.remove_all()


    ###########
    # Task 3d #
    ###########
    def damage(self):
        if self.shots_left() == 0:
            return 0
        else:
            self.shots -= 1
            return super().damage()




def test_task3():
    print('=== Task 3a ===')
    bow = RangedWeapon('bow', 10, 40)
    print(isinstance(bow, RangedWeapon)) # True
    print(isinstance(bow, Weapon))       # True

    print('=== Task 3b/c ===')
    crossbow = RangedWeapon('crossbow', 15, 45)
    arrows = Ammo('arrow', bow, 5)
    bolts = Ammo('bolt', crossbow, 10)

    bow.load(bolts)
    print(bow.shots_left())         # 0
    print(bolts.get_quantity())     # 10

    bow.load(arrows)
    print(bow.shots_left())         # 5
    print(arrows.get_quantity())    # 0

    print('=== Task 3d===')
    print(crossbow.damage())        # 0
    crossbow.load(bolts)
    print(crossbow.shots_left())    # 10
    print(bolts.get_quantity())     # 0
    print(crossbow.damage())        # Random value between 15 and 45
    print(crossbow.shots_left())    # 9

# uncomment to test task3
# test_task3()


###########
# Task 4a #
###########
class Food(Thing):
    def __init__(self, name, food_value):
        super().__init__(name)
        self.food_value = food_value
    
    def get_food_value(self):
        return self.food_value


###########
# Task 4b #
###########
class Medicine(Food):
    def __init__(self, name, food_value, medicine_value):
        super().__init__(name, food_value)
        self.medicine_value = medicine_value
    
    def get_medicine_value(self):
        return self.medicine_value


def test_task4():
    print('=== Task 4 ===')
    apple = Food('apple', 4)
    print(apple.get_food_value())               # 4
    panadol = Medicine('paracetamol', 0, 5)
    print(panadol.get_food_value())             # 0
    print(panadol.get_medicine_value())         # 5

# uncomment to test task4
# test_task4()


##############
# Task 5a&b  #
##############
class Animal(LivingThing):
    def __init__(self, name, health, food_value, threshold=None):
        if threshold == None:
            threshold = random.randint(0, 4)
        super().__init__(name, health, threshold)
        self.food_value = food_value

    def get_food_value(self):
        return self.food_value

    def go_to_heaven(self):
        place = self.get_place()
        food_name = self.name + " meat"
        food = Food(food_name, self.food_value)
        place.add_object(food)
        return super().go_to_heaven()
    


def test_task5():
    print('=== Task 5a ===')
    bear = Animal('bear', 20, 10, 3)
    print(bear.get_threshold())             # 3
    print(bear.get_food_value())            # 10

    deer = Animal('deer', 15, 6)
    print(deer.get_threshold())             # Random value between 0 and 4 inclusive

    print('=== Task 5b ===')
    BASE.add_object(bear)
    print(named_col(BASE.get_objects()))    # ['bear']
    print(bear.get_place().get_name())      # Base
    bear.go_to_heaven()                     # bear went to heaven!
    print(named_col(BASE.get_objects()))    # ['bear meat']

# uncomment to test task5
# test_task5()
                                                                        #
#################################################################################









#################################################################################
#                                                                               #
# MISSION 14                                                                    #
# TESTING CODE IS BELOW ALL THE TASKS                                           #
#                                                                               #
#################################################################################


#############
##  Task 1 ##
#############

class Tribute(Person):
    ############
    #  Task 1a #
    ############
    def __init__(self, name, health):
        # Tributes will not move by themselves, so set threshold to -1
        super().__init__(name, health, -1)
        self.hunger = 0

    ############
    #  Task 1b #
    ############
    def get_hunger(self):
        return self.hunger

    ############
    #  Task 1c #
    ############
    def add_hunger(self, hunger):
        self.hunger += hunger

        if self.hunger >= 100:
            self.go_to_heaven()
            
    ############
    #  Task 1d #
    ############
    def reduce_hunger(self, hunger):
        self.hunger -= hunger

        if self.hunger < 0:
            self.hunger = 0

    #############
    ##  Task 2 ##
    #############
    def eat(self, food):
        inventory = self.get_inventory()
        if food not in inventory: # no effect if food is not in inventory
            return
        
        food_value = food.get_food_value()
        self.reduce_hunger(food_value)

        if isinstance(food, Medicine):
            medicine_value = food.get_medicine_value()
            self.add_health(medicine_value)
        
        self.remove_item(food)

    ############
    #  Task 3a #
    ############
    def get_weapons(self):
        inventory = self.get_inventory()
        weapon_tup = tuple()

        for item in inventory:
            if isinstance(item, Weapon):
                weapon_tup += (item, )
        
        return weapon_tup

    ############
    #  Task 3b #
    ############
    def get_food(self):
        inventory = self.get_inventory()
        food_tup = tuple()

        for item in inventory:
            if isinstance(item, Food):
                food_tup += (item, )
        
        return food_tup

    ############
    #  Task 3c #
    ############
    def get_medicine(self):
        inventory = self.get_inventory()
        medicine_tup = tuple()

        for item in inventory:
            if isinstance(item, Medicine):
                medicine_tup += (item, )
        
        return medicine_tup

    #############
    ##  Task 4 ##
    #############
    def attack(self, living_thing, weapon):
        weapons = self.get_weapons()
        if weapon not in weapons:
            return 
        
        objects_around = self.objects_around()
        if living_thing not in objects_around:
            return
        
        damage = weapon.damage()
        living_thing.reduce_health(damage)


        





#############
##  Task 5 ##
#############
# You can either draw it here or attach a image file when you submit.




################
# Testing Code #
################


def test_task1():
    print("===== Task 1b ======")
    cc = Tribute("Chee Chin", 100)
    print(cc.get_hunger())          # 0

    print("===== Task 1c ======")
    Base = Place("base")
    cc = Tribute("Chee Chin", 100)
    Base.add_object(cc)
    print(cc.get_place().get_name())    # base
    cc.add_hunger(50)
    print(cc.get_hunger())              # 50
    cc.add_hunger(50)                   # Chee Chin went to heaven!
    print(cc.get_hunger())              # 100
    print(cc.get_place().get_name())    # Heaven

    print("===== Task 1d ======")
    cc = Tribute("Chee Chin", 100)
    cc.add_hunger(10)
    print(cc.get_hunger())          # 10
    cc.reduce_hunger(20)
    print(cc.get_hunger())          # 0

# Uncomment to test task 1
# test_task1()

def test_task2():
    print("===== Task 2 ======")
    cc = Tribute("Chee Chin", 100)
    chicken = Food("chicken", 5)
    aloe_vera = Medicine("aloe vera", 2, 5)

    Base = Place("base")
    Base.add_object(cc)
    Base.add_object(chicken)
    Base.add_object(aloe_vera)

    cc.reduce_health(10)
    cc.add_hunger(4)
    print(named_col(cc.get_inventory()))    # []

    cc.eat(chicken)
    print(cc.get_hunger())                  # 4

    cc.take(chicken)                        # Chee Chin took chicken
    cc.take(aloe_vera)                      # Chee Chin took aloe vera
    print(named_col(cc.get_inventory()))    # ['chicken', 'aloe vera']

    cc.eat(aloe_vera)
    print(cc.get_health())                  # 95
    print(cc.get_hunger())                  # 2

    print(named_col(cc.get_inventory()))    # ['chicken']

    cc.eat(chicken)
    print(cc.get_health())                  # 95
    print(cc.get_hunger())                  # 0
    print(named_col(Base.get_objects()))    # ['Chee Chin']

# Uncomment to test task 2
# test_task2()

def test_task3():
    print("===== Task 3 ======")
    cc = Tribute("Chee Chin", 100)
    chicken = Food("chicken", 5)
    aloe_vera = Medicine("aloe vera", 2, 5)
    bow = RangedWeapon("bow", 4, 10)
    sword = Weapon("sword", 2, 5)

    Base = Place("base")
    Base.add_object(cc)
    Base.add_object(chicken)
    Base.add_object(aloe_vera)
    Base.add_object(bow)
    Base.add_object(sword)

    cc.take(bow)                           # Chee Chin took bow
    cc.take(sword)                         # Chee Chin took sword
    cc.take(chicken)                       # Chee Chin took chicken
    cc.take(aloe_vera)                     # Chee Chin took aloe_vera

    print(named_col(cc.get_inventory()))   # ['bow', 'sword', 'chicken', 'aloe vera']
    print(named_col(cc.get_weapons()))     # ('bow', 'sword')
    print(named_col(cc.get_food()))        # ('chicken', 'aloe vera')
    print(named_col(cc.get_medicine()))    # ('aloe vera',)

# Uncomment to test task 3
# test_task3()

def test_task4():
    print("===== Task 4 ======")
    Base = Place("base")
    cc = Tribute("Chee Chin", 100)
    sword = Weapon("sword", 10, 10)
    bear = Animal("bear", 20, 10)

    Base.add_object(cc)
    Base.add_object(sword)
    Base.add_object(bear)

    print(bear.get_health())                # 20

    cc.attack(bear, sword)
    print(bear.get_health())                # 20

    cc.take(sword)                          # Chee Chin took sword
    cc.attack(bear, sword)
    print(bear.get_health())                # 10

    cc.attack(bear, sword)                  # bear went to heaven
    print(named_col(Base.get_objects()))    # ['Chee Chin', 'bear meat']

    Home = Place("home")
    cat = Animal("cat", 20, 10)
    Home.add_object(cat)
    cc.attack(cat, sword)
    print(cat.get_health())

# Uncomment to test task 4
test_task4()
