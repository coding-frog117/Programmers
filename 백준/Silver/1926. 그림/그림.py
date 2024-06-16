N,M = map(int,input().split())
maps = []
for i in range(N):
    col = list(map(int,input().split()))
    maps.append(col)

dy = [1,-1,0,0]
dx = [0,0,1,-1]
def DFS(maps,y,x):
    stack = [[y,x]]
    seen = []
    while stack:
        y,x = stack.pop()
        seen.append([y,x])

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if maps[ny][nx] == 1:
                stack.append([ny,nx])
                maps[ny][nx] = maps[y][x] + 1
    return seen

count = 0
maxSize = 0
for r_idx,r in enumerate(maps):
    for c_idx,c in enumerate(r):
        if maps[r_idx][c_idx] == 1:
            count += 1
            maps[r_idx][c_idx] = 2
            result = DFS(maps,r_idx,c_idx)
            maxSize = max(maxSize,len(result))
print(count)
print(maxSize)