# a simple parser for python. use get_number() and get_word() to read
# numpy and scipy are available for use
# import numpy
# import scipy
import xml.etree.ElementTree as ET
import re
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

# def removeStopWords(string):
#     querywords = string.split()
#     for word in querywords:
#         if word in stopWords:
#
#
#     resultwords = [word.lower() for word in querywords if word.lower() not in stopWords]
#     result = ''.join(resultwords)
#
#     return result
def removeStopWords(string):
    querywords = string.split()
    list1 = []
    for word in querywords:
        if word.lower() not in stopWords:
            list1.append(word.lower())
        else:
            list1.append(" ")
    # resultwords = [word.lower() for word in querywords if word.lower() not in stopWords]
    result = ' '.join(list1)
    return result

def removePuncuations(string):
    rx = '[' + re.escape(''.join(puncuations)) + ']'
    return re.sub(rx, '', string)

def getTagContent(xmlstring, tree, tagname):
    # #method1
    # content = []
    # for fact in tree.iter(tag=tagname):
    #     content.append(fact.text)
    # return content

    bodytmp = ET.fromstring(xmlstring).getiterator(tagname)
    for bodytemp1 in bodytmp:
        return [' '.join(bodytemp1.itertext())]

def getbody(xmlstring, tree):
    # root = ET.fromstring(xmlstring)
    # contentlist = []
    # for content in root.findall('.//response/body'):
    #     # ... process content, for instance
    #     contentlist.append(content)
    # return contentlist
    bodytmp = ET.fromstring(xmlstring).getiterator('body')
    for bodytemp1 in bodytmp:
        return [' '.join(bodytemp1.itertext())]
    # content = []
    # for body in tree.iter(tag="body"):
    #     for p in body.iter(tag="p"):
    #         if len(p.text.strip()) > 0:
    #             content.append(p.text)
    # return content



def calculateSW(weight, stringList):
    L = 0
    pattern = re.compile("[a-z']+")
    for string in stringList:
        if len(string) > 0:
            string = removePuncuations(string)
            string = removeStopWords(string)

            for word in string.split():
                if (len(word)) >= 4 and bool(pattern.fullmatch(word)):
                    L += 1
                    if (word in indexTermsDict.keys()):
                        indexTermsDict[word] += weight

    return  L

def calculateD(L, dict):
    for key in dict.keys():
        dict[key] = dict[key]/L * 100
    return dict



puncuations = [',', '.', '?', '!']
stopWords =  ['what', 'when', 'where', 'like', 'that', "\n"]
indexTerms =  ['welcome', 'ieee', 'xtreme', 'ieeextreme', 'programming']
indexTermsDict = dict.fromkeys(indexTerms, 0)
document =  "<title>Welcome to IEEEXtreme!</title><keyword>welcome, ieeextreme</keyword><abstract>Welcome!Participants!!!IEEE Xtreme is a global challenge in which teams of IEEE Student members, advised and proctored by an IEEE member, and often supported by an IEEE Student Branch.Compete in a twentyfour hour timespan against each other to solve a set of ...XtremE... programming problems in IEEEXtreme.</abstract><body>WELCOME. wel.come... Are you ready? Good luck and have fun in xtreme!</body><other>Mark your calender and don't miss the action.</other>"

# stopWords = get_word().split(";")
# indexTerms = get_word().split(";")
# indexTermsDict = dict.fromkeys(indexTerms, 0)
# document = []
# while True:
#     try:
#         line = input()
#     except EOFError:
#         break
#     document.append(line)

xmlstring = "".join(line for line in document)
xmlstring =  "<root>"+ xmlstring+"</root>"
# tree = ET.fromstring(re.sub(r"(<\?xml[^>]+\?>)", r"\1<root>", xmlstring) + "</root>")
tree = ET.ElementTree(ET.fromstring(xmlstring))
title = getTagContent(xmlstring, tree, "title")
abstract = getTagContent(xmlstring, tree, "abstract")
body = getbody(xmlstring, tree)

print("stopwords : ",stopWords)
print("index temrs : ",indexTerms)
print("title : ", title)
print("abstract : ", abstract)
print("body : ", body)

L1 = calculateSW(5, title)
L2 = calculateSW(3, abstract)
L3 = calculateSW(1, body)
L = L1+L2+L3

print(L)
print(L1,L2,L3)
print(indexTermsDict)

updatedIndexTermsDict = calculateD(L,indexTermsDict)
print(updatedIndexTermsDict)

# for key, value in sorted(updatedIndexTermsDict.items(), key=lambda x: x[1], reverse=True)[:3]:
#     print("{}: {}".format(key, value))

def printnew(updatedIndexTermsDict):
    # sorted = sorted(updatedIndexTermsDict.items(), key=lambda x: x[1], reverse=True)
    ansList = []
    # for key, value in sorted(updatedIndexTermsDict.items(), key=lambda x: x[1], reverse=True):
    #     ansList.append([key, value])
    # for i in range (len(ansList)-1):
    #     if ansList[i][1] == ansList[i+1][1]:
    #         if ansList[i][0] > ansList[i+1][0]:
    #             ansList[i] , ansList[i+1] = ansList[i+1] , ansList[i]

    ansdict = sorted(updatedIndexTermsDict.items(), key=lambda t: t[::-1])
    for key, value in ansdict:
        ansList.append([key,value])

    i = 0
    while(i<3 or ansList[i-1][1] == ansList[i][1] ):
        print(ansList[i][0]+": "+str(ansList[i][1]))
        i += 1

printnew(updatedIndexTermsDict)