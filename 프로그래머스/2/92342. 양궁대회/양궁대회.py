from itertools import combinations
from itertools import product

def calScore(apeach,lion):
    apeachScore = 0
    lionScore = 0
    for i,(a,l) in enumerate(zip(apeach,lion)):
        if a < l :
            lionScore += (10-i)
        elif a != 0 and a >= l :
            apeachScore += (10-i)
    if apeachScore >= lionScore:
        return False
    return lionScore-apeachScore
    
def solution(n, info):
    answer = []
    case = []
    for idx,i in enumerate(info):
        if idx != 10:
            case.append([i+1,0])
        else:
            case.append([0,0])
    allCases = list(product(*case))
    
    for c in allCases:
        summation = sum(c)
        if summation > n:
            continue
        elif summation == n :
#             이기는 경우라면 answer에 추가
            result = calScore(info,c)
            if result:
                rev = list(reversed(list(c)))
                answer.append([result,tuple(rev)])
                
        elif summation < n:
            appendNum = n-summation
            c = list(c)
            c[-1] += appendNum
            result = calScore(info,tuple(c))
            if result:
                rev = list(reversed(c))
                answer.append([result,tuple(rev)])
    answer.sort(reverse=True)

    if not answer:
        return [-1]
    answer = list(reversed(answer[0][1]))
    return answer
