def buildString(a, b, s):
    # Write your code here
    # only copy if a * n(subset) < b else a * n(subset)
    if len(s) == 0:
        return 0
    addCost = a
    copyCost = b
    sIndex = 1
    result = s[0]
    queue = ""
    cost = addCost
    while len(s) != len(result):
        queue += s[sIndex]
        if queue not in result and len(queue) == 1:
            cost += addCost
            result += queue
            queue = ""
        elif queue not in result and len(queue) > 1:
            if (len(queue) - 1) * addCost < copyCost:
                cost += (len(queue) - 1) * addCost
            else:
                cost += copyCost
            if queue[len(queue) - 1] in result:
                cost += addCost if addCost < copyCost else copyCost
            else:
                cost += addCost
            result += queue
            queue = ""
        elif queue in result and len(queue) * addCost < copyCost:
            result += queue
            queue = ""
            cost += addCost
        elif queue not in result:
            result += queue
            queue = ""
            cost += addCost
        sIndex += 1
    return cost
