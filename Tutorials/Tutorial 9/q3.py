from hungry_games import MobileObject

class Thing(MobileObject):
    def __init__(self, name):
        self.name = name
        self.owner = None

stone = Thing("stone")
stone.get_place()

# An error occurs - AttributeError: 'Thing' object has no attribute 'place'
# This is because there the get_place function is called and tries to look
# for the place attribute in the thing object but as it is not defined
# in the constructor, an AttributeError will thus occur.