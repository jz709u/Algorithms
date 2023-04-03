from linked_list import LinkedListNode, LinkedList
from PrintLinkedList import *

# Naiive approach would be iterate over linked list
# create a new node for each node in the list
# Per: O(n) Space: O(n)

# Optimized Approach
# in place 
# Per: O(n) Space: O(1)

def inPlaceReversalOfLinkedList(head: LinkedListNode):
	# case 1 handle when no head exists or it's a single node
	if not head or not head.next:
		return head

	# remaining nodes is everything after the head
	remainingNodes = head.next

	# the tail of the reversed list is the head of the 
	# current list
	reverseList = head
	reverseList.next = None

	# parse till remaining nodes is None
	while remainingNodes:
		# store the remainings node.next 
		# because we will be setting the next
		# to be equal to the reverse list head
		temp = remainingNodes.next

		# set remaining node tail to be the head of the reverse list
		remainingNodes.next = reverseList

		# progress the reversed list so the new head is the one selected
		reverseList = remainingNodes

		# progress the remaining nodes so the tail is pointing at the new tail
		remainingNodes = temp

	# return reverse list
	return reverseList

l = LinkedList("1 2 45 2 51 20 100")
printLinkedList(l.head)
x = reverse(l.head)
printLinkedList(x)