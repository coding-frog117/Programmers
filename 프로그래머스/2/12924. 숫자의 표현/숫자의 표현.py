def solution(n):
    ans = 0
    currSum =1
    arr = [i for i in range(1,n+1)]
    
    start = 1
    end = 1
    
    while end <= n:
        if currSum < n:
            end+= 1
            currSum += (end)
        elif currSum > n:
            currSum -= (start)
            start += 1
        else :
            ans += 1
            end += 1
            currSum += end
            
    return ans