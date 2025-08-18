def solution(mats, park):
    mats.sort(reverse= True)
    max_num = -1
    def isPossible(i,j):
        for mat in mats:
            isPossible = True
            for y in range(mat):
                for x in range(mat):
                    if (i+y) < 0 or (i+y) >= len(park) or j+x < 0 or j+x >= len(park[0]):
                        isPossible = False
                        break
                    if park[i+y][j+x] != "-1":
                        isPossible = False
                        break
            if isPossible :
                return mat
        return -1
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            max_num = max(isPossible(i,j),max_num)
    return max_num