# finding a cycle circular array
# returns true if one exists and false otherwise
# circular: follows one direction as it traverses whether right or left
# cycle: return to the original position where all movements off the edge
# are placed on the opposite of the array
def circular_array_loop(arr):  

    def step(index):
        return (index + arr[index]) % len(arr)

    def isRightDirection(index):
        return arr[index] > 0

    def cycleInCircularExists(start):
    
        slow = start
        fast = step(start)
        initialDir = isRightDirection(start)

        # a cycle when slow and fast converge
        while slow != fast:
            
            fast = step(fast)
            slow = step(slow)
            
            # change direction?
            if initialDir != isRightDirection(fast):
                return False

            fast = step(fast)
            
            # change direction?
            if initialDir != isRightDirection(fast):
                return False        
        return True

    for index in range(len(arr)):
        if cycleInCircularExists(index):
            return True
    return False

# Examples
print(circular_array_loop([3, 3, 1, -1, 2]))

