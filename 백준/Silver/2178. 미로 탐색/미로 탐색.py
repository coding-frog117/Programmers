from collections import deque
N,M = map(int,input().split())
maps = []
queue = deque()
queue.append([0,0])
for i in range(N):
    col = list(map(int,list(input())))
    maps.append(col)

dy=[1,-1,0,0]
dx =[0,0,1,-1]

while queue:
    y,x = queue.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny <0 or ny >= N or nx < 0 or nx >= M:
            continue
        if maps[ny][nx] == 1:
            maps[ny][nx] = maps[y][x]+1
            queue.append([ny,nx])

print(maps[N-1][M-1])