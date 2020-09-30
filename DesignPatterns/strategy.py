import types

class Strategy:
	def __init__(self, function=None):
		self.name = "Default"
		if function:
			self.execute = types.MethodType(function, self)

	def execute(self):
		print(f"{self.name} used")


def strategy_one(self):
	print(f"{self.name} is used to execute method 1")

def strategy_two(self):
	print(f"{self.name} is used to execute method 2")

s0 = Strategy()
s0.execute()

s1 = Strategy(strategy_one)
s1.name = "Strategy One"
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()