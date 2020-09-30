class AtmState():
	name = "state"
	allowed = []

	def goNext(self, state):
		if state.name in self.allowed:
			print(f"Current state: {self}, switched to {state.name}")
			self.__class__ = state
		else:
			print(f"Current state: {self}, switched to {state.name} not possible")			
	def __str__(self):
		return self.name


class Off(AtmState):
	name = "off"
	allowed = ["on"]


class On(AtmState):
	name = "on"
	allowed = ["off"]


class ATM():
	def __init__(self):
		self.current = Off()

	def setState(self, state):
		self.current.goNext(state)

def main():
	atm = ATM()
	atm.setState(On)
	atm.setState(Off)
	atm.setState(On)


if __name__ == "__main__":
	main()