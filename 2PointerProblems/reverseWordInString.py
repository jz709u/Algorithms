#!/usr/bin/env python3

def reverse(rs):
	l = 0
	r = len(rs) - 1
	while l < r:
		t = rs[l]
		rs[l] = rs[r]
		rs[r] = t
		l += 1
		r -= 1
	return rs

# O(n ^ 2)
def reverseWordInString(s):
	# list creation from string O(n)
	ls = list(s)

	# reverse list O(n)
	rs = reverse(ls)
	s = -1
	c = 0

	# O(n * w)
	for i in range(len(rs)):
		if rs[i] != " ":
			if s == -1:
				s = i
			c += 1
		if (rs[i] == " " or (i + 1) == len(rs)) and c > 0:
			rs[s:s + c] = reverse(rs[s:s + c])
			c = 0
			s = -1

	return "".join(rs)

print(reverseWordInString("  john   mill clow    show "))


