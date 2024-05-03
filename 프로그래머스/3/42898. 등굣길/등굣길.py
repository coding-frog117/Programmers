def solution(m, n, puddles):
        
    count = [[0]*m for i in range(n)]
    count[0][0] = 0
    if (m>1):
        count[0][1] = 1
    if (n>1):
        count[1][0] = 1
        
    for puddle in puddles:
        count[puddle[1]-1][puddle[0]-1] = -1
    
    for i in range(0, n):
        for j in range(0, m):   
            if count[i][j] == -1 or count[i][j] != 0 :
                continue;
            
#             가장자리 초기화하지 않음. (이유 - m이 1일때 웅덩이가 있음에도 1로 초기화되는 버그 발생함.)
            # if ((i-1 < 0 or j-1 < 0) and ):
            #     count[i][j] = 1
            #     continue;
                
            dx = count[i][j-1]
            dy = count[i-1][j]
            
            if (dx == -1 and dy != -1):
                count[i][j] = dy
            elif (dy == -1 and dx != -1):
                count[i][j] = dx
            elif (dy == -1 and dx == -1):
                count[i][j] = -1
            else:
                count[i][j] = dx+dy
        
    if (count[n-1][m-1] == -1):
        return 0
    answer = (count[n-1][m-1]) % 1000000007
    return answer