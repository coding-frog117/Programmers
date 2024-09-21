
                
def solution(key, lock):
    def rotateKey(key):
#         [2,1] => [1,0] , [2,0] => [0,0]
        newKey = [[0]*len(key) for i in range(len(key))]
        for i in range(n):
            for j in range(n):
                newKey[i][j] = key[n-1-j][i]
        return newKey

    def checkSum(maps):
        for row in range(m):
            for col in range(m):
                if maps[row+m][col+m] != 1:
                    return False
        return True
    
#     lock 맵 늘리기
    n = len(key)
    m = len(lock)
    new_lock = [[0]*(m*3) for i in range(m*3)]
    for i in range(m):
        for j in range(m):
            new_lock[i+m][j+m] = lock[i][j]
    
    rotated = []
    for i in range(4):
        if not rotated:
            rotated.append(rotateKey(key))
        else:
            rotated.append(rotateKey(rotated[-1]))
    for k in range(4):
        for i in range(m*2):
            for j in range(m*2):
                for y in range(n):
                    for x in range(n):
                        key = rotated[k]
                        new_lock[y+i][x+j] += key[y][x]
                # print(new_lock)
                if checkSum(new_lock) == True:
                    return True
                
                for y in range(n):
                    for x in range(n):
                        key = rotated[k]
                        new_lock[y+i][x+j] -= key[y][x]
    return False
                                        