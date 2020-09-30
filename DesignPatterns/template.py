import sys
from abc import ABC, abstractmethod


class AbstractClass(ABC):
	def template_method(self):
		self.__always_do_this()
		self.do_step_1()
		self.do_step_2()
		self.do_this_or()

	def __always_do_this(self):
		name = sys._getframe().f_code.co_name
		print('{}.{}'.format(self.__class__.__name__, name))

	@abstractmethod
	def do_step_1(self):
		pass

	@abstractmethod
	def do_step_2(self):
		pass

	def do_this_or(self):
		print('You can overide me but you do not have to')


class ConcreteClassA(AbstractClass):
	def do_step_1(self):
		print(f"Doing step 1 for ConcreteClassA")

	def do_step_2(self):
		print(f"Doing step 2 for ConcreteClassA")


class ConcreteClassB(AbstractClass):
	def do_step_1(self):
		print(f"Doing step 1 for ConcreteClassB")

	def do_step_2(self):
		print(f"Doing step 2 for ConcreteClassB")

	def do_this_or(self):
		print(f"Doing my own business in CCB")


def main():
	print(f"==ConcreteClassA==")
	a = ConcreteClassA()
	a.template_method()

	print(f"==ConcreteClassB==")
	b = ConcreteClassB()
	b.template_method()


if __name__ == "__main__":
	main()