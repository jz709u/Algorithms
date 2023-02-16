from linked_list import LinkedList
from linked_list_reverse import reverse_linked_list
from print_list import print_list_with_forward_arrow

def reverse_link_list(head):

    # Next <- Next <- Head 
    # Next <- Mid <- Head 
    # Next <- Mid  Head -> newTail(None)
    # Next <- Head NewTail -> None

    temp = None
    while head is not None:
        mid = head.next
        head.next = temp
        temp = head
        head = mid
    return temp

def palindrome(head):

    left = head
    right = head
    while right != None and right.next != None:
        left = left.next
        right = right.next.next

    
    reversedRight = None
    #even
    # reverse from the left [1, 2, left, left.next, 5, 6]
    if right is None:
        reversedRight = reverse_link_list(left)
    # odd right.next is None
    # reverse from center [1,2,left, left.next, 3]
    else:
        reversedRight = reverse_link_list(left.next)
    
    left = head
    right = reversedRight
    
    # comparing from the right only as the size of the array
    # will be different if it's 
    while right is not None:
        if right.data != left.data:
            return False
        left = left.next
        right = right.next
    return True

