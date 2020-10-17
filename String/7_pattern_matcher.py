import math

def patternMatcher(pattern, string):
    if len(pattern) > len(string):
        return []


    patternLen = len(pattern)
    stringLen = len(string)
    patternChanged = False
    result = []

    pattern, patternChanged = getNewPattern(pattern)

    x_count = pattern.count("x")
    y_count = pattern.count("y")
    x_len_min = 1
    x_len_max = math.ceil((stringLen - y_count * 1) / x_count)

    if y_count != 0:
        firstY = pattern.index("y")
        for i in range(x_len_min, stringLen):
            x_len = i
            y_len = (stringLen - x_count * x_len) / y_count

            if y_len <= 0 or y_len % 1 != 0:
                continue
            y_len = int(y_len)
            x = string[:x_len]
            y = string[x_len * firstY: (x_len * firstY + y_len)]

            potentialMatch = map(lambda char: x if char == "x" else y, pattern)
            if string == "".join(potentialMatch):
                return [x, y] if not patternChanged else [y, x]

    else:
        x_len = stringLen / x_count
        if x_len % 1 == 0:
            x_len = int(x_len)
            x = string[:x_len]
            patten_string = "".join(pattern)
            patten_string = patten_string.replace("x", x)
            if string == patten_string:
                result = [x, ""] if not patternChanged else ["", x]

    return result
    pass


def correctPattern(pattern):
    pattern = pattern.replace("x", "z")
    pattern = pattern.replace("y", "x")
    pattern = pattern.replace("z", "y")
    return pattern


def getNewPattern(pattern):
    patternLetters = list(pattern)
    if pattern[0] == "x":
        return patternLetters, False
    else:
        return list(map(lambda char: "x" if char == "y" else "y", patternLetters)), True

pattern = "xxyxxy"
string = "gogopowerrangergogopowerranger"

print(patternMatcher(pattern, string))