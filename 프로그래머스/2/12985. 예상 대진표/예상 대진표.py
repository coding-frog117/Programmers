def solution(n,a,b):
    a = (a+1) // 2
    b = (b+1) // 2
    
    if a+1 // 2 == b+1 // 2 :
        return 1
    
    ans = 1
    while True:
        ans += 1
        if (a+1) // 2 == (b+1) //2:
            return ans
        a = (a+1) // 2
        b = (b+1) // 2
        