def solution(n):
    init = bin(n)[2:]
    cnt = init.count('1')
    cur = n+1
    
    while True:
        if bin(cur)[2:].count('1') == cnt :
            return cur
        cur += 1