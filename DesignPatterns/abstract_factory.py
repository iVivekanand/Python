class Dog:
	"""One of the objects to be returned"""

	def speak(self):
		return 'Woof!'
	
	def __str__(self):
		return 'Dog'


class DogFactory:
	"""Concrete Factory"""

	def get_pet(self):
		"""Returns a Dog object"""
		return Dog()

	def get_food(self):
		"""Returns a Dog Food object"""
		return 'Dog Food!'


class PetStore:
	"""PetStore houses our Abstract Factory"""

	def __init__(self, pet_factory=None):
		"""pet_factory is our abstract factory"""
		self._pet_factory = pet_factory


	def show_pet(self):
		"""Utility method to display details of objects returned by DogFactory"""
		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print(f"Our pet is {pet}")
		print(f"Our pet says hello by {pet.speak()}")
		print(f"Our pet's food is {pet_food}")

factory = DogFactory()

shop = PetStore(factory)

shop.show_pet()