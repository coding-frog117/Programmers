# 해결 전략 : 연결된 동남서북 방향 블록 체크, 같은 문자면 탐색 이어감
# 탐색 초기 블록 설정? -> 모든 아이템 저장 후 시작
# 터진후 아래로 내려오는 블록 확인 -> 터진 블록 None 으로 만든후 블록을 거꾸로 돌면서 블록 채우기

dx =[1,0,-1,0]
dy = [0,1,0,-1]

def poll(maps,m,n):
    newMap = [[None for i in range(n)] for i in range(m)]
    # 55,45,35,25,15,05,  45,35...
    # 거꾸로 돌면서 각 행을 채워나감
    for i in range(n-1,-1,-1):
        curr_x = i
        curr_y = m-1
        for j in range(m-1,-1,-1):   
            if maps[j][i] == None:
                continue
            newMap[curr_y][curr_x] = maps[j][i]
            curr_y -= 1

    return newMap

def appendStack(maps):
    stack = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != None:
                stack.append([i,j,maps[i][j],[[i,j]]])
    return stack

def find(m,n,stack,maps):
    popBlock = []
    while stack:
        ny,nx,char,route = stack.pop()
        isPossible = True
        
        for i in range(4):
            ny = ny + dy[i]
            nx = nx + dx[i]
            
            if ny < 0 or nx<0 or nx >= n or ny >= m:
                isPossible = False
                break
            
            if maps[ny][nx] != char :
                isPossible = False
                break
            
            route.append([ny,nx])

        if isPossible:
            for i in route:
                if i not in popBlock:
                    popBlock.append(i)
    return popBlock
    
def solution(m, n, board):
    for i in range(len(board)):
        board[i] = list(board[i])
    answer = 0
    while True:
        stack = appendStack(board)
        popBlock = find(m,n,stack,board)
        
        if not popBlock :
            break
            
        answer += len(popBlock)
    
        for y,x in popBlock:
            board[y][x] = None
    
        board = poll(board,m,n)   

    return answer