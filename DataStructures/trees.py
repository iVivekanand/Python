class TreeNode(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.parent = None

class BinarySearchTree(object):
	def __init__(self):
		self.root = None
		self.__count = 0
		self.__max_height = 0
		self.__min_height = 0

	def __len__(self):
		return self.__count

	def insert(self, data):
		new_node = TreeNode(data)
		height_count = 0
		if self.root is None:
			self.root = new_node
		else:
			height_count += 1
			height_count = self.insert_node(data, self.root, height_count)
		if height_count > self.__max_height:
			self.__max_height = height_count
		self.__count += 1

	def insert_node(self, data, current_node, height_count):
		new_node = TreeNode(data)
		new_node.parent = current_node
		if data <= current_node.data:
			if current_node.left is None:
				current_node.left = new_node
			else:
				height_count += 1
				height_count = self.insert_node(data, current_node.left, height_count)
		else:
			if current_node.right is None:
				current_node.right = new_node
			else:
				height_count += 1
				height_count = self.insert_node(data, current_node.right, height_count)
		return height_count

	def node_exists_(self, node, data):
		if node:
			if data == node.data:
				return node
			if data < node.data:
				return self.node_exists_(node.left, data)
			elif data > node.data:
				return self.node_exists_(node.right, data)
		return None

	def node_exists(self, data):
		return self.node_exists_(self.root, data) != None

	def traverse_in_order(self, node):
		output = []
		if node.left:
			result = self.traverse_in_order(node.left)
			output.extend(result) if type(result) is list else output.append(result)
		output.append(node.data)
		if node.right:
			result = self.traverse_in_order(node.right)
			output.extend(result) if type(result) is list else output.append(result)
		return output

	def traverse_pre_order(self, node):
		output = []
		output.append(node.data)
		if node.left:
			result = self.traverse_pre_order(node.left)
			output.extend(result) if type(result) is list else output.append(result)
		if node.right:
			result = self.traverse_pre_order(node.right)
			output.extend(result) if type(result) is list else output.append(result)
		return output

	def traverse_post_order(self, node):
		output = []
		if node.left:
			result = self.traverse_post_order(node.left)
			output.extend(result) if type(result) is list else output.append(result)
		if node.right:
			result = self.traverse_post_order(node.right)
			output.extend(result) if type(result) is list else output.append(result)
		output.append(node.data)
		return output

	def traverse(self, type='inorder'):
		output = []
		if self.root is not None:
			if type == 'bfs':
				parents = [self.root]
				while len(parents) > 0:
					if parents[0].left is not None:
						parents.append(parents[0].left)
					if parents[0].right is not None:
						parents.append(parents[0].right)
					output.append(parents[0].data)
					parents.pop(0)

			elif type == 'inorder':
				output.extend(self.traverse_in_order(self.root))

			elif type == 'preorder':
				output.extend(self.traverse_pre_order(self.root))

			elif type == 'postorder':
				output.extend(self.traverse_post_order(self.root))

			else:
				return f"Invalid traversal type {type}. Available options: ['bfs', 'inorder', 'preorder', 'postorder']"
		return output

	def leaf_heights_(self, node, height_from_root):
		if node is None:
			return 0
		output = []
		if node.left is None and node.right is None:
			return [height_from_root]
		height_from_root += 1
		if node.left is not None:
			result = self.leaf_heights_(node.left, height_from_root)
			output.extend(result) if type(result) is list else output.append(result)
		if node.right is not None:
			result = self.leaf_heights_(node.right, height_from_root)
			output.extend(result) if type(result) is list else output.append(result)
		return output

	def check_balanced(self, node, height_from_root):
		if node is None:
			return True

		height_from_root += 1
		if node.left is None and node.right is None:
			if self.__max_height < height_from_root:
				self.__max_height = height_from_root
			if self.__min_height > height_from_root:
				self.__min_height = height_from_root
			if abs(self.__max_height - self.__min_height) > 1:
				return False
		
		if node.left is not None:
			if not self.check_balanced(node.left, height_from_root):
				return False
		if node.right is not None:
			if not self.check_balanced(node.right, height_from_root):
				return False
		return True

	def is_balanced(self):
		self.__min_height = float('inf')
		self.__max_height = 0
		return self.check_balanced(self.root, 0)

	def get_heights(self):
		print(f"Max: {self.__max_height}, Min: {self.__min_height}")

	def get_max_height(self):
		return self.__max_height

	def get_min_height(self):
		return self.__min_height

	def clear(self):
		self.root = None
		self.__count = 0
		self.__max_height = 0

class Graph(object):
	def __init__(self, connections, directed=False):
		self.__graph = dict()
		self.__directed = directed
		self.add_connections(connections)

	def add_connections(self, connections):
		for node1, node2 in connections:
			self.add(node1, node2)

	def add(self, node1, node2):
		if node1 not in self.__graph:
			self.__graph[node1] = set()
		self.__graph[node1].add(node2)
		if not self.__directed:
			if node2 not in self.__graph:
				self.__graph[node2] = set()
			self.__graph[node2].add(node1)

	def remove(self, node):
		if node in self.__graph:
			del self.__graph[node]
			for n, connections in self.__graph.items():
				print(n)
				if node in connections:
					connections.remove(node)

	def is_connected(self, node1, node2):
		return node1 in self.__graph and node2 in self.__graph[node1]

	def find_path(self, node1, node2, path=[]):
		path += [node1]
		if node1 == node2:
			return path
		if node1 not in self.__graph:
			return []
		for node in self.__graph[node1]:
			if node not in path:
				new_path = self.find_path(node, node2, path)
				if new_path:
					return new_path
		return None

	def get_vertices(self):
		vertices = []
		for key in self.__graph.keys():
			vertices.append(key)
		return vertices

	def __str__(self):
		return f"{self.__class__.__name__}, {dict(self.__graph)}"

	def dft(self, node, visited_nodes=dict()):
		if not node:
			return list(visited_nodes.keys())
		visited_nodes[node] = True
		for neighbor in self.__graph[node]:
			if neighbor in visited_nodes:
				continue
			self.dft(neighbor, visited_nodes)
		return list(visited_nodes.keys())

	def bft(self, node, visited_nodes=dict(), visited_nodes_queue=[]):
		if node is None:
			return list(visited_nodes.keys())
		if node not in visited_nodes:
			visited_nodes[node] = True
			visited_nodes_queue.append(node)
		if not visited_nodes_queue:
			return visited_nodes
		visited_nodes_queue.pop(0)
		for neighbor in self.__graph[node]:
			if neighbor not in visited_nodes:
				visited_nodes[neighbor] = True
				visited_nodes_queue.append(neighbor)
		if visited_nodes_queue:
			self.bft(visited_nodes_queue[0], visited_nodes, visited_nodes_queue)
		return list(visited_nodes.keys())


if __name__ == "__main__":
	connections = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')]
	graph = Graph(connections)
	
	print(f"Vertices: {graph.dft(graph.get_vertices()[0], {})}")
	print(f"Vertices: {graph.bft(graph.get_vertices()[0], {}, [])}")