from itertools import combinations

def checkPerson(maps):
    person = []
    for idx,r in enumerate(maps):
        for i,c in enumerate(r):
            if maps[idx][i] == 'P':
                person.append([idx,i])
    return person
    
def checkLen(p1,p2):
    p1_y,p1_x = p1
    p2_y,p2_x = p2
    return abs(p2_y-p1_y) + abs(p2_x-p1_x)

def isPartition(maps,p1,p2):
    p1_y,p1_x = p1
    p2_y,p2_x = p2
    # y가 같은경우 x사이에 파티션 확인
    if p2_y == p1_y:
        if maps[p2_y][p2_x-1] == 'X':
            return True
        return False
    # x가 같은경우 y사이에 파티션 확인
    elif p2_x == p1_x :
        if maps[p2_y-1][p2_x] == 'X':
            return True
        return False
    # 오른쪽 대각선 방향에 위치할 경우(x,y 둘다 다름)
    elif p1_x < p2_x:
        if maps[p1_y][p1_x+1] == 'X' and maps[p2_y][p2_x-1] == 'X':
            return True
        return False
    # 왼쪽 대각선 방향에 위치할 경우(x,y 둘다 다름)
    elif p1_x > p2_x:
        if maps[p1_y][p1_x-1] == 'X' and maps[p2_y][p2_x+1] == 'X':
            return True
        return False

def solution(places):
    answer = []
    for place in places:
        maps = []
        for idx,val in enumerate(place):
            maps.append(list(val))
        person = checkPerson(maps)
        
        if not person:
            answer.append(1)
            continue
            
        isPossible =True
        shortPos = []
        combi = list(combinations(person,2))
        for i in combi:
            length =checkLen(i[0],i[1])
            # 상호 거리가 1이면 무조건 False
            if length == 1:
                answer.append(0)
                isPossible = False
                break
            # 상호 거리가 2면 위치 저장
            elif length <= 2:
                shortPos.append([i[0],i[1]])
                    
        if isPossible == False:
            continue
        # 파티션이 존재하는지 확인
        for i in shortPos:
            i.sort()
            p1,p2 = i
            if not isPartition(maps,p1,p2):
                isPossible = False
        
        if isPossible :
            answer.append(1)
        else:
            answer.append(0)
    return answer