# your class definition here
class Thing:
	def __init__(self, name):
		self.name = name
		self.owner = None
	
	def is_owned(self):
		if self.owner is None:
			return False
		else:
			return True
		
	def get_owner(self):
		if self.is_owned():
			return self.owner
		else:
			return None




### uncomment the lines below ###
stone = Thing('stone')
stone2 = Thing('stoning')
stone2.owner = "beng" # a Person object whose name is 'beng'
### uncomment the lines above ###

print(stone.is_owned())
print(stone2.is_owned())
print(stone2.get_owner())