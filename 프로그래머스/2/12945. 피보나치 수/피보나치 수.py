def solution(n):
    count = [0 for i in range(n+1)]
    count[0] = 0
    count[1] = 1
    
    for i in range(2,n+1):
        count[i] = count[i-1] + count[i-2]
    
    answer = count[n] % 1234567
    return answer