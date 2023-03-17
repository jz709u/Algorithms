# naive approach:
# two loops one for s and one for t
# for each s: loop over t if it exists
# O(t * s * t)
# space O(1)

# Optimized Search
# Performance: O(s * t)
# Space O(1)
def min_window(s, t):

    # going to map char to amount of t
    valueToAmount = {}
    for x in t:
        if x in valueToAmount:
            valueToAmount[x] += 1
        else:
            valueToAmount[x] = 1

    #result 
    minLength = float('inf')
    minSequence = ""

    # overall index
    indexS = 0

    # state when looking over small subsections
    attemptToFind = valueToAmount.copy()
    start = 0

    while indexS < len(s):

        # found s in t
        if s[indexS] in attemptToFind:
            # found first element initialize start
            if attemptToFind == valueToAmount:
                start = indexS

            # decrement values in attemptToFind
            if attemptToFind[s[indexS]] == 1:
                del attemptToFind[s[indexS]]
            else:
                attemptToFind[x] -= 1
            # found all elements
            if attemptToFind == {}:
                # get sequence and set min if it's better than existing
                seq = s[start:indexS + 1]
                if len(seq) < minLength:
                    minSequence = seq
                    minLength = len(seq)
                    print(f"new minSequence {minSequence} minlenght {minLength}")
                # reset and start after the first found element
                attemptToFind = valueToAmount.copy()
                indexS = start + 1
                start = 0
                
        indexS += 1
    return minSequence