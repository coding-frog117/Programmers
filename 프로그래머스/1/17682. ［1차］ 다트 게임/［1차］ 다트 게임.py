def solution(dartResult):
    score = [0,0,0]
    dart = []
#   먼저 세번의 다트결과를 구분해서 나누기
    currStr = ''
    
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if currStr and currStr[-1].isalpha():
                dart.append(currStr)
                currStr = dartResult[i]
            else:
                currStr += dartResult[i]
            
        elif dartResult[i] == '*' or dartResult[i] == '#':
            currStr += dartResult[i]
            dart.append(currStr)
            currStr = ''
        else:
            currStr += dartResult[i]
            
    if currStr:
        dart.append(currStr)
    
    # S,D,T 에 따라 다른 가중치 부여
    def multipleNum(num,t):
        if t == 'S':
            return num
        elif t == 'D':
            return num * num
        elif t == 'T':
            return num * num * num
    
    #각 회차마다 계산하기 , 가중치 더하기
    for i in range(len(dart)):
        for j in range(len(dart[i])):
            if dart[i][j] == '1' and dart[i][j+1] == '0':
                score[i] += 10
            elif dart[i][j].isdigit() :
                score[i] += int(dart[i][j])
            elif dart[i][j].isalpha():
                score[i] = multipleNum(score[i],dart[i][j])
            elif dart[i][j] == '*':
                if i != 0:
                    score[i-1] *= 2
                score[i] *= 2
            elif dart[i][j] == '#':
                score[i] *= -1
                
    return sum(score)