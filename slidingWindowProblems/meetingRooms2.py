from interval import Interval

# finds the minimum amount of rooms
# Performance O(n^2)
# Space O(n)
def find_sets(intervals):
    index = 0
    group = []
    rooms = 0
    allocated = set()
    start = index

    # by the start time sort
    def increasingStart(n):
        return n.start
    intervals.sort(key=increasingStart)

    # untill all has been allocated
    while len(allocated) != len(intervals):
        # base case where end reached and we can know a room is needed
        if index >= len(intervals):
            index = start + 1
            start = index
            rooms += 1
            group = []

        # continue on if already allocated
        if index in allocated:
            index += 1
            continue

        # initial setup for new room
        if len(group) == 0:
            group += [index]
            allocated.add(index)
            index += 1
            continue
        
        # if the last time of the current room is less than or equal to
        # the current looked at interval than it does not overlap
        # so add to room schedule
        if intervals[index].start >= intervals[group[-1]].end:
            group.append(index)
            allocated.add(index)

        index += 1

    # the last group is added if it exists
    if len(group) > 0:
        rooms += 1
        
    return rooms