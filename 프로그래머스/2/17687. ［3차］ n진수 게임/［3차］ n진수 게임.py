def solution(n, t, m, p):
    count = 0
    finish = 0
    num = 1
    answer= '0'
    
    invertAlpha = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    
    def invertNum(num,n):
        ans = ''
        while True:
            if num > 0:
                num,mod = divmod(num,n)
                if mod >= 10 and mod <= 15:
                    ans = str(invertAlpha[mod]) + ans
                else:
                    ans = str(mod) + ans
            else:
                break

        return ans
    
    while True:
        if n == 16:
            invert = hex(num)
            invert = invert[2:].upper()
        else:
            invert = invertNum(num,n)
        num += 1
        
        # 말한 사람수를 더하기> 멤버수보다 많으면 finish-멤버수로 바꾸고 count 갱신
        finish += len(invert)
        answer += invert
        
        if finish >= m and finish > 0:
            div,mod = divmod(finish,m)
            finish = mod
            count += div
        if count > t :
            break

    tube = ""
    tubeIdx = p-1
    while len(tube) < t :
        tube += answer[tubeIdx]
        tubeIdx += m
    return tube