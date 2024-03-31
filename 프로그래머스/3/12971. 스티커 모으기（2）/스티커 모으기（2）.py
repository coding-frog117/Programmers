def dp(subArray):
    if (len(subArray) == 1):
        return subArray[0]
    
    count = [0 for _ in range(len(subArray))]
    count[0] = subArray[0]
    count[1] = max(subArray[0],subArray[1])
    
    for i in range(2, len(subArray)):
        count[i] = max(count[i-1], count[i-2]+ subArray[i])

    return count[-1]

def solution(sticker):
    if (len(sticker) == 1):
        return sticker[0]
    
    # 만약 한번만 dp 수행하면 sticker[0]이 선택되었을 시 sticker[-1]은 항상 선택이 불가하므로 sticker[0]을 선택하는 경우와 sticker[-1]를 선택하는 경우를 나누어 dp 수행
    # 이를 위해 index 0이 포함된 subArray와 -1이 포함된 subArray로 나눔
    firstArray = sticker[0:len(sticker)-1]
    secondArray = sticker[1:len(sticker)]
    
    answer = max(dp(firstArray), dp(secondArray))
    return answer