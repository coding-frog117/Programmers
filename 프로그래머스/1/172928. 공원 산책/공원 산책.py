def solution(park, routes):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    pos = {"N" : 0, "S": 1, "W" : 2, "E" : 3}
    y,x = [0,0]
    for y_idx,i in enumerate(park):
        for x_idx,j in enumerate(i):
            if j == "S":
                y,x = [y_idx,x_idx]

    for r in routes:
        isPossible = True
        position,count = r.split(" ")
        ny= y
        nx = x

        for i in range(int(count)):
            ny = ny + dy[pos[position]]
            nx = nx + dx[pos[position]]
            if ny < 0 or nx < 0 or ny >= len(park) or nx >= len(park[0]):
                isPossible = False
                continue
            if park[ny][nx] == "X" :
                isPossible = False
                continue
        if isPossible:
            y= ny
            x = nx
    return [y,x]