import random
# from linked_list import Node
from linked_list import SinglyLinkedList as sll
from linked_list import Stack
from linked_list import Queue

class ArrayStackFixed(object):
	def __init__(self, size, stackCount):
		self.MAX_SIZE = size
		self.data = [-1 for _ in range(self.MAX_SIZE)]
		self.stackCount = stackCount
		self.stackTop = [0]
		for i in range(self.stackCount - 1):
			self.stackTop.append(self.MAX_SIZE//self.stackCount+self.stackTop[i])
		self.stackLimit = [_ for _ in self.stackTop]
		self.stackLimit.append(self.MAX_SIZE)

	def getStackCount(self):
		return self.stackCount

	def getStackLimits(self):
		return self.stackLimit

	def getStackTops(self):
		return self.stackTop

	def isEmpty(self, s):
		if s < self.stackCount:
			return self.stackTop[s] == self.stackLimit[s]
		else:
			return f"Max stack count is {self.stackCount-1}"

	def isFull(self, s):
		if s < self.stackCount:
			return self.stackTop[s] == self.stackLimit[s+1]
		else:
			return f"Max stack count is {self.stackCount-1}"

	def getStackSize(self, s):
		if s < self.stackCount:
			return self.stackLimit[s+1] - self.stackLimit[s]
		else:
			return f"Max stack count is {self.stackCount-1}"

	def getTop(self, s):
		if s < self.stackCount:
			return self.stackTop[s]
		else:
			return f"Max stack count is {self.stackCount-1}"

	def push(self, s, data):
		if s < self.stackCount:
			if self.stackTop[s] < self.stackLimit[s+1]:
				self.data[self.stackTop[s]] = data
				self.stackTop[s] += 1
			else:
				return f"Stack {s} is already full"
		else:
			return f"Max stack count is {self.stackCount-1}"

	def pop(self, s):
		if s < self.stackCount:
			if self.stackTop[s] > self.stackLimit[s]:
				data = self.data[self.stackTop[s]-1]
				self.data[self.stackTop[s]-1] = -1
				self.stackTop[s] -= 1
				return data
			else:
				return f"Stack {s} is empty"
		else:
			return f"Max stack count is {self.stackCount-1}"

	def peek(self, s):
		if s < self.stackCount:
			if self.stackTop[s] > self.stackLimit[s]:
				return self.data[self.stackTop[s]-1]
			else:
				return f"Stack {s} is empty"
		else:
			return f"Max stack count is {self.stackCount-1}"

	def clear(self, s):
		if s < self.stackCount:
			if self.stackTop[s] > self.stackLimit[s]:
				for i in range(self.stackLimit[s], self.stackTop[s]):
					self.data[i] = -1
				self.stackTop[s] = self.stackLimit[s]
		else:
			return f"Max stack count is {self.stackCount-1}"

	def clearAll(self):
		for i in range(self.MAX_SIZE):
			self.data[i] = -1
		for i in range(len(self.stackTop)):
			self.stackTop[i] = self.stackLimit[i]

class Node(object):
	def __init__(self, data, previous):
		self.data = data
		self.previous = previous

class ArrayStack(object):
	def __init__(self, size, stackCount):
		self.size = size
		self.stackCount = stackCount
		self.stack = [None for _ in range(size)]
		self.stackTop = [None for _ in range(stackCount)]
		self.usedCount = 0
		self.freeIndex = {_ for _ in range(size)}

	def push(self, s, data):
		if s < self.stackCount:
			if self.usedCount < self.size:
				previous = None
				if self.stackTop[s] is not None:
					previous = self.stack[self.stackTop[s]]
				self.stackTop[s] = self.freeIndex.pop()
				self.stack[self.stackTop[s]] = Node(data, previous)
				self.usedCount += 1
			else:
				return f"Buffer already full"
		else:
			return f"Max zero-indexed stack count is {self.stackCount}"

	def pop(self, s):
		if s < self.stackCount and self.stackTop[s] is not None:
			if self.usedCount > 0:
				data = self.stack[self.stackTop[s]].data
				previous = self.stack[self.stackTop[s]].previous
				self.freeIndex.add(self.stackTop[s])
				self.stack[self.stackTop[s]] = None
				if previous is not None:
					self.stackTop[s] = self.stack.index(previous)
				else:
					self.stackTop[s] = None
				self.usedCount -= 1
				return data
			else:
				return f"Buffer is empty"
		elif self.stackTop[s] is None:
			return f"{s} is an empty stack"
		else:
			return f"Max zero-indexed stack count is {self.stackCount}"

	def peek(self, s):
		if s < self.stackCount and self.stackTop[s] is not None:
			if self.usedCount > 0:
				return self.stack[self.stackTop[s]].data
			else:
				return f"Buffer is empty"
		elif self.stackTop[s] is None:
			return f"{s} is an empty stack"
		else:
			return f"Max zero-indexed stack count is {self.stackCount}"

	def isEmpty(self):
		return self.usedCount == 0

	def isFull(self):
		return self.usedCount == self.size
	

def towerOfHanoi(discCount=2):
	a = Stack()
	b = Stack()
	c = Stack()

	for i in range(discCount, 0, -1):
		a.push(i)

	print("Tower A at start")
	for i in range(1, discCount+1):
		print(i)

	minMoves = 2**discCount - 1
	for i in range(minMoves):
		if i%3 == 0:
			if c.length > 0 and a.length > 0:
				if a.peek() < c.peek():
					c.push(a.pop())
				else:
					a.push(c.pop())
			elif c.length > 0:
				a.push(c.pop())
			elif a.length > 0:
				c.push(a.pop())
		elif i%3 == 1:
			if a.length > 0 and b.length > 0:
				if a.peek() < b.peek():
					b.push(a.pop())
				else:
					a.push(b.pop())
			elif a.length > 0:
				b.push(a.pop())
			elif b.length > 0:
				a.push(b.pop())
		elif i%3 == 2:
			if b.length > 0 and c.length > 0:
				if b.peek() < c.peek():
					c.push(b.pop())
				else:
					b.push(c.pop())
			elif b.length > 0:
				c.push(b.pop())
			elif c.length > 0:
				b.push(c.pop())

	if discCount%2 == 0:
		b, c = c, b

	if a.length > 0:
		print("Tower A at end")
		while a.length > 0:
			print(a.pop())

	if b.length > 0:
		print("Tower B at end")
		while b.length > 0:
			print(b.pop())

	if c.length > 0:
		print("Tower C at end")
		while c.length > 0:
			print(c.pop())
	return

class TowerOfHanoi(object):
	def __init__(self, discCount=3):
		self.discs = discCount
		self.tower = [Stack(), Stack(), Stack()]
		for i in range(self.discs, 0, -1):
			self.tower[0].push(i)

	def move(self, start, end):
		if self.tower[start].length > 0 and self.tower[end].length > 0:
			if self.tower[start].peek() > self.tower[end].peek():
				#print(f"Cannot move larger size disc on top of smaller size disc")
				return False
			else:
				self.tower[end].push(self.tower[start].pop())
				return True
		elif self.tower[start].length > 0:
			self.tower[end].push(self.tower[start].pop())
			return True
		return False
			

	def printTower(self, towerId):
		tempStack = Stack()
		while self.tower[towerId].length > 0:
			topNode = self.tower[towerId].pop()
			print(f"{topNode}")
			tempStack.push(topNode)
		while tempStack.length > 0:
			self.tower[towerId].push(tempStack.pop())

	def solve(self):
		minMoves = 2**self.discs - 1
		source = 0
		destination = 2
		buffer = 1

		if self.discs//2 == 0:
			buffer, destination = destination, buffer

		for i in range(minMoves):
			if i%3 == 0:
				if not self.move(source, destination):
					self.move(destination, source)
			elif i%3 == 1:
				if not self.move(source, buffer):
					self.move(buffer, source)
			else:
				if not self.move(destination, buffer):
					self.move(buffer, destination)

		self.printTower(destination)
		return

class MyQueue(object):
	def __init__(self):
		self.s1 = Stack()
		self.s2 = Stack()

	def enqueue(self, data):
		self.s1.push(data)

	def dequeue(self):
		if self.s2.length > 0:
			return self.s2.pop()
		while self.s1.length > 0:
			self.s2.push(self.s1.pop())
		return self.s2.pop()

	def peek(self):
		if self.s2.peek() is None:
			while self.s1.length > 0:
				self.s2.push(self.s1.pop())
		return self.s2.peek()

	def getLength(self):
		return self.s1.length + self.s2.length


def sortStack(stackSize=10):
	s = Stack()

	print("Before sort")
	for _ in range(stackSize):
		data = random.randint(1, stackSize*10)
		print(data, end = ', ')
		s.push(data)

	r = Stack()
	while not s.isEmpty():
		data = s.pop()
		while(not r.isEmpty() and data > r.peek()):
			s.push(r.pop())
		r.push(data)

	print("\nPost sort")
	while not r.isEmpty():
		print(r.pop(), end=', ')

if __name__ == "__main__":
	sortStack(3)
	s = ArrayStack(10, 4)
	s.push(1, 1)
	t = TowerOfHanoi(3)
	t.solve()