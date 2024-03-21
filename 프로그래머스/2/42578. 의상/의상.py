import itertools

clothDict = {}


def solution(clothes):
    count = 1
    for cloth in clothes :
        clothDict[cloth[1]] = clothDict.get(cloth[1], [])
        clothDict[cloth[1]].append(cloth[0])
    
    for i in clothDict:
        clothList = clothDict[i]
        wearCount = len(clothList) +1
        count *= wearCount
        
    return count-1