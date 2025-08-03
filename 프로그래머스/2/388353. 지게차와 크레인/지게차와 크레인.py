def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
        
    # 삭제된 블럭
    deleted = [[False] * m for _ in range(n)]
    # 가장자리 영역
    line = [[False] * m for _ in range(n)]
    
    # 초기 가장자리 영역 셋팅
    for i in range(n) :
        if (i == 0 or i == n-1):
            for j in range(m) :
                line[i][j] = True
        else :
            line[i][0] = True
            line[i][m-1] = True
                
    def DFS1(target):
        stack = []
        delete_target = set()
        seen = set()
        
        for i in range(n):
            for j in range(m):
                if line[i][j]:
                    stack.append((i,j,seen))
        
        while stack :
            i,j,seen = stack.pop()
            if (i,j) in seen :
                continue
            # 현재 블록이 타겟이고 삭제되지 않은 블록인 경우 : 삭제
            if storage[i][j] == target and not deleted[i][j]:
                delete_target.add((i,j))
                seen.add((i,j))
                for k in range(4) :
                    ny = dy[k] + i
                    nx = dx[k] + j
                    if ny < 0 or nx <0 or ny >= n or nx >= m :
                        continue
                    if line[ny][nx] and deleted[ny][nx]:
                        line[i][j] = True
                continue 
            # 삭제된 블록인 경우 : 주변 블록 탐색
            if deleted[i][j]:
                for k in range(4) :
                    ny = dy[k] + i
                    nx = dx[k] + j
                    if ny < 0 or nx <0 or ny >= n or nx >= m :
                        continue
                    stack.append((ny,nx,seen))
                        
            seen.add((i,j))
        for y,x in delete_target:
            deleted[y][x] = True
    
    def DFS2(target):
        for i in range(n):
            for j in range(m):
                if storage[i][j] == target:
                    deleted[i][j] = True
                    
                    for k in range(4) :
                        ny = dy[k] + i
                        nx = dx[k] + j
                        if ny < 0 or nx <0 or ny >= n or nx >= m :
                            continue
                        if line[ny][nx] and deleted[ny][nx]:
                            line[i][j] = True
    
    for request in requests:
        if len(request) == 1:
            DFS1(request)
        else:
            DFS2(request[0])
    
    answer=0
    for y_idx,y in enumerate(deleted):
        for x_idx,x in enumerate(y) :
            if x == False :
                answer += 1
    return answer