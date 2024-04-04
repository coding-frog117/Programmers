def solution(k, dungeons):
    seen = [0]*len(dungeons)
    
    global maxCount
    maxCount = 0
    
    def dfs(total,count,current):
        global maxCount
        maxCount = max(count,maxCount)
        for i in range(len(dungeons)):
            
            if (current == dungeons[i]):
                continue;
                
            if ((dungeons[i][0]) <= total and total - dungeons[i][1] >= 0 and seen[i] == 0):
                seen[i] =1
                dfs(total - dungeons[i][1],count+1,dungeons[i])
                seen[i] =0
        return maxCount
    
    return dfs(k,0,dungeons[0])