from linked_list import LinkedListNode

def printLinkedList(linkedList: LinkedListNode):
	result = ""
	while linkedList:
		result += f"{linkedList.data}"
		if linkedList.next:
			result += " -> "
		linkedList = linkedList.next
	print(result)

