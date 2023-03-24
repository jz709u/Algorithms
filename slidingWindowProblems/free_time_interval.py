from interval import Interval

def intersect(interval1, interval2):
    if interval1.end <= interval2.start or interval2.end <= interval1.start:
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
        #print(f"from {interval_list_a[indexA]} and {interval_list_b[indexB]}")
        interR = intersect(interval_list_a[indexA], interval_list_b[indexB])
        #print(f"intersect {interR}")
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

# find all free intervals intervals in a schedule
# P: O(n)
# S: O(n)
def calculateFree(schedule, start, end):
    
    _begin = start
    result = []
    for sched in schedule:
        diff = sched.start - _begin
        if diff > 0:
            result += [Interval(_begin, sched.start)]
        _begin = sched.end

    freeEndDiff = end - schedule[-1].end 
    if freeEndDiff > 0:
        result += [Interval(schedule[-1].end, end)]
    return result

# find the start and end times of everyones schedule
# P: O(n)
# S: O(1)
def calculateStartAndEnd(schedule):
    start = float('inf')
    end = float('-inf')
    for employeeSched in schedule:
        start = min(start, employeeSched[0].start)
        end = max(end, employeeSched[-1].end)
    return (start, end)

# O(s * n)
# O(k) k == free intervals
def employee_free_time(schedule):  
    if len(schedule) == 0:
        return []

    # s = employee count
    # O(s)
    start, end = calculateStartAndEnd(schedule)

    # n = interval count
    # O(n)
    currentFree = calculateFree(schedule[0], start, end)
    
    # O(s * n)
    for i in range(1, len(schedule)):
        indexFree = calculateFree(schedule[i], start, end)
        currentFree = intervals_intersection(currentFree, indexFree)
            
    return currentFree
