import random

class Node(object):
	def __init__(self, data):
		self.next = None
		self.data = data

class SinglyLinkedList(object):
	def __init__(self):
		self.head = None
		self.length = 0

	def __len__(self):
		return self.length

	def insertStart(self, data):
		newNode = Node(data)
		if not self.head:
			self.head = newNode
		else:
			newNode.next = self.head
			self.head = newNode
		self.length += 1

	def insertEnd(self, data):
		newNode = Node(data)
		if not self.head:
			self.head = newNode
			self.length += 1
			return

		currentNode = self.head
		while currentNode.next is not None:
			currentNode = currentNode.next
		currentNode.next = newNode
		self.length += 1

	def insertAt(self, index, data):
		if index > self.length:
			print(f"List length is {self.length}. Can't insert at index {index}")
			return -1

		newNode = Node(data)
		currentNode = self.head

		if index == 0:
			self.head = newNode
			newNode.next = currentNode
			self.length += 1
			return

		indexCounter = 1
		while currentNode is not None:
			if indexCounter == index:
				newNode.next = currentNode.next
				currentNode.next = newNode
				self.length += 1
				return
			currentNode = currentNode.next
			indexCounter += 1

	def deleteAt(self, index):
		if index > self.length - 1:
			print(f"List length is {self.length}. Can't delete element at index {index}")

		indexCounter = 0
		currentNode = self.head
		previousNode = None

		while currentNode is not None:
			if indexCounter == index:
				if previousNode is not None:
					previousNode.next = currentNode.next
				else:
					self.head = currentNode.next
				self.length -= 1
				return
			previousNode = currentNode
			currentNode = currentNode.next
			indexCounter += 1

	def deleteNode(self, data, firstOnly=False):
		if self.head is None:
			print(f"Empty list. {data} cannot be removed")
			return -1

		currentNode = self.head
		previousNode = None

		startLength = self.length

		while currentNode is not None:
			if currentNode.data == data:
				if previousNode is not None:
					previousNode.next = currentNode.next
				else:
					self.head = currentNode.next
				if firstOnly:
					break
				currentNode = currentNode.next
				self.length -= 1
			else:
				previousNode = currentNode
				currentNode = currentNode.next

		if startLength == self.length:
			print(f"{data} not present in list")

	def traverse(self):
		if self.head is None:
			return

		currentNode = self.head
		counter = 1
		while currentNode is not None:
			print(f"Element {counter}: {currentNode.data}")
			currentNode = currentNode.next
			counter += 1

	def clear(self):
		self.head = None
		self.length = 0

	def makeUnique(self):			
		print("Original list")
		self.traverse()

		duplicates = dict()
		currentNode = self.head
		previousNode = None

		while currentNode is not None:
			if currentNode.data not in duplicates:
				duplicates[currentNode.data] = currentNode.data
				previousNode = currentNode
			else:
				self.length -= 1
				previousNode.next = currentNode.next
			currentNode = currentNode.next
	
		print("List with duplicates removed")
		self.traverse()

	def removeDuplicates(self):			
		print("Original list")
		self.traverse()
	
		previousNode = self.head
		currentNode = previousNode.next
	
		while currentNode is not None:
			runnerNode = self.head
			currentMoved = False
			while runnerNode != currentNode and currentNode is not None:
				if runnerNode.data == currentNode.data:
					previousNode.next = currentNode.next
					currentNode = currentNode.next
					currentMoved = True
					continue
				runnerNode = runnerNode.next
	
			if currentNode is not None and not currentMoved:
				previousNode = currentNode
				currentNode = currentNode.next
	
		print("List with duplicates removed")
		self.traverse()

class MinStack(object):
	def __init__(self):
		self.top = None
		self.length = 0

	def push(self, data):
		newNode = Node(data)
		if self.top is not None:
			if data <= self.top.data:
				currentNode = self.top
				self.top = newNode
				self.top.next = currentNode
			else:
				return
		else:
			self.top = newNode
		self.length += 1

	def pop(self, data):
		if self.top is not None and data == self.top.data:
			self.top = self.top.next
			self.length -= 1

class Stack(object):
	def __init__(self):
		self.top = None
		self.length = 0
		self.minStack = MinStack()

	def isEmpty(self):
		return self.length == 0

	def push(self, data):
		newNode = Node(data)
		if self.top is not None:
			currentNode = self.top
			self.top = newNode
			self.top.next = currentNode
		else:
			self.top = newNode
		self.length += 1
		self.minStack.push(data)

	def pop(self):
		if self.top is not None:
			data = self.top.data
			self.top = self.top.next
			self.length -= 1
			self.minStack.pop(data)
			return data
		else:
			return

	def peek(self):
		if self.top is not None:
			return self.top.data
		else:
			return

	def clear(self):
		self.top = None

	def __len__(self):
		return self.length

	def getMin(self):
		if self.length > 0:
			return self.minStack.top.data
		else:
			return f"Stack is empty"

class SetOfStacks(object):
	def __init__(self, threshold):
		self.length = 0
		self.stack = [Stack()]
		self.maxSize = threshold
		self.subStackCount = 1

	def push(self, data):
		newNode = Node(data)
		stackIndex = 0
		if self.length > 0:
			stackIndex = self.length//self.maxSize

			if (self.length) % self.maxSize == 0 and stackIndex > 0:
				self.stack.append(Stack())
				newNode.next = self.stack[stackIndex-1].top
				self.subStackCount += 1
			else:
				newNode.next = self.stack[stackIndex].top

		self.stack[stackIndex].push(data)
		self.length += 1

	def pop(self):
		stackIndex = 0
		if self.length > 0:
			stackIndex = (self.length-1)//self.maxSize
		if self.stack[stackIndex].top is not None:
			data = self.stack[stackIndex].top.data
			self.stack[stackIndex].pop()
			if stackIndex > 0 and self.stack[stackIndex].top is None:
				del(self.stack[stackIndex])
				self.subStackCount -= 1
			self.length -= 1
			return data
		else:
			return f"Stack is empty"

	def getSubStackCount(self):
		return self.subStackCount

	def popAt(self, stackIndex):
		if stackIndex == self.subStackCount - 1:
			self.pop()
			return
		if stackIndex > self.subStackCount - 1:
			return f"Max sub-stack size is {self.subStackCount}"

		tempStack = Stack()
		while self.length != (stackIndex+1) * self.maxSize:
			tempStack.push(self.pop())

		data = self.stack[stackIndex].pop()
		self.length -= 1
		while tempStack.length > 0:
			self.push(tempStack.pop())
		return data

	def traverse(self):
		tempStack = Stack()
		while self.length > 0:
			data = self.pop()
			print(data)
			tempStack.push(data)
		while tempStack.length > 0:
			self.push(tempStack.pop())

	def peek(self):
		if self.length == 0:
			return f"Set of Stacks is empty"
		else:
			return self.stack[self.subStackCount-1].top.data

	def peekAt(self, stackIndex):
		if stackIndex == self.subStackCount - 1:
			return self.peek()
		if stackIndex > self.subStackCount - 1:
			return f"Max sub-stack size is {self.subStackCount}"

		return self.stack[stackIndex].top.data

	def peekSubStacks(self):
		if self.length == 0:
			return f"Stack is empty"
		return {subStackIndex: self.stack[subStackIndex].top.data for subStackIndex in range(0, self.subStackCount)}
		

class Queue(object):
	def __init__(self):
		self.first = None
		self.length = 0
		self.last = None

	def isEmpty(self):
		return self.length == 0

	def enqueue(self, data):
		newNode = Node(data)
		if self.last is not None:
			self.last.next = newNode
			self.last = newNode
		else:
			self.first = newNode
			self.last = newNode
		self.length += 1

	def dequeue(self):
		data = None
		if self.first is not None and self.first != self.last:
			data = self.first.data
			self.first = self.first.next
			self.length -= 1
		elif self.first is not None:
			data = self.first.data
			self.first = None
			self.last = None
			self.length -= 1

		return data

	def peek(self):
		if self.first is not None:
			return self.first.data
		return

	def clear(self):
		self.first = None
		self.last = None
		self.length = 0

	def __len__(self):
		return self.length