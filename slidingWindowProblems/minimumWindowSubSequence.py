

# We need to parse back to find the min subseq
def _parseBackToFindMinSubSeq(str1, str2, str1Index):
	# hold index after the end of str1 which is the length
	start, end = str1Index, str1Index + 1
	str2Index = len(str2) - 1
	print(f"parsing back from index: {start}, keep end at {end}")
	while str2Index >= 0:
		if str1[start] == str2[str2Index]:
			print(f"exists: {str1[start]} == {str2[str2Index]}")
			str2Index -= 1
		else:
			print(f"none: {str1[start]}")
		start -= 1
	# this is necessary to account for the last start -=1
	# in the while loop 
	start += 1
	print(f"window from {start} to {end}")
	newMinLength = end - start

	return (start, newMinLength, str1[start:end])
	
# 1. Parse over the seq1 till all of seq2 has been found
# 2. then parse back to find the min of that seq
# 3. Start again from the index after the beginning of minSeq1 was found 
def _findFirstSequenceWhereAllStr2IsInStr1(str1, str2):
	str1Index, str2Index = 0, 0
	minimumLen = float('inf')
	min_subsequence = ""

	while str1Index < len(str1):
		print(f"starting from {str1Index} with {str1[str1Index]}")
		if str1[str1Index] == str2[str2Index]:
			str2Index += 1
			if str2Index == len(str2):

				(start, newMinLength, subSeq) = _parseBackToFindMinSubSeq(str1, str2, str1Index)

				if newMinLength < minimumLen:
					minimumLen = newMinLength
					min_subsequence = subSeq
					print(f"min length setting {minimumLen} with seq {min_subsequence}")
				else:
					print(f"no less than existing found:{subSeq}")

				# reset for next window 
				print(f"reseting at {start} and 0")
				str1Index = start
				str2Index = 0
		str1Index += 1
	return (min_subsequence, minimumLen)

# naive approach 
# Performance: O(n^3)
# Space: O(1)
# optimized 
# Performance: O(n * m)
# Space: O(1)
# 
def minimumWindowSubsequence(str1, str2):
	return _findFirstSequenceWhereAllStr2IsInStr1(str1, str2)

def main():
    str1 = ["abcdebdde", "fgrqsqsnodwmxzkzxwqegkndaa",
            "qwewerrty", "aaabbcbq", "zxcvnhss", "alpha",
            "beta", "asd", "abcd"]
    str2 = ["bde", "kzed", "werty", "abc", "css", "la", "ab", "as", "pp"]

    for i in range(len(str1)):
        print(i+1, ". \tInput string: (" + str1[i]+", " + str2[i]+")", sep="")
        print("\tSubsequence string: ", minimumWindowSubsequence(str1[i], str2[i]))
        print("-"*100)


if __name__ == '__main__':
    main()