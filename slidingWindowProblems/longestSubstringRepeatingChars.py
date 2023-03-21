longestSubstringRepeatingChars.py

# each index find the longest substring without any repeated characteres
# Performance: O(n^3)
# Space: O(min(characterSet, n))
# optimized approach 
# window approach using a dictionary we can save the location of duplicate
# then when we start from the index after the duplicate.
# Performance: O(n^2)
# Space O(min(characterSet, n))
def find_longest_substring(str):
   if len(str) == 0: 
      return 0
   result = 1
   index = 0
   
   while index < len(str):
      window = dict()
      substringIndex = index
      while substringIndex < len(str) and str[substringIndex] not in window:
         window[str[substringIndex]] = substringIndex
         substringIndex += 1
      result = max(len(window), result)

      if substringIndex < len(str):
         index = window[str[substringIndex]] + 1
      else:
         index += 1
   return result


## optimized O(n)
## space(n)
def find_longest_substring(str):
    # Check the length of str
    if len(str) == 0:
        return 0

    window_start, longest, window_length = 0, 0, 0

    last_seen_at = {}

    # Traverse str to find the longest substring
    # without repeating characters.
    for index, val in enumerate(str):
        # If the current element is not present in the hash map,
        # then store it in the hash map with the current index as the value.
        if val not in last_seen_at:
            last_seen_at[val] = index
        else:
            # If the current element is present in the hash map,
            # it means that this element may have appeared before.
            # Check if the current element occurs before or after `window_start`.
            if last_seen_at[val] >= window_start:
                window_length = index - window_start
                if longest < window_length:
                    longest = window_length
                window_start = last_seen_at[val] + 1

            # Update the last occurence of
            # the element in the hash map
            last_seen_at[val] = index

    index += 1
    # Update the longest substring's
    # length and starting index.
    if longest < index - window_start:
        longest = index - window_start

    return longes