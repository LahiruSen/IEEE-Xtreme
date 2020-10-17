def longestPalindromicSubstring(string):
    # Write your code here.
    Palindrome = ""
    length = len(string)
    if (length) == 1:
        return string
    for i in range(length):
        for j in range(i, length):
            substring = string[i:j + 1]
            if isPalindrome(substring):
                if (len(substring) > len(Palindrome)):
                    Palindrome = substring
    return Palindrome

def isPalindrome(string):
    leftIndex = 0
    rightIndex = len(string) - 1
    while (rightIndex > leftIndex):
        if (string[leftIndex] != string[rightIndex]):
            return False
        leftIndex += 1
        rightIndex -= 1
    return True

string = "abaxyzzyxf"

print(longestPalindromicSubstring(string))