def underscorifySubstring(string, substring):
    locations = collapse(getLocations(string, substring))
    return underscore(locations, string)


# def getLocations(string,substring):
# 	locations = []
# 	startIdx = 0
# 	for i in range(len(string)):
# 		nextIdx = string.find(substring, startIdx)
# 		if (nextIdx >= 0):
# 			locations.append([nextIdx,nextIdx+len(substring)])
# 			startIdx = nextIdx + 1
# 		else:
# 			break
# 	return locations

def getLocations(string, substring):
    locations = []
    startIdx = 0
    while startIdx < len(string):
        nextIdx = string.find(substring, startIdx)
        if (nextIdx != -1):
            locations.append([nextIdx, nextIdx + len(substring)])
            startIdx = nextIdx + 1
        else:
            break
    return locations


def collapse(locations):
    if not len(locations):
        return locations
    newLocations = [locations[0]]
    prev = newLocations[0]
    for i in range(1, len(locations)):
        current = locations[i]
        if (current[0] <= prev[1]):
            prev[1] = current[1]
        else:
            newLocations.append(current)
            prev = current
    return newLocations


def underscore(locations, string):
    strIdx = 0
    locationIdx = 0
    chars = []
    inBetween = False
    i = 0
    while strIdx < len(string) and locationIdx < len(locations):
        if (strIdx == locations[locationIdx][i]):
            chars.append("_")
            inBetween = not inBetween
            if (not inBetween):
                locationIdx += 1
            i = 0 if i == 1 else 1

        chars.append(string[strIdx])
        strIdx += 1

    if locationIdx < len(locations):
        chars.append("_")
    elif strIdx < len(string):
        chars.append(string[strIdx:])
    return "".join(chars)

# def underscorifySubstring(string, substring):
#     # Write your code here.
# 	subLength = len(substring)
# 	indexes = []
# 	for i in range(len(string)-subLength):
# 		if checkIfSimilar(string[i:i+subLength]):
# 			indexes.append([i,i+subLength])

# 	indexes1D = []
# 	for i in range indexes:
# 		indexes1D.extend(indexes[i])

# 	for i in range(len(string)):


#     pass

string = "testthis is a testtest"
substring = "test"
print(underscorifySubstring(string, substring))