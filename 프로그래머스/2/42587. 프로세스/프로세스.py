from collections import deque

prioritiesDict ={}
seen = []

def solution(priorities, location):
    queue = deque(priorities)
    numberQueue = deque(priorities)
    
    queue[location] = 'target'
    
    while queue :
        if (len(seen) == len(priorities)):
            break
            
        current = queue.popleft()
        currentNumber = numberQueue.popleft()
        
        if (len(list(numberQueue)) ==0):
            seen.append(current)
            
        elif (max(list(numberQueue)) > currentNumber):
            numberQueue.append(currentNumber)
            queue.append(current)
            
        else :
            seen.append(current)
    
    return seen.index('target')+1