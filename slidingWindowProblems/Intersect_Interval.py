from Interval import *

# intersections
def intersect(interval1, interval2):
    if interval1.end < interval2.start or interval2.end < interval1.start:
        return None
    return Interval(max(interval1.start, interval2.start), min(interval1.end, interval2.end))

# Function to find the intersecting points between two intervals
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