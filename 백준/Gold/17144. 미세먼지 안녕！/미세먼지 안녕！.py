import math
R,C,T = map(int,input().split())
maps = []
clean = []

for i in range(R):
    inp = list(map(int,input().split()))
    maps.append(inp)
    for j in range(C):
        if inp[j] == -1:
            clean.append([i,j])

def copyMap(maps):
    newMaps = [[] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            newMaps[i].append(maps[i][j])
    return newMaps

def findSmoke(maps):
    currSmoke = []
    for i in range(R):
        for j in range(C):
            if maps[i][j] > 0:
                currSmoke.append([i,j])

    return currSmoke

dy = [1,-1,0,0]
dx = [0,0,1,-1]

# 상하좌우 탐색하면서 공청기가 아니거나 영역을 나가지 않는다면 새로운 배열에 입력
def spreadSmoke(smoke,pos,maps,newMap):
    count = 0
    y,x = pos
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny >= R or nx >= C:
            continue
        if maps[ny][nx] == -1:
            continue

        newMap[ny][nx] += smoke
        count += 1
    newMap[y][x] -= smoke * count

def cleaning(clean,maps,newMaps):
    headMoveX = [1,0,-1,0]
    headMoveY = [0,-1,0,1]

    tailMoveX = [1,0,-1,0]
    tailMoveY = [0,1,0,-1]

    head_y,head_x = clean[0]
    tail_y,tail_x = clean[1]

    cleanMove(head_y,head_x,headMoveY,headMoveX,maps,newMaps)
    cleanMove(tail_y,tail_x,tailMoveY,tailMoveX,maps,newMaps)

def cleanMove(y,x,moveY,moveX,maps,newMaps):
    for i in range(4):
        while True:
            if y+moveY[i] < 0 or x+moveX[i] < 0 or y+moveY[i] >= R or x+moveX[i] >= C:
                break

            if newMaps[y+moveY[i]][x+moveX[i]] == -1:
                break

            if maps[y][x] == -1:
                newMaps[y + moveY[i]][x + moveX[i]] = 0

            else:
                newMaps[y + moveY[i]][x + moveX[i]] = maps[y][x]
            y = y + moveY[i]
            x = x + moveX[i]

def copyCurrValue(maps,newMaps):
    for i in range(R):
        for j in range(C):
            maps[i][j] = newMaps[i][j]

for i in range(T):
    newMaps = copyMap(maps)
    currSmoke = findSmoke(maps)

    for y,x in currSmoke:
        smoke = maps[y][x] // 5
        spreadSmoke(smoke, [y,x], maps, newMaps)

    copyCurrValue(maps, newMaps)
    cleaning(clean, maps, newMaps)
    maps = newMaps

ans = 0
for i in range(R):
    for j in range(C):
        if maps[i][j] == -1:
            continue
        ans += maps[i][j]
print(ans)