import math

from trees import BinarySearchTree
from linked_list import SinglyLinkedList as sll


def construct_bst_from_sorted_array(input, bst):
	input_len = len(input)
	if input_len == 0:
		return

	bst.insert(input[input_len//2])
	construct_bst_from_sorted_array(input[:input_len//2], bst)
	construct_bst_from_sorted_array(input[input_len//2+1:], bst)


def get_children(parent_list=[], children_list=[]):
	current_level = sll()
	next_level_parents = []

	if len(parent_list) == 0:
		return

	if len(children_list) == 0:
		first_level = sll()
		first_level.insertEnd(parent_list[0].data)
		children_list.append(first_level)

	for parent in parent_list:
		if parent.left:
			current_level.insertEnd(parent.left.data)
			next_level_parents.append(parent.left)
		if parent.right:
			current_level.insertEnd(parent.right.data)
			next_level_parents.append(parent.right)
	if len(current_level) > 0:
		children_list.append(current_level)

	get_children(next_level_parents, children_list)

def in_order_successor(bst, data):
	node = bst.node_exists_(bst.root, data)
	if node.parent is None or node.right:
		while node.left is not None:
			node = node.left
		return node
	elif node.parent.left == node:
		return node.parent
	else:
		while(node.parent is not None):
			if node.parent.left == node:
				break
			node = node.parent
		if node.parent is not None:
			return node.parent


def node_exists(tree, node_1, node_2):
	node_1_exists = False
	node_2_exists = False
	count = 0
	if tree == node_1:
		node_1_exists = True
	if tree == node_2:
		node_2_exists = True
	if count == 0 and tree.left:
		count = node_exists(tree.left, node_1, node_2)
		if count == 1:
			node_1_exists = True
		elif count == 2:
			node_2_exists = True
		if count == 0 and tree.right:
			count = node_exists(tree.right, node_1, node_2)
			if count == 1:
				node_1_exists = True
			elif count == 2:
				node_2_exists = True
		
	if node_1_exists and node_2_exists:
		return 3
	elif node_1_exists:
		return 1
	elif node_2_exists:
		return 2
	return count

def common_ancestor(tree, value_1, value_2):
	count = 0

	if tree == value_1 or tree == value_2:
		return tree
	if value_1 == value_2:
		if value_1 == tree.left or value_1 == tree.right:
			return tree

	count = node_exists(tree.left, value_1, value_2)
	if count == 3:
		return common_ancestor(tree.left, value_1, value_2)
	elif count == 1:
		count = node_exists(tree.right, value_1, value_2)
		if count == 2:
			return tree
		else:
			return None
	elif count == 2:
		count = node_exists(tree.left, value_1, value_2)
		if count == 1:
			return tree
		else:
			return None
	
	count = node_exists(tree.right, value_1, value_2)
	if count == 3:
		return common_ancestor(tree.right, value_1, value_2)
	elif count == 1:
		count = node_exists(tree.right, value_1, value_2)
		if count == 2:
			return tree
		else:
			return None
	elif count == 2:
		count = node_exists(tree.left, value_1, value_2)
		if count == 1:
			return tree
		else:
			return None

	return None


def path_sum_of_value(bst, values={}, value_list=[]):
	value_list.append(bst.data)
	values[bst.data] = bst.data
	sum = 0
	for i in range(len(value_list)-1, -1, -1):
		sum += value_list[i]
		if sum in values:
			print(f"{value_list[i:]}")
	if bst.left:
		path_sum_of_value(bst.left, values, value_list)

	if bst.right:
		path_sum_of_value(bst.right, values, value_list)

	value_list.pop()

def search(nums, target) -> bool:
	num_size = len(nums)
	if len(nums) == 0:# or (target < nums[0] and target < nums[num_size-1]):
		return False
	if len(nums) == 1 and nums[0] != target:
		return False
	if nums[0] == target:
		return True
	if search(nums[:len(nums)//2], target) == False:
		return search(nums[len(nums)//2:], target)
	else:
		return True
	
	nums = list(set(nums))
	num_size = len(nums)
	mid = num_size//2

	rotated = 0
	if nums[mid] < nums[0]:
		rotated = 1
	elif nums[num_size-1] < nums[mid]:
		rotated = 2
	
	if num_size == 0 or (num_size == 1 and nums[0] != target):
		return False
	
	if nums[mid] == target or nums[0] == target or nums[num_size-1] == target:
		return True
	elif num_size == 3:
		return False

	if rotated == 1:
		if target > nums[0]:
			return search(nums[:mid], target)
		else:
			return search(nums[mid+1:], target)
	elif rotated == 2:
		if target > nums[mid]:
			return search(nums[:mid], target)
		else:
			return search(nums[mid+1:], target)
	
	if target > nums[0] and target < nums[mid]:
		return search(nums[:mid], target)
	else:
		return search(nums[mid+1:], target)

if __name__ == "__main__":
	search([10,10,10,-10,-10,-10,-10,-9,-9,-9,-9,-9,-9,-9,-8,-8,-8,-8,-8,-8,-8,-8,-7,-7,-7,-7,-6,-6,-6,-5,-5,-5,-4,-4,-4,-4,-3,-3,-2,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,-1,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,2,2,2,3,3,3,4,4,4,5,5,5,5,6,6,6,7,7,7,7,7,8,8,8,8,9,9,9,9,9,9,9,10,10],-6)
	bst = BinarySearchTree()
	input = []
	
	for _ in range(5):
		input.append(_*_)

	construct_bst_from_sorted_array(input, bst)
	print(f"{bst.traverse('bfs')}, Balanced: {bst.is_balanced()}")
	#bst.get_heights()

	bst.clear()
	for _ in [49, 9, 121, 1, 25, 81, 169, 0, 4, 16, 36, 64, 100, 144, 196]:
		bst.insert(_)

	children_list = []
	parent_list = [bst.root]
	get_children(parent_list, children_list)

	bst_height = bst.get_max_height() + 1

	print(f"Levels: {len(children_list)}")


	for child in children_list:
		child_node = child.head
		while child_node:
			print(f"{child_node.data}", end=' ')
			child_node = child_node.next
		print()

	node_1 = in_order_successor(bst, 4)
	node_2 = in_order_successor(bst, 121)

	print(node_1.data, node_2.data)

	ancestor = common_ancestor(bst.root, node_1, node_2)
	print(ancestor.data)

	print(f"In order successor: {in_order_successor(bst, 49).data}")

	path_sum_of_value(bst.root, {}, [])