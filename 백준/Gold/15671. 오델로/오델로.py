N = int(input())
maps = [[] for i in range(6)]

for r in range(6):
    for c in range(6):
        maps[r].append('.')

maps[2][2] ='W'
maps[3][3] ='W'
maps[2][3]= 'B'
maps[3][2]='B'
currMap = {0:'B',1:'W'}
currIdx = 1

# 현재 방향 체크
def isBlock(dir_y,dir_x,y,x,rev,curr):
    isCurr = False
    isRev = False
    change= []

    y = y + dir_y
    x = x + dir_x
    if y >= 0 and x >=0 and y < 6 and x < 6 and maps[y][x] == rev:
        isRev = True
        change.append([y,x])
    else:
        return False

    while y + dir_y >= 0 and x + dir_x>=0 and y + dir_y < 6 and x+ dir_x < 6 :
        y = y + dir_y
        x = x + dir_x
        if maps[y][x] == curr :
            isCurr = True
            break
        elif maps[y][x] == rev and isRev == True:
            change.append([y,x])
        else:
            return False

    if isRev and isCurr:
        return change
    return False

# 8방향 정의
direction_y = [-1,-1,-1,0,1,1,1,0]
direction_x = [-1,0,1,1,1,0,-1,-1]

for i in range(N):
    R,C = map(int,input().split())
    currIdx = not currIdx
    maps[R-1][C-1] = currMap[currIdx]

    for i in range(8):
        result = isBlock(direction_y[i], direction_x[i], R-1, C-1, currMap[not currIdx], currMap[currIdx])
        if result:
            for y,x in result:
                maps[y][x] = currMap[currIdx]

wCnt = 0
bCnt = 0
for i in maps:
    print(''.join(i))
    for j in i:
        if j == 'W':
            wCnt += 1
        elif j == 'B':
            bCnt += 1

print('White' if wCnt > bCnt else 'Black')

