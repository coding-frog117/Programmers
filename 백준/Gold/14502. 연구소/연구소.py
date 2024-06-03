from itertools import combinations
import sys

dy = [1,-1,0,0]
dx = [0,0,1,-1]
ans = 0
N,M= map(int,input().split())
empty = []
maps = []
virus = []

def makeCopyMap(maps):
    newMaps = [[] for i in range(N)]
    for r_idx, r in enumerate(maps):
        for c_idx,c in enumerate(r):
            newMaps[r_idx].append(c)
    return newMaps

def countEmpty(maps):
    empty = []
    for idx,r in enumerate(maps):
        for i,c in enumerate(r):
            if c == 0:
                empty.append([idx,i])
    return empty

def spread(maps,y,x):
    count = 0
    isPossible = False
    # 네 방향으로 가능한 부분까지 확산
    for i in range(4):
        ny = y
        nx = x
        while True:
            ny = ny + dy[i]
            nx = nx + dx[i]

            if ny < 0 or ny >= N or nx <0 or nx >= M:
                break

            if maps[ny][nx] == 1:
                break

            if maps[ny][nx] == 0:
                count += 1
                isPossible = True
                maps[ny][nx] = 2
                spread(maps,ny,nx)
    if isPossible == False:
        return False

    # return count if maxCount < count else maxCount

for i in range(N):
    inp = list(map(int,input().split()))
    maps.append(inp)
    for idx, c in enumerate(inp):
        if c == 0:
            empty.append([i,idx])
        elif c == 2:
            virus.append([i,idx])

combi = list(combinations(empty,3))

# 각 조합마다 새로운 maps을 만들어 spread 시킴
for i in combi :
    newMaps = makeCopyMap(maps)
    for y,x in i :
        newMaps[y][x] = 1
    empty = countEmpty(newMaps)
    currCount = 0
    for y,x in virus:
        spread(newMaps, y, x)
    for idx,r in enumerate(newMaps):
        for i,c in enumerate(r):
            if newMaps[idx][i] == 0:
                currCount+=1

    ans = max(currCount,ans)
print(ans)