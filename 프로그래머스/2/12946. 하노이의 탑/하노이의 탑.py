global answer
answer= []

def hanoi(n,fromIdx,toIdx,supportIdx):
    global answer
    if n == 1 :
        answer.append([fromIdx,toIdx])
        return
        
    #n-1개의 원판을 보조 기둥으로 옮긴다.
    hanoi(n-1,fromIdx,supportIdx,toIdx)
    
    #맨 아래 원판을 목적지 기둥으로 옮긴다.
    answer.append([fromIdx,toIdx])
    
    #보조 기둥에 있던 n-1개의 원판을 목적지 기둥으로 옮긴다.
    hanoi(n-1,supportIdx,toIdx,fromIdx)

def solution(n):
    hanoi(n,1,3,2)
    
    return answer