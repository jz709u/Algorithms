
class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None
        self.tail = None

    # insert_node_at_head method will insert a LinkedListNode at head
    # of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node

    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAthead method.
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)

    # returns the number of nodes in the linked list
    def get_length(self, head):
        temp = head
        length = 0
        while(temp):
            length+=1
            temp = temp.next
        return length

    # returns the node at the specified position(index) of the linked list
    def get_node(self, head, pos):
        if pos != -1:
            p = 0
            ptr = head
            while p < pos:
                ptr = ptr.next
                p += 1
            return ptr

    def add_cycle(self, pos):
    	node = self.get_node(self.head, pos)
    	self.tail.next = node

    
    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp != self.tail:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "

        result += ""
        if self.tail.next != None:
        	result += f"cycle exists to {self.tail.next.data}"
        return result

class LinkedListNode:
	def __init__(self, data, next = None):
		self.data = data
		self.next = next

def linkListCycle(head):
	slow = head
	fast = head

	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

		if fast == None:
			break

		if slow == fast:
			return True

	return False

linkedList = LinkedList()
linkedList.create_linked_list([1,2,5,123,200,5])
linkedList.add_cycle(2)
print(linkedList) 
print(linkListCycle(linkedList.head))


