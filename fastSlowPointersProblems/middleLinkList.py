from linked_list import LinkedList

def get_middle_node(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    return slow