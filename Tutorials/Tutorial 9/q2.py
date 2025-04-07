# your class definition here
class Thing(object):
	def __init__(self, name):
		self.name = name
		self.owner = None
		self.place = None
	
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
		
	def get_name(self):
		return self.name
	
	def get_place(self):
		return self.place

### uncomment the lines below ###
stone2 = Thing('Stone')
stone2.owner = "beng"
stone2.place = "base" # a Place object whose name is 'base'
### uncomment the lines above ###

print(stone2.get_name())
print(stone2.get_owner())
print(stone2.get_place())
