from hungry_games import *

beng_office = Place("beng_office")
bing_office = Place("bing_office")
beng = Person("beng", 100, 3)
bing = Person("bing", 100, 2)
beng_office.add_object(beng)
bing_office.add_object(bing)

ice_cream = Thing("ice_cream") 
ice_cream.owner = beng 

print(ice_cream.get_name())
print(ice_cream.get_owner())
print(ice_cream.get_owner() == beng)

beng.ice_cream = ice_cream

# q6
# The last two statements are modifying the object values directly and they
# are not modifying using the setter functions in the object. This breaks
# the abstraction of the object.

# q7
rum_and_raisin = NamedObject("ice_cream")
print(ice_cream is rum_and_raisin)
# ice_cream and rum_and_raisin are not the same object as ice_cream
# is rum_and_raisin does not evaluate to True.

# q8
burger1 = Thing("burger")
burger2 = Thing("burger")
print(burger1 == burger2)
# burger1 and burger2 are not the same object. 
# burger1 == burger2 resolves to False
# I would use the is function to compare the two objects and if both 
# objects have the same name and are located in the same location,
# the result will be True, otherwise it will be False.