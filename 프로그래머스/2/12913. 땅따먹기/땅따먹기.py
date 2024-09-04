def solution(land):
    #DFS로 모든 경로 탐색해서 최대값 return
    #자기자신의 인덱스만 제외하고 선택하기
    #시간초과뜸 -> DP - 2차원 배열에 각 위치까지의 최댓값 구하기
    
    dp = [[0,0,0,0] for i in range(len(land))]
    for i in range(4):
        dp[0][i] = land[0][i]
    
    for i in range(1,len(land)):
        for j in range(4):
            maxNums = []
            for z in range(4):
                if z == j:
                    continue
                maxNums.append(dp[i-1][z]+land[i][j])
            dp[i][j] = max(maxNums)
    
    return max(dp[-1][0],dp[-1][1],dp[-1][2],dp[-1][3])