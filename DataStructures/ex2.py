import random
from linked_list import Node
from linked_list import SinglyLinkedList as sll

def removeDuplicates(l1):
		
	print("Original list")
	l1.traverse()

	previousNode = l1.head
	currentNode = previousNode.next

	while currentNode is not None:
		runnerNode = l1.head
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
	l1.traverse()

def getFromLast(l1, n):
	l1.traverse()

	# Without len parameter
	currentNode = l1.head
	nNode = l1.head

	for _ in range(n):
		if nNode is not None:
			nNode = nNode.next
		else:
			return f"List does not have {n} elements"

	while nNode is not None:
		currentNode = currentNode.next
		nNode = nNode.next

	print(f"Element {n} from end is {currentNode.data}")


	# With len parameter exposed
	if n > len(l1):
		return f"List size is {len(l1)}. Cannot get element number {n} from last"

	currentNode = l1.head
	for _ in range(len(l1) - n):
		currentNode = currentNode.next

	print(f"Element {n} from end is {currentNode.data}")

	return ""


def delNode(n):
	if n is None or n.next is None:
		return
	
	n.data = n.next.data
	n.next = n.next.next

def addLinkedList(l1, l2):
	l3 = sll()

	lst1 = l1.head
	lst2 = l2.head

	carry = 0

	while lst1 is not None or lst2 is not None:
		sum_ = carry
		if lst1 is not None:
			sum_ += lst1.data
			lst1 = lst1.next
		if lst2 is not None:
			sum_ += lst2.data
			lst2 = lst2.next

		carry = sum_//10
		sum_ = sum_%10
		l3.insertEnd(sum_)

	if carry > 0:
		l3.insertEnd(carry)

	return l3

def getLoopStart(lst):
	# lst.traverse()
	a = list()
	slowRunner = lst.head
	fastRunner = lst.head
	
	while fastRunner is not None:
		if fastRunner.next is None:
			return
		slowRunner = slowRunner.next
		fastRunner = fastRunner.next.next
		if slowRunner == fastRunner:
			break
	
	if fastRunner is None:
		return

	fastRunner = lst.head
	while(slowRunner != fastRunner):
		slowRunner = slowRunner.next
		fastRunner = fastRunner.next

	return slowRunner

def createLoop(lst):
	loopNode = Node(0)
	currentNode = lst.head
	loopCounter = 0
	loopIndex = random.randint(0,len(lst)-1)
	while loopCounter < loopIndex:
		loopCounter += 1
		currentNode = currentNode.next
	
	loopNode = currentNode

	loopCounter = 0
	currentNode = l1.head
	while loopCounter < listLength - 1:
		loopCounter += 1
		currentNode = currentNode.next
			
	currentNode.next = loopNode
	print(f"Index of loop start: {loopIndex}, data at loop index: {loopNode.data}")

if __name__ == "__main__":
	l1 = sll()
	l2 = sll()

	listLength = 9

	for _ in range(listLength): l1.insertEnd(random.randint(0, 9))
	for _ in range(listLength): l2.insertEnd(random.randint(0, 9))

	print(getFromLast(l1, 9))

	l1.traverse(), l2.traverse()

	addLinkedList(l1, l2).traverse()
	
	createLoop(l1)
	loopStart = getLoopStart(l1)
	
	print(loopStart.data, loopStart.next.data)