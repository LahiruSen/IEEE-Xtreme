import json
import random

# while True:
#     line = input()
#     if line:
#         lines.append(line)
#     else:
#         break
    
lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

noOflines = lines[0]

# Input = []
# for i in range(noOflines):
#     Input.append(input())  

publications = lines[1]
citations = lines[2:]

#print(type(citations[0]),citations[0])
# line2 = Input[1] 

line1 = '{"publications": [{"publicationTitle" : "Letters on IEEEXtreme", "publicationNumber" : "1","articleCounts" : [{"year" : "2017","articleCount" : "3"}, {"year" : "2018","articleCount" : "6"}]},{"publicationTitle" : "Journal of 24 hours programing", "publicationNumber" : "2","articleCounts" : [{"year" : "2017","articleCount" : "1"}, {"year" : "2018","articleCount" : "4"}]}]}'
line2 = '{"publisher": "IEEE","title": "Publication Title 5","contentType": "periodicals","ieeeCitationCount": "2","publicationNumber": "15","paperCitations": {"ieee": [{"order": "1","articleNumber" : "28","publicationNumber" : "1","year" : "2017","title": "Article 28"},{"order": "2","articleNumber" : "1","publicationNumber" : "1","year" : "2018","title": "Article 1"},{"order": "3","articleNumber" : "109","publicationNumber" : "4","year" : "2018","title": "Article 109"},{"order": "4","articleNumber" : "82","publicationNumber" : "1","year" : "2016","title": "Article 82"},{"order": "5","articleNumber" : "83","publicationNumber" : "1","year" : "2017","title": "Article 83"},{"order": "6","articleNumber" : "136","publicationNumber" : "4","year" : "2018","title": "Article 136"},{"order": "7","articleNumber" : "36","publicationNumber" : "1","year" : "2018","title": "Article 36"},{"order": "8","articleNumber" : "83","publicationNumber" : "4","year" : "2015","title": "Article 83"},{"order": "9","articleNumber" : "132","publicationNumber" : "3","year" : "2018","title": "Article 132"},{"order": "10","articleNumber" : "83","publicationNumber" : "4","year" : "2016","title": "Article 83"},{"order": "11","articleNumber" : "51","publicationNumber" : "4","year" : "2015","title": "Article 51"},{"order": "12","articleNumber" : "37","publicationNumber" : "2","year" : "2015","title": "Article 37"},{"order": "13","articleNumber" : "112","publicationNumber" : "1","year" : "2016","title": "Article 112"},{"order": "14","articleNumber" : "16","publicationNumber" : "1","year" : "2015","title": "Article 16"},{"order": "15","articleNumber" : "2","publicationNumber" : "3","year" : "2019","title": "Article 2"}]}}'
# publications = json.loads(line1)
# publications = publications['publications']

# for i in publications:
#     print(publications[0])

def getTitle(Json_obj):
    publications = {}
    json_array = json.loads(Json_obj)['publications']
    # print(json_array[0]['publicationTitle'])
    for i in range(len(json_array)):
        # print(type(json_array[i]['publicationTitle']))
        articleCounts = json_array[i]['articleCounts']
        articleCount = 0
        for j in articleCounts:
            if(j['year']=="2017" or j['year']=="2018"):
                articleCount+=int(j['articleCount'])
        publications[json_array[i]['publicationTitle']]=[json_array[i]['publicationNumber'],articleCount]
    return publications


def getcitations(Json_obj,publicationNumber):
    noOfCitations = 0
    citation_list = json.loads(Json_obj)['paperCitations']['ieee']
    for citation in citation_list:
        # print(type(citation['publicationNumber']),type(citation['year']))
        if(citation['publicationNumber']==publicationNumber):
            if(citation['year']=="2017" or citation['year']=="2018" ):
                noOfCitations+=1
    # print(noOfCitations)
    return noOfCitations

def getIF(publications,citations):
    titleDic = getTitle(publications)
    titleDicNew= {}
    # publicationNumbers = list(titleDic.values())
    for key,value in titleDic.items():
        publicationNumber = value[0]
        publicationTitle = key
        noOfPublications = value[1]
        onOfCitations = 0
        for j in citations:
            # print(type(j),type(publicationNumber))
            onOfCitations+= getcitations(j,publicationNumber)
        if(noOfPublications!=0):
            score = onOfCitations/float(noOfPublications)
            titleDicNew[publicationTitle]="{0:.2f}".format(round(score,2))
        else:
            titleDicNew[publicationTitle]="0.00"
    return (titleDicNew)
        
    
    
ans = getIF(publications,citations)
# print(getTitle(publications))
# getcitations(line2,"1")
ansnew = sorted(ans, key=ans.get, reverse=True)

for i in ansnew :
    print(i+":",ans[i])
