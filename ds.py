# class Node(object):
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.size = 0

	def remove(self, data):
		if self.head is None:
			return

		current = self.head
		previous = None

		while current is not None:
			if current.data != data:
				previous = current
				current = current.next
			elif current.data == data:
				if previous is None:
					self.head = current.next
				else:
					previous.next = current.next
				current = current.next
				self.size -= 1

	def insertStart(self, data):
		newNode = Node(data)
		if not self.head:
			self.head = newNode
		else:
			newNode.next = self.head
			self.head = newNode
		self.size += 1

	def insertEnd(self, data):
		newNode = Node(data)
		if self.head is None:
			self.head = newNode
			self.size += 1
			return
		actualNode = self.head
		while actualNode.next is not None:
			actualNode = actualNode.next
		actualNode.next = newNode
		self.size += 1

	def traverse(self):
		actualNode = self.head
		counter = 1
		while actualNode is not None:
			print(f"Element {counter}: {actualNode.data}")
			actualNode = actualNode.next
			counter += 1

class DoubleNode(object):
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class Stack:
	def __init__(self):
		self.stack = []

	def isEmpty(self):
		return self.stack == []

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		data = self.stack[-1]
		del self.stack[-1]
		return data

	def peek(self):
		data = self.stack[-1]
		return data

	def sizeStack(self):
		return len(self.stack)

class Queue:
	def __init__(self):
		self.queue = []

	def isEmpty(self):
		return self.queue == []

	def enqueue(self, data):
		self.queue.insert(0, data)

	def dequeue(self):
		data = self.queue[-1]
		del self.queue[-1]
		return data

	def peek(self):
		return self.queue[-1]

	def sizeQueue(self):
		return len(self.queue)

class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BinarySearchTree(object):
	def __init__(self):
		self.root = None

	def insert(self, data):
		if not self.root:
			self.root = Node(data)
		else:
			self.insertNode(data, self.root)

	def insertNode(self, data, node):
		if data < node.data:
			if node.left:
				self.insertNode(data, node.left)
			else:
				node.left = Node(data)
		else:
			if node.right:
				self.insertNode(data, node.right)
			else:
				node.right = Node(data)


	def getMin(self):
		if self.root:
			return self.getMinValue(self.root)

	def getMinValue(self, node):
		if node.left:
			return self.getMin()
		return node.data

	def getMax(self):
		if self.root:
			return self.getMaxValue(self.root)

	def getMaxValue(self, node):
		if node.right:
			return self.getMax()
		return node.data

	def traverseInOrder(self, node):
		if node.left:
			self.traverseInOrder(node.left)
		print(f"{node.data}")
		if node.right:
			self.traverseInOrder(node.right)
		#return node.data

	def traversePreOrder(self, node):
		print(f"{node.data}")
		if node.left:
			self.traversePreOrder(node.left)
		if node.right:
			self.traversePreOrder(node.right)

	def traversePostOrder(self, node):
		if node.left:
			self.traversePostOrder(node.left)
		if node.right:
			self.traversePostOrder(node.right)
		print(f"{node.data}")

	def traverse(self, order='in'):
		if self.root:
			if order == 'in':
				self.traverseInOrder(self.root)
			elif order == 'pre':
				self.traversePreOrder(self.root)
			elif order == 'post':
				self.traversePostOrder(self.root)

	def removeNode(self, data, node):
		if not node:
			return node
		if data < node.data:
			node.left = self.removeNode(data, node.left)
		elif data > node.data:
			node.right = self.removeNode(data, node.right)
		else:
			if not node.left and not node.right:
				print(f"Removing a leaf node")
				del node
				return None
			if not node.left:
				print(f"Removing node with single right child")
				tempNode = node.right
				del node
				return tempNode
			elif not node.right:
				print(f"Removing node with single left child")
				tempNode = node.left
				del node
				return tempNode

			print(f"Removing node with two children")
			tempNode = self.getPredecessor(node.left)
			node.data = tempNode.data
			node.left = self.removeNode(tempNode.data, node.left)

		return node

	def getPredecessor(self, node):
		if node.right:
			return self.getPredecessor(node.right)
		return node

	def remove(self, data):
		if self.root:
			self.root = self.removeNode(data, self.root)
