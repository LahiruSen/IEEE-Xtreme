def isPalindrome(string):
    new = ""
    for i in reversed(range(len(string))):
        new += string[i]
    return (string == new)
    pass

string = "abcdcba"

print(isPalindrome(string))