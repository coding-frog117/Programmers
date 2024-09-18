def solution(board, skill):
    degreeArr = [[0 for i in range(len(board[0])+1)] for i in range(len(board)+1)]
    for t,start_x,start_y,end_x,end_y,degree in skill:
        if t == 1:
            degreeArr[start_x][start_y] += (-degree)
            degreeArr[end_x+1][start_y] += (degree)
            degreeArr[start_x][end_y+1] += (degree)
            degreeArr[end_x+1][end_y+1] += (-degree)
        else :
            degreeArr[start_x][start_y] += (degree)
            degreeArr[end_x+1][start_y] += (-degree)
            degreeArr[start_x][end_y+1] += (-degree)
            degreeArr[end_x+1][end_y+1] += (degree)
    
    for r_idx,row in enumerate(degreeArr):
        total = 0
        for c_idx,degree in enumerate(row):
            total += degree
            degreeArr[r_idx][c_idx] = total
    
    for c_idx in range(len(degreeArr[0])):
        total = 0
        for r_idx in range(len(degreeArr)):
            total += degreeArr[r_idx][c_idx]
            degreeArr[r_idx][c_idx] = total
    
    ans = 0
    for r_idx,row in enumerate(board):
        for c_idx,col in enumerate(row):
            if col + degreeArr[r_idx][c_idx] > 0:
                ans += 1
    return ans
                