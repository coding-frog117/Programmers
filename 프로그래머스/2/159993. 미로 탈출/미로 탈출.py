from collections import deque

def solution(maps):
    newArr = []
    
    for i in maps:
        newArr.append(list(i))
        
    queue = deque()
    answer = 0
    S = []
    L = []
    E = []
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                S = [i,j]
            elif maps[i][j] == 'L' :
                L = [i,j]
            elif maps[i][j] == 'E':
                E = [i,j]
    length = 0
    queue.append([S[0],S[1],length])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    seen = [[S[0],S[1]]]
    
    while queue:
        y,x,currLen = queue.popleft()
        if y == L[0] and x == L[1] :
            answer += currLen
            break
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or nx >= len(maps[0]) or ny < 0 or ny >= len(maps):
                continue
            if newArr[ny][nx] == 'X' or [ny,nx] in seen:
                continue
            
            seen.append([ny,nx])
            queue.append([ny,nx,currLen+1])
        
    if (answer == 0):
        return -1
    
    secondLen = 0
    secondAnswer=0
    secondQueue = deque()
    secondQueue.append([L[0],L[1],secondLen])
    seen = [[L[0],L[1]]]
    while secondQueue:
        y,x,currLen = secondQueue.popleft()
        if y == E[0] and x == E[1] :
            answer += currLen
            secondAnswer += currLen
            break
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or nx >= len(maps[0]) or ny < 0 or ny >= len(maps):
                continue
            if newArr[ny][nx] == 'X' or [ny,nx] in seen:
                continue
            
            seen.append([ny,nx])
            secondQueue.append([ny,nx,currLen+1])
        
    if (secondAnswer == 0):
        return -1
    return answer