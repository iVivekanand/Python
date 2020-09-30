class Dog:
	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Woof!"


class Cat:
	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Meow!"

def get_pet(pet="dog"):
	pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
	return pets[pet]


print(get_pet("dog").speak())
print(get_pet("cat").speak())