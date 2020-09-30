import time

class Producer:
	def produce(self):
		print(f"Producer is working")

	def meet(self):
		print(f"Producer is free")


class Proxy:
	def __init__(self):
		self.occupied = 'No'
		self.producer = None

	def produce(self):
		print(f"Artist checking if producer is free")

		if self.occupied == 'No':
			self.producer = Producer()
			time.sleep(1)

			self.producer.meet()

		else:
			time.sleep(2)
			print(f"Producer is busy!")


p = Proxy()
p.produce()

p.occupied = 'Yes'
p.produce()