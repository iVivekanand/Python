class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None

	def get_data(self):
		return self.val

	def set_data(self, val):
		self.val = val

	def get_next(self):
		return self.next

	def set_next(self, next):
		self.next = next


class LinkedList(object):
	def __init__(self, head=None):
		self.head = head
		self.count = 0

	def get_count(self):
		return self.count

	def insert(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node
		self.count += 1

	def find(self, val):
		item = self.head
		while (item != None):
			if item.get_data() == val:
				return item
			else:
				item = item.get_next()
		return None

	def deleteAt(self, idx):
		if idx > self.count-1:
			return
		if idx == 0:
			self.head = self.head.get_next()
		else:
			tempIdx = 0
			node = self.head
			while tempIdx < idx - 1:
				node = node.get_next()
				tempIdx += 1
			node.set_next(node.get_next().get_next())
			self.count -= 1

	def dump_list(self):
		tempnode = self.head
		while (tempnode != None):
			print(f"Node: {tempnode.get_data()}")
			tempnode = tempnode.next


itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)
itemlist.dump_list()

print(f"Item count: {itemlist.get_count()}")
print(f"Finding item: {itemlist.find(13)}")
print(f"Finding item: {itemlist.find(78)}")

itemlist.deleteAt(3)
print(f"Item count: {itemlist.get_count()}")
print(f"Finding item: {itemlist.find(38)}")
itemlist.dump_list()

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print(f"{stack}")
print(f"{stack.pop()}")
print(f"{stack}")

from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print(f"{queue}")
print(f"{queue.popleft()}")
print(f"{queue}")

ht = dict({"key1": 1, "key 2": 2, "key 3": "three"})
print(ht)
ht2 = {}
ht2['key1'] = 1
ht2['key2'] = 2
ht2['key3'] = 3
print(ht2)

for key, value in ht.items():
	print(f"Key: {key}, Value: {value}")

import time

def countdown(x = 10):
	if x == 0:
		print("Done")
		return
	else:
		print(f"{x} ...")
		#time.sleep(1)
		countdown(x-1)

countdown(5)

def power(num=1, pwr=0):
	if pwr == 0:
		return 1
	else:
		return num * power(num, pwr-1)

def factorial(num=1):
	if num == 0:
		return 1
	else:
		return num * factorial(num -1)

print(power(5, 3))
print(power(1, 5))
print(factorial(4))
print(factorial())

def bubbleSort(data):
	for i in range(len(data) - 1, 0, -1):
		for j in range(i):
			if data[j] > data[j+1]:
				temp = data[j]
				data[j] = data[j+1]
				data[j+1] = temp
			print(f"Current state: {data}")

data = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
bubbleSort(data)

def mergeSort(data):
	if len(data) > 1:
		mid = len(data) // 2
		left = data[:mid]
		right = data[mid:]

		mergeSort(left)
		mergeSort(right)

		i = 0
		j = 0
		k = 0
		
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				data[k] = left[i]
				i += 1
			else:
				data[k] = right[j]
				j += 1
			k += 1
		while i < len(left):
			data[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			data[k] = right[j]
			j += 1
			k += 1
data = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print(data)
mergeSort(data)	
print(data)

def quickSort(data, first, last):
	if first < last:
		pivotIdx = partition(data, first, last)
		quickSort(data, first, pivotIdx-1)
		quickSort(data, pivotIdx+1, last)

def partition(data, first, last):
	pivot = data[first]
	lower = first + 1
	upper = last
	done = False
	while not done:
		while lower <= upper and data[lower] <= pivot:
			lower += 1
		while data[upper] >= pivot and upper >= lower:
			upper -=1

		if upper < lower:
			done = True
		else:
			temp = data[lower]
			data[lower] = data[upper]
			data[upper] = temp

	temp = data[first]
	data[first] = data[upper]
	data[upper] = temp

	return upper

data = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print(data)
quickSort(data, 0, len(data)-1)	
print(data)