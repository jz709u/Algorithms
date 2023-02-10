#!/usr/bin/env python3

# Naive Approach

# O(n^3)
def naiveThreeSumProblem(arr, sumTo):

    arrSize = len(arr)
    
    for i in range(0, arrSize - 2):

        for x in range(i + 1, arrSize - 1):

            for y in range(x + 1, arrSize):
                print("values: ", arr[i], arr[x], arr[y])

                if arr[i] + arr[x] + arr[y] == sumTo:
                    return True

    return False

# Optimal Solution 2 Pointer O(n^2)
def threeSumProblem(arr, sumTo):

    arrSize = len(arr)

    # sort elements with timsort( O(nlogn) )
    sArr = sorted(arr)

    for i in range(0, arrSize - 2):

        left = i + 1

        right = arrSize - 1

        while left < right:

            if arr[i] + arr[left] + arr[right] == sumTo:
                print("result: ", i,  " ", arr[i],  ", ", left, " ", arr[left],  ", ",  right,  " ", arr[right])

                return True
            elif arr[i] + arr[left] + arr[right] > sumTo:

                right -= 1
            else:
                left += 1
    return False  


print(threeSumProblem([1,2,34,232,5,100,55,6,7,8,10],40))

print(naiveThreeSumProblem([1,2,34,232,5,100,55,6,7,8,10],2030))
