class SubsystemA:
	def method1(self):
		print(f"SSA Method 1")

	def method2(self):
		print(f"SSA Method 2")


class SubsystemB:
	def method1(self):	
		print(f"SSB Method 1")

	def method2(self):
		print(f"SSB Method 2")


class Facade:
	def __init__(self):
		self._ssa = SubsystemA()
		self._ssb = SubsystemB()

	def method(self):
		self._ssa.method1()
		self._ssa.method2()
		self._ssb.method1()
		self._ssb.method2()


def main():
	facade = Facade()
	facade.method()


if __name__ == "__main__":
	main()