def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)
def get_list():
    input_list = []
    n = get_number()
    for i in range(n):
        array = list(map(str, input().split()))
        input_list.append(array)
    return input_list

#################################################################
# method1

# def longestPalindromicSubstring(string):
#     # Write your code here.
#     Palindrome = ""
#     length = len(string)
#     if (length) == 1:
#         return string
#     for i in range(length):
#         for j in range(i, length):
#             substring = string[i:j + 1]
#             if isPalindrome(substring):
#                 if (len(substring) > len(Palindrome)):
#                     Palindrome = substring
#     return Palindrome
#
# def isPalindrome(string):
#     leftIndex = 0
#     rightIndex = len(string) - 1
#     while (rightIndex > leftIndex):
#         if (string[leftIndex] != string[rightIndex]):
#             return False
#         leftIndex += 1
#         rightIndex -= 1
#     return True



#################################################################
# method2

def longestPalindromicSubstring(string):
    currentLongest = [0,1]
    for i in range(1, len(string)):
        odd = getLongestPalindromeFrom(string, i-1, i+1)
        even = getLongestPalindromeFrom(string, i-1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0] )
    return  string[currentLongest[0] : currentLongest[1] ]

def getLongestPalindromeFrom(string,leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx  += 1
    return  [leftIdx+1, rightIdx]

################################################################################



# input = get_list()
input = [['xabcbayabbaz'], ['abcbaabc'], ['abcba']]

def getlensum(string1, string2):
    return len(string1)+len(string2)


def calculate(string):
    maxLen = 0
    for i in range(1,len(string)):
        string1 = string[:i]
        string2 = string[i:]
        currentMaxLen = getlensum(longestPalindromicSubstring(string1), longestPalindromicSubstring(string2))
        if  currentMaxLen > maxLen:
            maxLen = currentMaxLen
    return maxLen



# print(longestPalindromicSubstring("abc"))

for string in input:
    print(calculate(string[0]))

