# Importing doubly ended queue
from collections import deque


def find_max_sliding_window(nums, window_size):

    result = []
    window = deque()
    
    # example edge case where window size is greater than the length
    # of the size of array of nums
    window_size = min(window_size, len(nums))

    right = -1
    left = 0

    # pop items in the window which is less than the current value 
    # example: [2,<4>,19,2,-20], 
    #          window: [0] 
    #          should pop and become [] because 4 > 2
    def popWindowFromRightWhileLessThanCurrentIndex(index):
        while window and nums[index] >= nums[window[right]]:
            window.pop()

    # index 8 with a window size of 3
    # window[0] is left side would be 5
    # 5 <= 8 - 3 
    # window: [5,6,7,8] window size 3
    # pop -> [6,7,8]
    def maintainWindowLengthByPoppingLeft(index):
        if window and window[left] <= (index - window_size):
            window.popleft()

    # expand window right [0,1] -> [0,1,2]
    def expandWindowRight(index):
        window.append(index)

    # max value should always be in left side of window
    def pushMaxValueFromWindow():
        result.append(nums[window[left]])

    # 1. start populating first window
    # 2. fill first max result for first window
    for i in range(window_size):
        popWindowFromRightWhileLessThanCurrentIndex(i)
        expandWindowRight(i)
    pushMaxValueFromWindow()
    
    # move the window to the right while populating
    # max results 
    for i in range(window_size, len(nums)):
        popWindowFromRightWhileLessThanCurrentIndex(i)
        maintainWindowLengthByPoppingLeft(i)
        expandWindowRight(i)
        pushMaxValueFromWindow()
            
    return result


def main():
    target_list = [3, 3, 3, 3, 2, 4, 3, 2, 3, 18]
    nums_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                 [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                 [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
                 [1, 5, 8, 10, 10, 10, 12, 14, 15, 19, 19, 19, 17, 14, 13, 12, 12, 12, 14, 18, 22, 26, 26, 26, 28, 29, 30],
                 [10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67],
                 [4, 5, 6, 1, 2, 3],
                 [9, 5, 3, 1, 6, 3],
                 [2, 4, 6, 8, 10, 12, 14, 16],
                 [-1, -1, -2, -4, -6, -7],
                 [4, 4, 4, 4, 4, 4]]

    for i in range(len(nums_list)):
        print(i + 1, ".\tOriginal array:\t", nums_list[i], sep="")
        print("\tWindow size:\t", target_list[i])
        print("\n\tMax:\t\t",
              find_max_sliding_window(nums_list[i], target_list[i]))
        print("-"*100)


if __name__ == '__main__':
    main()
