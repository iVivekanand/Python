class Command:
	def execute(self):
		pass


class Copy(Command):
	def execute(self):
		print(f"Copy command")


class Paste(Command):
	def execute(self):
		print(f"Paste command")


class Save(Command):
	def execute(self):
		print(f"Save command")


class Macro: # Invoker
	def __init__(self):
		self.commands = []

	def add(self, command):
		self.commands.append(command)

	def run(self):
		for command in self.commands:
			command.execute()


def main():
	macro = Macro()
	macro.add(Copy())
	macro.add(Paste())
	macro.add(Save())
	macro.run()


if __name__ == "__main__":
	main()