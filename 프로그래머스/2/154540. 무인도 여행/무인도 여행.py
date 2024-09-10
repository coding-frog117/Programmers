def solution(maps):
    for idx,i in enumerate(maps):
        maps[idx] = list(i)

    dx = [1,-1,0,0]
    dy =[0,0,1,-1]
    ans = []
    vis = [[False for i in range(len(maps[0]))] for i in range(len(maps))]
    
    def DFS(y,x):
        stack = [[y,x]]
        total = int(maps[y][x])
        while stack:
            y,x = stack.pop()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                
                if ny < 0 or nx < 0 or ny >= len(maps) or nx >= len(maps[0]):
                    continue
                if vis[ny][nx] == True:
                    continue
                
                if maps[ny][nx] != 'X':
                    vis[ny][nx] = True
                    stack.append([ny,nx])
                    total+= int(maps[ny][nx])
            if not stack:
                return total
            
    while True:
        isPossible = False
        for row_idx,row in enumerate(maps):
            for col_idx,col in enumerate(row):
                if vis[row_idx][col_idx] == False and col != 'X':
                    isPossible = True
                    vis[row_idx][col_idx] = True
                    ans.append(DFS(row_idx,col_idx))
        if isPossible == False:
            break
            
    if ans == []:
        return [-1]
    ans.sort()
    return ans
            