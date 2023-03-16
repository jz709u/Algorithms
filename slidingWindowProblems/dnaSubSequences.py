
# unoptimized solution
# where O((n + 1 - k) k)
# where iterating over all possible contigous sets
# of length k windows
# space O(n + 1 - k)
def allRepeatedSubsequences(s, k):
    n = len(s)
    if k >= n:
        return set()
    found = set()
    result = set()
    for i in range(0, n + 1 - k):
        # slice is k^2 copying 
        v = s[i:i + k]
        if v in found:
            result.add(v)
        else:
            found.add(v)
    return result


# optimized solution
# speed: O(n + 1 - k)
# space: O(k)
def optimizedAllRepeatedSubstrings(s,k):
    n = len(s)
    if k >= n:
        return set()

    # -------- encoding step ---------
    base = 4
    mappings = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    # the base raised to the window size - 1 
    # window size is 3 then 
    # 4^2 * num[2] + 4^1 * num[1] + 4^0 * num[0]
    #     ^
    # high position
    #
    highPosition = pow(base, k - 1) # 4 ^ k - 1
    mappedSeqtoNum = []

    # map sequence to base 4 encoded numbers
    for i in range(n):
        mappedSeqtoNum.append(mappings[s[i]])


    found, result = set(), set()
    # rolling hash
    windowHash = 0
    
    # all Windows n - k + 1

    # initialize first window
    for v in range(k):
        windowHash = windowHash * base + mappedSeqtoNum[v]

    found.add(windowHash)

    # Remaining Windows 
    remainingWindows = n - k
    for i in range(remainingWindows):

        # remove left position
        windowHash -= mappedSeqtoNum[i] * highPosition

        # add right position
        windowHash = (windowHash * base) + mappedSeqtoNum[i + k]

        # if found again
        if windowHash in found:
            result.add(s[i:i + k])

        # add to found
        found.add(windowHash)

    return result

print(optimizedAllRepeatedSubstrings('ACGTACGT', 3))

