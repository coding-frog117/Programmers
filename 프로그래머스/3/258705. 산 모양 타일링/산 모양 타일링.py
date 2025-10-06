# 각 위치에 맞게 배열 생성, 위에 삼각형을 붙인 경우는 1로 표현...
# dp로 최종 타일 갯수 구하기

def solution(n, tops):
    triangles = [0]
    tiles = []
    cur_idx = 0
    while cur_idx < n:
        if tops[cur_idx] == 0:
            triangles.append(0)
            triangles.append(0)
        else:
            triangles.append(0)
            triangles.append(1)
            triangles.append(0)
        cur_idx+=1
    
    for idx, triangle in enumerate(triangles):
        if idx == 0:
            tiles.append(1)
            continue
        if idx == 1:
            tiles.append(2)
            continue
        
        if triangles[idx-1] == 1:
            cur_tiles = tiles[-1] + tiles[-3]
            tiles.append(cur_tiles %10007)
        else:
            cur_tiles = tiles[-1] + tiles[-2]
            tiles.append(cur_tiles % 10007)
    return tiles[-1] % 10007