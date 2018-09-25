class Dog:

	def __init__(self,given_name='',given_breed=''):
		self.color = 'red'
		if len(given_name)>0 and len(given_breed)>0:
			self.name = given_name
			self.breed = given_breed
	
	

	def GetName(self):
		return self.name

	def GetBreed(self):
		return self.breed

pet1 = Dog('porkchop','pug') 
pet2 = Dog()

print(pet1.GetName())
print(pet1.name)

#class Cat:
#	name = 'garfield'
#	breed = 'siamese'

#class Rabbit:
#	name = 'hopper'
#	breed = 'grey'
