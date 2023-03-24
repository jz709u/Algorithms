class Interval:
   def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed

    # set the flag for closed/open
    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) \
              + "]" if self.closed else "(" + str(self.start) + ", " \
              + str(self.end) + ")"

# Naive approach:
# for each interval merge with every other interval
# and see if they exist in the new_interval
# save flag for each interval that says those can be merged 
# then at the end for each true get the lower and upper value
# and create a new one and insert 
# for each false leave as is
# Performance: O(n^2)
# Space: O(n)

#
# Optimized approach:
# O(n)
# space O(n)
def insert_interval(existing_intervals, new_interval):

  lower = new_interval.start
  upper = new_interval.end
  inserted = False
  result = []

  for interval in existing_intervals:
    # here we check once the upper is less than the beginning of the interval
    # then insert the merged interval and set inserted to true
    if upper < interval.start and not inserted:
          inserted = True
          result.append(Interval(lower, upper))

    # if the interval exists outside or does not overlap with the
    # inserted interval
    if interval.end < lower or interval.start > upper:
      result += [interval]

    # find the merged intervals and updating when an interval's
    # lower or upper bounds will extend the final merged interval
    else:
      if lower <= interval.end and upper >= interval.end:
        lower = min(lower, interval.start)
      if upper >= interval.start and lower <= interval.start:
        upper = max(upper, interval.end)
  # edge case where the inserted interval is in the last position 
  # and does not overlap existing intervals
  if not inserted:
    result.append(new_interval)
  return result