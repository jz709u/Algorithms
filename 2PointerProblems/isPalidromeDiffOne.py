# O(n)
def is_palindrome_diff_one(s):
  l = 0
  r = len(s) - 1
  diff = 0
  while l <= r:
    if s[l] != s[r]:
      if s[l] == s[r - 1]:
        r -= 1
        diff += 1
      elif s[l + 1] == s[r]:
        l += 1
        diff += 1
      else:
        return False
    if diff == 2:
      return False
    l += 1
    r -= 1
  return True