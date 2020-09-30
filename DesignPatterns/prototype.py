import copy

class Prototype:
	def __init__(self):
		self._objects = {}

	def register_object(self, name, obj):
		self._objects[name] = obj

	def unregister_object(self, name, obj):
		del self._objects[name]

	def clone(self, name, **attr):
		obj = copy.deepcopy(self._objects.get(name))
		obj.__dict__.update(attr)
		return obj


class Car:
	def __init__(self):
		self.name = 'Skylark'
		self.color = 'Blue'
		self.options = 'Ex'

	def __str__(self):
		return f"Model: {self.name}, Color: {self.color}, Options: {self.options}"


car = Car()
prototype = Prototype()
prototype.register_object('skylark', car)

car1 = prototype.clone('skylark')

print(car1)