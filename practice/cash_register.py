class CashRegister(object):
	def __init__(self):
		self.register = {25: 100, 10: 100, 5: 100, 1: 100}
		self.total = 0
		for denomination, count in self.register.items():
			self.total += denomination*count

	def getTotal(self):
		return self.total

	def getDenominations(self):
		return self.register

	def updateTotal(self):
		self.total = 0
		for denomination, count in self.register.items():
			self.total += denomination*count

	def reset(self):
		self.__init__()

	def fillRegister(self, refill={}):
		for denomination, count in refill.items():
			self.register[denomination] += count
		self.updateTotal()

	def tenderChange(self, amount):
		print(f"Requested change amount: {amount}")

		if amount > self.getTotal():
			return f"Sorry! Insufficient change available in cash register"

		coinCount = 0
		change = {}
			
		for denomination, count in self.register.items():
			currentCount = amount//denomination
			if currentCount <= count and currentCount > 0:
				coinCount += currentCount
				change[denomination] = currentCount
				self.register[denomination] -= currentCount
				amount -= denomination*currentCount
				if amount == 0: # Done with getting change, break out now
					break

		self.updateTotal()
		
		if amount > 0:
			print(f"Cash register does not have change for {amount} cents")
			print(f"Available denominations: {self.getDenominations()}")
			print(f"Tendering next highest amount")
			for denomination, count in sorted(self.register.items()):
				if count > 0:
					coinCount += 1
					amount -= denomination
					if denomination in change:
						change[denomination] += 1
					else:
						change[denomination] = 1
					break
			self.register[denomination] -= 1
			print(f"Balance to be returned to cash register: {abs(amount)}")

		print(f"Total coins: {coinCount}")
		print(f"Coin types: {change}")

	def tenderChange(self, amount, denominations=[]):
		print(f"Requested change amount: {amount}")

		coinCount = 0
		change = {}
			
		for denomination in sorted(denominations, reverse=True):
			currentCount = amount//denomination
			if currentCount == 0:
				continue
			coinCount += currentCount
			change[denomination] = currentCount
			amount -= denomination*currentCount
			if amount == 0: # Done with getting change, break out now
				break
		
		if amount > 0:
			print(f"Cash register does not have change for {amount} cents")
			print(f"Tendering next highest amount")
			for denomination in sorted(denominations):
				coinCount += 1
				amount -= denomination
				if denomination in change:
					change[denomination] += 1
				else:
					change[denomination] = 1
				break
			print(f"Balance to be returned to cash register: {abs(amount)}")

		print(f"Total coins: {coinCount}")
		print(f"Coin types: {change}")

if __name__ == "__main__":
	cr = CashRegister()
	cr.tenderChange(31)
	cr.tenderChange(123)
