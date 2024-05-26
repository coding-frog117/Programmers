def solution(str1, str2):
    str1start = 0
    str1end = 1
    str1Set = []
    str2Set=[]
    
    def checkValidString(string):
        if string.isalpha():
            return True
        return False
    
    while str1end < len(str1):
        substring = str1[str1start:str1end+1]
        if checkValidString(substring):
            subString = str1[str1start].lower()+str1[str1end].lower()
            str1Set.append(subString)
        str1start += 1
        str1end += 1
    
    str2start = 0
    str2end = 1

    while str2end < len(str2):
        substring = str2[str2start:str2end+1]
        if checkValidString(substring):
            subString = str2[str2start].lower()+str2[str2end].lower()
            str2Set.append(subString)
        str2start += 1
        str2end += 1
    
    if len(str1Set) == 0 and len(str2Set) ==0:
        return 65536
    
    unionSet= []
    intersectSet= []
    
    copystr2Set = str2Set[:]
    
    for i in str1Set:
        if i not in copystr2Set:
            unionSet.append(i)
        else:
            intersectSet.append(i)
            copystr2Set.remove(i)
    
    unionSet = unionSet + str2Set
    print(unionSet,intersectSet)

    answer = int((len(intersectSet) / len(unionSet)) * 65536)
    return answer