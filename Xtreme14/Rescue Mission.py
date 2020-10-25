# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


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


def get_list(n):
    input_list = []
    for i in range(n):
        array = list(map(int, input().split()))
        input_list.append(array)
    return input_list


# N = get_number()
# sList = list(map(int, input().split()))
# D = get_number()
# LRV = get_list(D)

N = 4
sList = [5, 4, 3, 2]
D = 4
LRV = [[1, 2, 4], [1, 1, 3], [2, 4, 1], [3, 3, 4]]

# print(N)
# print(sList)
# print(D)
# print(LRV)

sDict = {}
for i in range(len(sList)):
    sDict[str(i)] = sList[i]

def updatesDict(remainingSolders,foggyHideOuts, future ):
    remainingSolders = remainingSolders
    futureDay = 0
    while futureDay<len(future) and remainingSolders> 0:
        futureFoggyHideouts = future[:2]
        futureVehicalCapacity = future[2]
        for hideOute in range(futureFoggyHideouts[0], futureFoggyHideouts[1]):
            if hideOute in range(foggyHideOuts[0], foggyHideOuts[1]):
                CurrentlyOnHideout = sDict[hideOute]
                availableSpace = futureVehicalCapacity - CurrentlyOnHideout
                if availableSpace < remainingSolders:
                    sDict[hideOute] =   CurrentlyOnHideout +  remainingSolders
                    break
                else:
                    sDict[hideOute] = futureVehicalCapacity
                    remainingSolders -= availableSpace


def rescue(present,future ):
    vehicleCapacity = present[2]
    availableSolders = 0
    foggyHideOuts = present[:2]
    for hideout in range(foggyHideOuts[0], foggyHideOuts[1]):
        sDict[str(hideout)] = 0
        availableSolders += sDict[str(hideout)]
    if (availableSolders <= vehicleCapacity):
        return  availableSolders

    else:
        remainingSolders = availableSolders - vehicleCapacity
        updatesDict(remainingSolders, foggyHideOuts, future)
        return vehicleCapacity



rescuredSolders = 0

for day in range(D):
    present = LRV[day]
    future = LRV[day+1:]
    rescuredSolders += rescue(present,future )

print(rescuredSolders)


