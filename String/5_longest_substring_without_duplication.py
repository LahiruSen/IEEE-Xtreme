def longestSubstringWithoutDuplication(string):
	longestsubString = ""
	for i in range(len(string)):
		for j in range(i,len(string)+1):
			if(notIncludDuplicates(string[i:j])):
				if(len(longestsubString)< len(string[i:j])):
					longestsubString = string[i:j]
	return longestsubString
	pass


def notIncludDuplicates(string):
	charList = set([char for char in string])
	if (len(charList) != len(string)):
		return False
	return True

string = "clementisacap"
print(longestSubstringWithoutDuplication(string))