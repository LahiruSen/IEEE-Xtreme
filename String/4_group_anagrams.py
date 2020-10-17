def groupAnagrams(words):
    # Write your code here.
    anagrams = []
    for word in words:
        if(len(anagrams)==0):
           anagrams.append([word])
           continue
        for i in range(len(anagrams)):
            anagram = anagrams[i]
            if(areAnagrams(word, anagram[0])):
                anagram.append(word)
                anagrams[i] = anagram
                break
        anagrams.append([word])
    return anagrams



def areAnagrams(string1, string2):
    if(sorted(string1)==sorted(string2)):
        return True
    else:
        return False

words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
print(groupAnagrams(words))