def solution(n, times):
    left = min(times)
    right = max(times) * n
    answer = right
    
    while (left <= right):
        people = 0
        targetTime = (left+right) //2
        for time in times :
            people += targetTime // time
            
            if (people > n):
                break
        if (people >= n):
            answer = min(answer,targetTime)
            right = targetTime -1
        elif (people < n):
            left = targetTime + 1
    
    return answer;