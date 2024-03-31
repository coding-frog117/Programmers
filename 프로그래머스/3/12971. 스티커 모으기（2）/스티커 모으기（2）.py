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
    
    firstArray = sticker[0:len(sticker)-1]
    secondArray = sticker[1:len(sticker)]
    
    answer = max(dp(firstArray), dp(secondArray))
    return answer