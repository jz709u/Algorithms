
from __future__ import annotations

class LinkedListNode:
	def __init__(self, data: int, next: LinkedListNode = None):
		self.next = next
		self.data = data

class LinkedList:
	def __init__(self, data: str):
		result = data.split()
		currentHead = None
		for x in result:
			asInt = int(x)
			if asInt:
				if currentHead:
					currentHead.next = LinkedListNode(asInt)
					currentHead = currentHead.next
				else:
					currentHead = LinkedListNode(asInt)
					self.head = currentHead
		self.tail = currentHead
