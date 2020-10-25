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
        array = list(map(str, input().split()))
        input_list.append(array)
    return input_list


# NM = input().split()
# N, M = int(NM[0]), int(NM[1])
# listings = get_list(M)

N, M = 10, 8
listingOld = [['Zulian', '3', '100'], ['Sandfury', '5', '500'], ['Skullsplitter', '6', '900'], ['Bloodscalp', '5', '400'], ['Razzashi', '5', '125'], ['Hakkari', '7', '375'], ['Witherbark', '7', '60'], ['Zulian', '4', '800']]
listings = []

for listItem in listingOld:
    tempList = [listItem[0], int(listItem[1]), int(listItem[2])]
    listings.append(tempList)



# print(N)
# print(M)
# print(listings)

set1 =  {"Zulian":0, "Razzashi":0, "Hakkari":0 }
set2 = {"Sandfury":0, "Skullsplitter":0, "Bloodscalp":0 }
set3 = {"Gurubashi":0, "Vilebranch":0, "Witherbark":0 }

def updateSet(set,coin,listing):
    if set[coin] == 0:
        set[coin] = listing[1:]
    else:
        tempcount = set[coin][0] + listing[1]
        temprice = set[coin][1]+ listing[2]
        set[coin] = [tempcount, temprice]

for listing in listings:
    coin = listing[0]

    if coin in set1.keys():
        updateSet(set1,coin,listing)
    elif coin in set2.keys():
        updateSet(set2,coin,listing)
    elif coin in set3.keys():
        updateSet(set3,coin,listing)




def getMinMax(set):
    tempList = []
    priceList = []
    for key, value in  set.items():
        if value == 0:
            tempList.append(0)
            priceList.append(0)
        else:
            tempList.append(int(value[0]))
            priceList.append(int(value[1]))
    return min(tempList), max(priceList)


set1Min, set1Price = getMinMax(set1)
set2Min, set2Price = getMinMax(set2)
set3Min, set3Price = getMinMax(set3)

priceDict = {"1":set1Price, "2":set2Price, "3":set3Price}

minNoOfSets = set1Min + set2Min+ set3Min
# print(set1)
# print(set1Min, set1Price)
# print(set2)
# print(set2Min, set2Price )
# print(set3)
# print(set3Min, set3Price)

if N > minNoOfSets:
    print("impossible")
else:
    print(max(set1Price,set2Price,set3Price))
# else:
#     priceList = []
#     for key in sorted(priceDict, key=priceDict.get):
#         print(key)




