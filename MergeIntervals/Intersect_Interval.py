from Interval import *

# intersections
def intersect(interval1, interval2):
    if interval1.end < interval2.start or interval2.end < interval1.start:
        return None
    return Interval(max(interval1.start, interval2.start), min(interval1.end, interval2.end))

# Naive Approach:
# for every item in a: find intersections for every interval of b
# performance: O(a * b)
# 
#
# Function to find the intersecting points between two intervals
# Optimized Approach: O(a + b)
# Space: O(a + b - 1)
# we are going to traverse each list at the same time
# moving forward the earlier one by one otherwise both until one of them hits the end
# hitting the end on just one means we got to the point where the
# rest of a that occur after b will not intersect so we can end early
#
def intervals_intersection(interval_list_a, interval_list_b):
    lenA = len(interval_list_a) 
    lenB = len(interval_list_b)
    indexA = 0
    indexB = 0

    result = []
    while indexA < lenA and indexB < lenB:
        # find intersection of intervals
        interR = intersect(interval_list_a[indexA], interval_list_b[indexB])
        # if it exists add to results
        if interR != None:
            result += [interR]

        # increment the side with lower end
        if interval_list_a[indexA].end > interval_list_b[indexB].end:
            indexB += 1
        elif interval_list_a[indexA].end < interval_list_b[indexB].end:
            indexA += 1
        # otherwise increment both
        else:
            indexA += 1
            indexB += 1
            
    return result