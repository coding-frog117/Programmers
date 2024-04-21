from collections import deque

def solution(n, edge):
    queue = deque()
    
    vertexList = [[] for i in range(n)]
    countList = [0 for i in range(n)]
    seenList= [False for i in range(n)]
    
    for a,b in edge:
        vertexList[a-1].append(b)
        vertexList[b-1].append(a)
    
    seenList[0] = True
    queue.append(1)
    maxCount =0
    
    while queue:
        target = queue.popleft() -1
        for node in vertexList[target]:
            if (seenList[node-1] == False):
                queue.append(node)
                seenList[node-1] = True
                
                countList[node-1] = countList[target] + 1
                if (countList[node-1] > maxCount):
                    maxCount = countList[node-1]
                    
    answer =0
    for i in countList:
        if maxCount == i:
            answer += 1
        
    return answer