# 비트연산
def solution(n, arr1, arr2):
    map1 = []
    map2 = []
    for num in arr1:
        invert = str(bin(num))[2:]
        if len(invert) < n:
            plusStr = n-len(invert)
            plusStr = '0' * plusStr
            invert = plusStr + invert
        map1.append(invert)
    
    for num in arr2:
        invert = str(bin(num))[2:]
        if len(invert) < n:
            plusStr = n-len(invert)
            plusStr = '0' * plusStr
            invert = plusStr + invert
        map2.append(invert)
    
    ansMap = ['' for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            ans = '1' if (map1[i][j] == '1' or map2[i][j] =='1') else '0'
            if ans == '1':
                ansMap[i] +='#'
            else:
                ansMap[i] +=' '
                
    return ansMap