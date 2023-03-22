from interval import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed
    # set the flag for closed/open

    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]" \
            if self.closed else \
                "(" + str(self.start) + ", " + str(self.end) + ")

## Naive approach 
## Performance compare every interval with every other interval
## O(n(n))
## Space: O(1)

## Optimized O(n)
## Space: O(1)
def merge_intervals(v):
    if len(v) <= 1:
        return v
    result = []
    buildingInt = v[0]
    for index in range(1,len(v)):
        curr = v[index]
        
        if buildingInt.end >= curr.start and curr.end > buildingInt.end:
            buildingInt.end = curr.end
        elif curr.start > buildingInt.end:
            result += [buildingInt]
            buildingInt = curr
    result += [buildingInt]

    return result

