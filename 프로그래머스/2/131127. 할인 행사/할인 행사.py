import copy

def solution(want, number, discount):
    wantMap = {}
    
    # hash 사용
    for i in range(len(want)):
        wantMap[want[i]] = number[i]
        
    startIdx = 0
    endIdx = 9
    subArr = discount[0:10]
    answer = 0
    
    # 슬라이딩 윈도우로 sub 배열 체크
    for disIdx in range(len(discount)):
        if sum(number) > len(subArr):
            break
        
        subMap = {}
        for i in subArr:
            if subMap.get(i) :
                subMap[i] += 1
            else:
                subMap[i] = 1
                
        checkCount = True
        for i in want:
            if subMap.get(i) == None or wantMap[i] > subMap[i] :
                checkCount = False
        if checkCount :
            answer += 1
        
        startIdx += 1
        if endIdx < len(discount)-1:
            endIdx += 1
            subArr.append(discount[endIdx])
            subArr = subArr[1:]
        else:
            break
    return answer