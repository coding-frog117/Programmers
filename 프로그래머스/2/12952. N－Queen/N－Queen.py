answer = 0
def solution(n):
    if (n==1):
        return 1
    def BT(x,ny,diagonal_right, diagonal_left):
        if (x > n-1):
            global answer
            answer += 1
        
        for i in range(n):
#           y좌표, 대각선 오른쪽, 대각선 왼쪽에 대한 조건을 만족하는지 체크
            if ((i not in ny) and (i+x not in diagonal_right) and (i-x not in diagonal_left)):
                BT(x+1, ny + [i], diagonal_right + [i+x], diagonal_left + [i-x])
    
    for i in range(n):
        BT(1,[i],[i],[i])
    
    return answer