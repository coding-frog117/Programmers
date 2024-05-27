def solution(msg):
    dic = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    
    # 아이디어 - 사전에 있으면 answer에 추가, 다음 글자가 없으면 사전에 등록
    
    answer = []
    currNum = 26
    msg = list(msg)
    isLast = False
    skipCount = 0
    
    for i in range(len(msg)):
        if isLast :
            break
        
        if skipCount > 1:
            skipCount -= 1
            continue
        else:
            currString = ''
            for j in range(i,len(msg)):
                if dic.get(currString + msg[j]) :
                    currString += msg[j]
                    if j == len(msg)-1:
                        answer.append(dic[currString])
                        isLast = True
                        break

                else :
                    if currString :
                        answer.append(dic[currString])
                        currNum += 1
                        dic[currString+ msg[j]] = currNum
                        skipCount = len(currString)
                        break
    return answer