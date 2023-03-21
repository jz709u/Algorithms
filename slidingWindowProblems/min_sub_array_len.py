min_sub_array_len.py


## Naive approach would be to cycle through every possible sub array which is O(n^2)
## then sum all the values of the sub array which would be O(n)
## so Performance: O(n^3)
## Space would be O(1) to store the minimum len

## Optimized approach 
## O(n)
## Space O(1) 
def min_sub_array_len(target, nums):

    result = len(nums) + 1

    windowSum, windowStart, windowLen = 0, 0, 0
    
    for x in range(len(nums)):
        windowSum += nums[x]
        windowLen += 1
        while windowSum >= target:
            result = min(windowLen, result)
            windowSum -= nums[windowStart]
            windowStart += 1
            windowLen -= 1
    
    return 0 if result == len(nums) + 1 else result