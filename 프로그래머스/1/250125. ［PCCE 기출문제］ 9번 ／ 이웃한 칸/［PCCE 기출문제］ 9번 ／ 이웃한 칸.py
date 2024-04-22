def solution(board, h, w):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    answer = 0
    
    x= w
    y= h
    color = board[h][w]
    
    for i in range(len(dx)):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if (nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board)):
            continue
        if (board[ny][nx] == color):
            answer += 1
        
    return answer