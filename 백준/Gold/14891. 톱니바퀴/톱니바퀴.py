arr = []

def move(idx,move,arr):
    if move == True or move == 1:
        arr[idx] = [arr[idx][-1]] + arr[idx][:-1]
    else:
        arr[idx] = arr[idx][1:] + [arr[idx][0]]

def isMove(curr,other,moveDir):
    # 왼쪽 방향
    if moveDir == 1:
        if curr[6] != other[2]:
            return True
    # 오른쪽 방향
    else:
        if curr[2] != other[6]:
            return True
    return False

for i in range(4):
    inp = list(map(int,list(input())))
    arr.append(inp)

K= int(input())
for i in range(K):
    idx,dir = map(int,input().split())
    # move(idx-1,dir,arr)

    result = []
    # 왼쪽 방향 확인
    checkIdx = 1
    leftIdx = idx-1
    curr_dir = dir * -1
    while leftIdx > 0:
        if isMove(arr[leftIdx], arr[leftIdx-1], checkIdx):
            result.append([leftIdx - 1, curr_dir])
            leftIdx -= 1
            curr_dir = curr_dir * -1
        else:
            break

    # 오른쪽 방향 확인
    checkIdx = -1
    rightIdx = idx-1
    curr_dir = dir * -1
    while rightIdx < 3:
        if isMove(arr[rightIdx], arr[rightIdx + 1], checkIdx):
            result.append([rightIdx + 1, curr_dir])
            rightIdx += 1
            curr_dir = curr_dir * -1
        else:
            break
    # 현재 바퀴 이동
    move(idx-1,dir,arr)

    # 이웃된 바퀴 연쇄 이동
    for i in result:
        idx,dir = i
        move(idx,dir,arr)

    answer = 0
    mul = 1
for idx,val in enumerate(arr):
    if val[0] == 1:
        answer += mul
    mul *= 2
print(answer)