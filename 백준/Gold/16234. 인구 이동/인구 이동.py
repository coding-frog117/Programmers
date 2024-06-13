from collections import deque

N,lower,upper = list(map(int,input().split()))
maps = []
copyMaps = []
for i in range(N):
    inp = list(map(int,input().split()))
    maps.append(inp)
answer = 0

dy = [1,-1,0,0]
dx = [0,0,1,-1]

def dfs(maps,copyMaps,changeMaps,queue):
    count = 0
    while queue:
        y, x, seen = queue.pop()
        copyMaps[y][x] = True

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue

            if copyMaps[ny][nx] == 1:
                continue
            sub = abs(maps[y][x] - maps[ny][nx])
            if sub >= lower and sub <= upper:
                seen.append([ny,nx])
                queue.append([ny, nx, seen])
                copyMaps[ny][nx] = True

        if len(queue) == 0:
            seen = set(list(map(tuple,seen)))
            size = len(seen)
            if size == 1:
                seen = list(seen)
                y,x = seen[0]
                copyMaps[y][x] = True
                return False
            else:
                for i in seen:
                    y,x = i
                    count += maps[y][x]
                result = count // size
                for i in seen:
                    y, x = i
                    changeMaps[y][x] = result
                return True
            break

while True:
    isCount = False
    count = 0
    copyMaps = [[0 for i in range(N)] for i in range(N)]
    changeMaps = [[] for i in range(N)]
    for r_idx,r in enumerate(maps):
        for c_idx,c in enumerate(r):
            changeMaps[r_idx].append(c)

    # 현재 연합이 몇개인지 확인
    while True:
        isPossible = False
        for r_idx,r in enumerate(copyMaps):
            for c_idx,c in enumerate(r):
                if c != True:
                    isPossible = True
                    if copyMaps[r_idx][c_idx] == True:
                        continue
                    queue = []
                    queue.append([r_idx, c_idx, [[r_idx, c_idx]]])
                    result = dfs(maps,copyMaps,changeMaps,queue)
                    # 연합이 존재하면 체크
                    if result :
                        isCount = True
        # True인 곳이 없으면 변화된 map 복사 후 현재 단계 종료
        if not isPossible:
            for r_idx,r in enumerate(maps):
                for c_idx,c in enumerate(r):
                    maps[r_idx][c_idx] = changeMaps[r_idx][c_idx]
            break
    if isCount:
        answer += 1
    else:
        break
print(answer)