def diagonalDifference(arr):
    left = 0
    right = 0
    for i in range(0, len(arr)):
        left += arr[i][i]
        right += arr[(len(arr) - 1) - i][i]
    return abs(left - right)
