def solution(n):
    triangle = [[0] * (i+1) for i in range(n)]
    
    dr = [1, 0, -1]
    dc = [0, 1, -1]
    
    num = 1
    r, c = 0, 0
    dir_idx = 0 
    
    for i in range(n * (n+1) // 2):
        triangle[r][c] = num
        num += 1
        
        nr, nc = r + dr[dir_idx], c + dc[dir_idx]
        # 범위 벗어나거나 이미 채워진 경우 방향 전환
        if not (0 <= nr < n and 0 <= nc <= nr and triangle[nr][nc] == 0):
            dir_idx = (dir_idx + 1) % 3
            nr, nc = r + dr[dir_idx], c + dc[dir_idx]
        r, c = nr, nc
    
    # 2차원 배열 → 1차원 flatten
    return [num for row in triangle for num in row]