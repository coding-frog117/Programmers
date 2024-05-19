def solution(N, stages):
    result = []
    for i in range(1,N+1):
        fail = 0
        challenge = 0
        
        for stage in stages:
            if stage >= i:
                if stage == i:
                    fail += 1
                challenge += 1
        if fail == 0 :
            result.append([0,-i])
        else:
            result.append([fail/challenge,-i])

    result.sort(reverse=True)
    ans = []
    for i in result:
        ans.append(i[1]*-1)
        
    return ans
        