from collections import deque

def solution(land):
    rows, cols = len(land), len(land[0])
    visited = [[False]*cols for _ in range(rows)]
    group_size = [[0]*cols for _ in range(rows)]
    sizes = [] 

    dy = [1,-1,0,0]
    dx = [0,0,1,-1]

    def bfs(sy, sx, group_id):
        q = deque([(sy, sx)])
        visited[sy][sx] = True
        cells = [(sy, sx)]
        count = 1
        while q:
            y, x = q.popleft()
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < rows and 0 <= nx < cols and not visited[ny][nx] and land[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    cells.append((ny, nx))
                    count += 1
        for y, x in cells:
            group_size[y][x] = group_id
        return count

    group_id = 1
    id_to_size = {}
    for y in range(rows):
        for x in range(cols):
            if land[y][x] == 1 and not visited[y][x]:
                size = bfs(y, x, group_id)
                id_to_size[group_id] = size
                group_id += 1

    answer = 0
    for x in range(cols):
        seen = set()
        total = 0
        for y in range(rows):
            gid = group_size[y][x]
            if gid > 0 and gid not in seen:
                seen.add(gid)
                total += id_to_size[gid]
        answer = max(answer, total)

    return answer