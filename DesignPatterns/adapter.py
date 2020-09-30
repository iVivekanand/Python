class Tamil:
	def __init__(self):
		self.name = "Tamil"

	def speak_tamil(self):
		return "Vanakkam!"

class French:
	def __init__(self):
		self.name = "French"

	def speak_french(self):
		return "Bonjour!"

class Adapter:
	def __init__(self, object, **adapter_method):
		self._object = object
		self.__dict__.update(adapter_method)

	def __getattr__(self, attr):
		return getattr(self._object, attr)


objects = []

tamil = Tamil()
french = French()

objects.append(Adapter(tamil, speak=tamil.speak_tamil))
objects.append(Adapter(french, speak=french.speak_french))

for obj in objects:
	print(f"{obj.name} says {obj.speak()}")