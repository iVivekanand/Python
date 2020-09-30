class Stack(object):
	def __init__(self):
		self.stack = []

	def isEmpty(self):
		return self.stack == []

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		data = ''
		if self.stack != []:
			data = self.stack[-1]
			del self.stack[-1]
		return data
			
	def peek(self):
		if self.stack != []:
			return self.stack[-1]
		return

	def clear(self):
		self.stack = []
	
	def __len__(self):
		return len(self.stack)


class Queue(object):
	def __init__(self):
		self.queue = []

	def isEmpty(self):
		return self.queue == []

	def enqueue(self, data):
		self.queue.append(data)

	def dequeue(self):
		data = ''
		if self.queue != []:
			data = self.queue[0]
			self.queue.remove(self.queue[0])
		return data

	def peek(self):
		if self.queue != []:
			return self.queue[0]
		return

	def clear(self):
		self.queue = []

	def __len__(self):
		return len(self.queue)